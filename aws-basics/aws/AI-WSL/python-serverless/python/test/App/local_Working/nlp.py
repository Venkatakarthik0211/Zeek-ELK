import sys
import pandas as pd
import re
import string
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

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
    count = sum([1 for char in text if char in string.punctuation])
    return round(count/(len(text) - text.count(' ')), 3) * 100

if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: python3 nlp.py <file_name>")

        file_name = sys.argv[1]

        # Load dataset
        df = pd.read_csv(file_name, sep="\t", header=None, names=['Person', 'text'])

        # Adding a feature - punctuation percentage in the text
        df['punctuation_percentage'] = df['text'].apply(punctuation_percentage)

        # Apply preprocessing
        df['text'] = df['text'].apply(preprocess_text)

        # Split the dataset into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(df[['text', 'punctuation_percentage']], df['Person'], test_size=0.2)

        # Save the first 10 lines of training data to a CSV file
        X_train.head(10).to_csv('training_data.csv', index=False)

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        print("No data found. The file might be empty.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

