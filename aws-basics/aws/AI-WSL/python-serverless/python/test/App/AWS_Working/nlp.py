#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import re, string, nltk, boto3
from io import StringIO
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split


# In[2]:


# Check if NLTK resources are already downloaded
try:
    nltk.data.find('corpora/stopwords.zip')
    nltk.data.find('corpora/wordnet.zip')
except LookupError:
    nltk.download('stopwords')
    nltk.download('wordnet')

stopwords = nltk.corpus.stopwords.words('english')
lem = nltk.WordNetLemmatizer()


# In[3]:


def preprocess_text(text):
    text = re.sub(f"[{string.punctuation}]", "", text.lower())
    tokens = re.split('\W+', text)
    tokens = [word for word in tokens if word not in stopwords and word]
    tokens = [lem.lemmatize(word) for word in tokens]
    return ' '.join(tokens)


# In[34]:


def punctuation_percentage(text):
    if len(text) == 0 or len(text.strip()) == 0:
        return 0.0  # Return 0% if the text is empty or contains only whitespace
    
    count = sum([1 for char in text if char in string.punctuation])
    return round(count / (len(text) - text.count(' ')), 3) * 100


# In[38]:


# Accessing S3 Bucket, Which Contains CSV File
bucket_name = 'mlnlp0608'
file_key = 'SMSSpamCollection.tsv'

# Create a boto3 client to interact with S3
s3_client = boto3.client('s3')

# Fetch the CSV file from S3
response = s3_client.get_object(Bucket=bucket_name, Key=file_key)

# Read the CSV content
csv_content = response['Body'].read().decode('utf-8')

# Convert the CSV content to a pandas DataFrame with specific parameters
df = pd.read_csv(StringIO(csv_content), sep="\t", header=None, names=['Person', 'text'])


# In[39]:


# Split the Training Data Set for NLP Modal
# Adding a feature - punctuation percentage in the text
df['punctuation_percentage'] = df['text'].apply(punctuation_percentage)

# Apply preprocessing
df['text'] = df['text'].apply(preprocess_text)

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(df[['text', 'punctuation_percentage']], df['Person'], test_size=0.2)
        
# Save the first 10 lines of training data to a CSV file
# X_train.head(10).to_csv('training_data.csv', index=False)
# Put the training dataset in the S3 Bucket

# Uploading to Sample_Training_Dataset.csv
FILE_NAME = 'Sample_Training_Dataset.csv'

csv_content = X_train.head(10).to_csv(index=False)

try:
    # Check if the file exists
    s3_client.head_object(Bucket=bucket_name, Key=FILE_NAME)
    print(f'{FILE_NAME} already exists in {bucket_name}. Clearing content and uploading new data...')
    
    # Clear existing content by uploading new data
    s3_client.put_object(Bucket=bucket_name, Key=FILE_NAME, Body=csv_content)
    print(f'{FILE_NAME} has been updated in {bucket_name}.')
    
except s3_client.exceptions.ClientError as e:
    if e.response['Error']['Code'] == '404':
        # File does not exist, create it
        print(f'{FILE_NAME} does not exist. Creating file...')
        s3_client.put_object(Bucket=bucket_name, Key=FILE_NAME, Body=csv_content)
        print(f'{FILE_NAME} has been created in {bucket_name}.')
    else:
        print(f'Error checking file existence: {e}')
except (NoCredentialsError, PartialCredentialsError) as e:
    print(f'Credentials error: {e}')


# In[ ]:





# In[ ]:




