import pandas as pd
import numpy as np
import re, string
import nltk

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')

# Remove punctuation function
def remove_punctuation(text):
    text = ''.join(char for char in text if char not in string.punctuation)
    return text

def tokenize(text):
    tokens = re.split('\W+', text)
    return tokens

def remove_stopwords(tokenized_list):
    text = [word for word in tokenized_list if word not in stopwords]
    return text

# Load the dataset
file_name = 'SMSSpamCollection.tsv'

df = pd.read_csv(file_name, sep="\t", header=None)
df.columns = ['Person', 'text']

# Apply the remove punctuation function to the 'text' column
df['text'] = df['text'].apply(remove_punctuation)

# Apply the tokenize function to the 'text' column
df['text'] = df['text'].apply(lambda x: tokenize(x.lower()))

# Remive stopwords
df['text'] = df['text'].apply(lambda x: remove_stopwords(x))

print(df.head())