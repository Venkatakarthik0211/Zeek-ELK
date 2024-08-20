#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import re, string, nltk, gspread
from sklearn.feature_extraction.text import TfidfVectorizer
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

def lambda_handler(event, context):
    # Initialize Google Sheets client
    gc = gspread.service_account(filename='google_service_account_credentials.json')
    gsheet = gc.open("Website Analytics").sheet1
    
    # Read data from Google Sheet
    df = read_data_from_google_sheet(gsheet)
    
    # Extract the 'Body' column for NLP processing
    df['punctuation_percentage'] = df['Body'].apply(punctuation_percentage)
    df['Body'] = df['Body'].apply(preprocess_text)
    
    # Perform train-test split
    X_train, X_test, y_train, y_test = train_test_split(df[['Body', 'punctuation_percentage']], df['Subject'], test_size=0.2)
    
    # Save the first 10 lines of training data to CSV
    csv_content = X_train.head(10).to_csv(index=False)
    
    # Instead of saving to S3, just return CSV content as part of the Lambda response
    # return {
    #     'statusCode': 200,
    #     'body': csv_content
    # }
