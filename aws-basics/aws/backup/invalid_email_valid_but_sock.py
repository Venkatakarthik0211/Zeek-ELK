#!/usr/bin/env python
# coding: utf-8

# Install required packages
!pip install py3-validate-email pandas nltk gspread scikit-learn

# Import libraries
import pandas as pd
import re
import string
import nltk
import gspread
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from io import StringIO
from validate_email import validate_email
import dns.resolver

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

def extract_email(email_str):
    """Extract the email address from a string that may contain a name."""
    # Regular expression to match email addresses
    email_regex = r'<([^<>]+)>|([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
    match = re.search(email_regex, email_str)
    if match:
        return match.group(1) or match.group(2)
    return None

def process_emails(df):
    """Process the DataFrame to extract email addresses from the 'Sender' column."""
    # Extract emails from the 'Sender' column
    df['Sender'] = df['Sender'].apply(extract_email)
    return df

# Validation Functions
def check_email_format(email):
    """Check if the email format is valid."""
    return validate_email(email_address=email, check_format=True, check_blacklist=True, check_dns=True, check_smtp=True)

def check_email_domain(email):
    """Check if the domain part of the email is valid."""
    domain = email.split('@')[1]
    return re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', domain)

def has_dns_records(domain):
    """Check if DNS records exist for the domain."""
    try:
        dns.resolver.resolve(domain, 'A')
        return True
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
        return False

def has_mx_record(domain):
    """Check if the domain has MX records."""
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        return bool(answers)
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
        return False

def is_gibberish(email):
    """Check if the email is gibberish."""
    if not email:
        return False
    local_part = email.split('@')[0]
    gibberish_pattern = re.compile(r'^[a-zA-Z0-9._%+-]{8,}$')  # Simplified pattern
    return len(local_part) > 20 or not gibberish_pattern.match(local_part)

def is_spam(email):
    """Check if the email is likely spam based on specific patterns."""
    if not email:
        return False
    local_part = email.split('@')[0]
    spam_patterns = re.compile(r'(do-not-reply|notify|alert|no-reply|noreply)', re.IGNORECASE)
    return bool(spam_patterns.search(local_part))

def validate_email_address(email):
    """Validate the email address step by step and categorize."""
    if not email:
        return "Invalid Email - No Address Provided"

    # First, check basic email validity
    if not check_email_format(email):
        return f"Basic Validations Failed"

    # Then check domain validity
    if not check_email_domain(email):
        return f"Basic Validations Failed"

    domain = email.split('@')[1]

    # Check DNS records
    if not has_dns_records(domain):
        return f"Basic Validations Failed"

    # Check MX records
    if not has_mx_record(domain):
        return f"Basic Validations Failed"

    # Check if the email is likely spam
    if is_spam(email):
        return f"Valid Domains - Likely Notification Email"

    # # Check if the email is gibberish
    # if is_gibberish(email):
    #     return f"Valid Domains - Likely Gibberish: {email}"

    return f"Valid Email - Possibly Personal or Corporate Email"

# Initialize Google Sheets client
gc = gspread.service_account(filename='cred.json')
gsheet = gc.open("Email Data").get_worksheet(1)

# Read data from Google Sheet
df = read_data_from_google_sheet(gsheet)

# Process the DataFrame to extract email addresses
df = process_emails(df)

# Get unique email addresses
unique_emails = df['Sender'].dropna().unique()

# Create a dictionary to store validation results
validation_results = {email: validate_email_address(email) for email in unique_emails}

# Map the validation results back to the DataFrame
df['Sender_Validation'] = df['Sender'].map(validation_results)

# Optionally, you can print the DataFrame to verify the results
print(df[['Sender', 'Sender_Validation']].head())

# df['Sender'].dropna().unique()
# emails = df['Sender'].dropna().unique()  # Ensure no NaN values are processed

# for email in emails:
#     print(validate_email_address(email))

# # NLP processing
# df['punctuation_percentage'] = df['Body'].apply(punctuation_percentage)
# df['Body'] = df['Body'].apply(preprocess_text)
# df['body_length'] = df['Body'].apply(lambda x: len(x) - x.count(' '))

# # Vectorizing the data using TF-IDF
# Tfidf_vect = TfidfVectorizer(analyzer=preprocess_text)
# X_tfidf = Tfidf_vect.fit_transform(df['Body'])

# # Combine the features into a DataFrame
# X_features = pd.concat([df[['punctuation_percentage', 'body_length']], pd.DataFrame(X_tfidf.toarray())], axis=1)
# X_features.columns = X_features.columns.astype(str)