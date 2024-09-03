#!/usr/bin/env python
# coding: utf-8
# !pip install py3-validate-email pandas nltk gspread scikit-learn
import pandas as pd
import re, string, nltk, gspread
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold, cross_val_score
from sklearn.model_selection import train_test_split
from io import StringIO

# Check if NLTK resources are already downloaded
try:
    nltk.data.find('corpora/stopwords.zip')
    nltk.data.find('corpora/wordnet.zip')
except LookupError:
    nltk.download('stopwords')
    nltk.download('wordnet')

stopwords = nltk.corpus.stopwords.words('english')
lem = nltk.WordNetLemmatizer()

def preprocess_text(text):
    text = re.sub(f"[{string.punctuation}]", "", text.lower())
    tokens = re.split('\W+', text)
    tokens = [word for word in tokens if word not in stopwords and word]
    tokens = [lem.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

def punctuation_percentage(text):
    if len(text) == 0 or len(text.strip()) == 0:
        return 0.0  # Return 0% if the text is empty or contains only whitespace

    count = sum([1 for char in text if char in string.punctuation])
    return round(count / (len(text) - text.count(' ')), 3) * 100

def read_data_from_google_sheet(sheet):
    # Fetch all data from the Google Sheet
    data = sheet.get_all_records()
    return pd.DataFrame(data)

def extract_email(sender):
    # Use regex to extract email from the sender string
    match = re.search(r'<(.*?)>', sender)
    return match.group(1) if match else sender

# Running in SageMaker Notebook Instance
# Initialize Google Sheets client
gc = gspread.service_account(filename='cred.json')
gsheet = gc.open("Email Data").get_worksheet(1)

# Read data from Google Sheet
df = read_data_from_google_sheet(gsheet)

# Apply the extract_email function to the 'Sender' column
df['Sender'] = df['Sender'].apply(extract_email)

# # Extract the 'Body' column for NLP processing
df['punctuation_percentage'] = df['Body'].apply(punctuation_percentage)
df['Body'] = df['Body'].apply(preprocess_text)

# Calculate the body length
df['body_length'] = df['Body'].apply(lambda x: len(x) - x.count(' '))

# # Perform train-test split
# X_train, X_test, y_train, y_test = train_test_split(df[['Body', 'punctuation_percentage']], df['Subject'], test_size=0.2)



# # Save the first 10 lines of training data to CSV
# X_train.head(10).to_csv('Sample_Training_Dataset.csv', index=False)

# print("Sample training data saved as 'Sample_Training_Dataset.csv'")

# Vectorizing the data using TF-IDF
Tfidf_vect = TfidfVectorizer(analyzer=preprocess_text)
X_tfidf = Tfidf_vect.fit_transform(df['Body'])

# Combine the features into a DataFrame
X_features = pd.concat([df[['punctuation_percentage', 'body_length']], pd.DataFrame(X_tfidf.toarray())], axis=1)

# X_features.head()

X_features.columns = X_features.columns.astype(str)
# X_features.head()
df.head()