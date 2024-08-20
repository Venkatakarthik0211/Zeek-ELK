# Natural Language Processing

## Steps Involved in NLP

1. **Text Preprocessing**:
    - **Tokenization**: Splitting the text into words or sentences.
    - **Lowercasing**: Converting all text to lowercase to ensure uniformity.
    - **Remove Punctuation**: Eliminating punctuation marks to clean the text.
    - **Stop Words Removal**: Removing common words (e.g., "and", "the") that do not contribute much meaning.
    - **Stemming/Lemmatization**: Reducing words to their root form.

2. **Feature Extraction**:
    - **Bag of Words (BoW)**: Representing text as a collection of its words, disregarding grammar and word order.
    - **Term Frequency-Inverse Document Frequency (TF-IDF)**: Evaluating the importance of a word in a document relative to a collection of documents.
    - **Word Embeddings**: Representing words in continuous vector space (e.g., Word2Vec, GloVe).

3. **Model Building**:
    - **Choosing an Algorithm**: Selecting a machine learning or deep learning model (e.g., Naive Bayes, SVM, LSTM).
    - **Training the Model**: Using the training data to let the model learn the patterns.
    - **Evaluation**: Assessing the model's performance using metrics like accuracy, precision, recall, and F1-score.

4. **Post-Processing**:
    - **Interpretation of Results**: Understanding and interpreting the model's predictions.
    - **Fine-Tuning**: Adjusting parameters and re-training the model for better performance.

## Stemming

Stemming is the process of reducing words to their base or root form. This helps in handling different forms of the same word during text analysis. 

### Types of Stemming

1. **Porter Stemmer**:
    - One of the most widely used stemming algorithms.
    - It applies a set of rules to iteratively trim suffixes.

```python
def stem_text(tokenized_text):
    text = [ps.stem(word) for word in tokenized_text]
    return text
```

2. **Lancaster Stemmer**:
    - A more aggressive stemming algorithm compared to Porter Stemmer.
    - Often produces shorter stems.
    - Process of grouping together the inflected forms of a word so they can be analyzed as a **Single Term**
    - **Computationally Expensive**

```python
def lemmatize_text(tokenized_text):
    text = [lem.lemmatize(word) for word in tokenized_text]
    return text
```

3. **Snowball Stemmer**:
    - An improved version of Porter Stemmer.
    - Supports multiple languages.

## Packages and In-Built Functions Used in NLP

1. **NLTK (Natural Language Toolkit)**:
    - `nltk.tokenize`: Functions for tokenizing text.
    - `nltk.corpus`: Access to various text corpora and lexical resources.
    - `nltk.stem`: Contains stemming algorithms like PorterStemmer and LancasterStemmer.

2. **spaCy**:
    - `spacy.load()`: Loads a pre-trained language model.
    - `spacy.tokenizer`: Tokenizes text into words, punctuation, etc.
    - `spacy.lemmatizer`: Lemmatizes words to their root form.

3. **TextBlob**:
    - `TextBlob(text)`: Creates a TextBlob object for the given text.
    - `blob.sentiment`: Analyzes the sentiment of the text.
    - `blob.words`: Tokenizes the text into words.

4. **Gensim**:
    - `gensim.models.Word2Vec`: Creates and trains a Word2Vec model.
    - `gensim.corpora.Dictionary`: Creates a dictionary from a corpus.

5. **scikit-learn**:
    - `sklearn.feature_extraction.text.CountVectorizer`: Converts a collection of text documents to a matrix of token counts.
    - `sklearn.feature_extraction.text.TfidfVectorizer`: Converts a collection of raw documents to a matrix of TF-IDF features.
    - `sklearn.naive_bayes.MultinomialNB`: Implements the Naive Bayes classifier for multinomially distributed data.

## Vectorization in NLP

Vectorization is the process of converting text data into numerical vectors that can be used by machine learning algorithms. This step is crucial because machine learning models require numerical input to perform computations.

### Types of Vectorization

1. **Bag of Words (BoW)**
    - **Description**: Represents text as a set of word frequencies. Each word in the text is treated as a feature, and the value is the count of that word in the document.
    - **Advantages**: Simple to implement and understand.
    - **Disadvantages**: Ignores the order of words and context. Can result in large sparse matrices for large vocabularies.
    - **Example**: 
        ```
        Document 1: "I love machine learning"
        Document 2: "Machine learning is fun"
        
        Vocabulary: ["I", "love", "machine", "learning", "is", "fun"]
        
        Document 1 Vector: [1, 1, 1, 1, 0, 0]
        Document 2 Vector: [0, 0, 1, 1, 1, 1]
        ```

2. **TF-IDF (Term Frequency-Inverse Document Frequency)**
    - **Description**: Reflects the importance of a term in a document relative to a collection of documents. Combines term frequency (TF) with inverse document frequency (IDF).
    - **Advantages**: Provides a more informative representation by considering the relative importance of words.
    - **Disadvantages**: Still ignores the order of words and context.
    - **Formula**: 
        ```
        TF = (Number of times term t appears in a document) / (Total number of terms in the document)
        IDF = log(Total number of documents / Number of documents with term t in it)
        
        TF-IDF = TF * IDF
        ```
    ## TF-IDF Calculation

    TF-IDF (Term Frequency-Inverse Document Frequency) is a numerical statistic that reflects the importance of a term in a document relative to a collection of documents. It combines the term's frequency in the document (TF) with its rarity across the entire collection (IDF).

    Here's an example of how to calculate TF-IDF:

    ```plaintext
    1. Term Frequency (TF):
        Given a text message: "I like NLP"
        Calculate the frequency of the term "NLP" in the message:
        tf_NLP = (number of occurrences of NLP in text message) / (total words in text message) = 1 / 3 = 0.33

    2. Document Frequency (DF):
        Assume there are 20 documents in our collection.
        The term "NLP" appears in 1 document.
        df_NLP = 1

    3. Inverse Document Frequency (IDF):
        Use the formula: w_ij = tf_ij * log(N / df_i)
        Substituting values:
        w_NLP = 0.33 * log(20 / 1) = 0.33 * 1.301 = 0.43

    4. Final Value:
        The TF-IDF weight for the term "NLP" in this document is approximately 0.43.
    ```

    TF-IDF helps evaluate how important a word is to a document within a collection or corpus. It considers both the term's frequency in the document (TF) and its rarity across the entire collection (IDF).

    By calculating TF-IDF, we can identify the most significant terms in a document and use them for various natural language processing tasks, such as information retrieval, text classification, and sentiment analysis.

```python
# Initialize TF-IDF Vectorizer
tfidf_vect = TfidfVectorizer()
X_counts = tfidf_vect.fit_transform(df['text'])

# Output shape of the TF-IDF matrix
print(X_counts.shape)
```


3. **Word Embeddings**
    - **Description**: Represents words in a dense vector space where semantically similar words are close to each other. Pre-trained models like Word2Vec, GloVe, and FastText are commonly used.
    - **Advantages**: Captures semantic meaning and context of words. Reduces dimensionality compared to BoW and TF-IDF.
    - **Disadvantages**: Requires large amounts of data and computational power to train.
    - **Example**: In Word2Vec, the words "king" and "queen" might have similar vectors because they share similar contexts.

4. **Sentence Embeddings**
    - **Description**: Extends word embeddings to entire sentences or documents, capturing the meaning of the entire text. Models like Universal Sentence Encoder (USE) and BERT are used.
    - **Advantages**: Captures contextual and semantic meaning of entire sentences.
    - **Disadvantages**: Computationally intensive to train and require large datasets.
    - **Example**: BERT (Bidirectional Encoder Representations from Transformers) can generate embeddings for sentences that understand context in both directions.

5. **Count Vectorization**
    - **Description**: Similar to BoW, but represents the text as the count of each word in the document. Each document is represented as a vector of the counts of each word.
    - **Advantages**: Simple and easy to implement.
    - **Disadvantages**: Can lead to high-dimensional sparse matrices.
    - **Example**:
        ```
        Document 1: "I love machine learning"
        Document 2: "Machine learning is fun"
        
        Vocabulary: ["I", "love", "machine", "learning", "is", "fun"]
        
        Document 1 Vector: [1, 1, 1, 1, 0, 0]
        Document 2 Vector: [0, 0, 1, 1, 1, 1]
        ```

6. **Hashing Vectorization**
    - **Description**: Uses a hash function to convert words into vectors of fixed size. This method is particularly useful for large datasets.
    - **Advantages**: Handles large vocabularies efficiently and reduces memory usage.
    - **Disadvantages**: Potential for hash collisions, where different words are mapped to the same vector.
    - **Example**: Words are mapped to indices in a fixed-size array using a hash function.


# Cross-Validation Techniques in Machine Learning

Cross-validation is a statistical method used to estimate the skill of machine learning models. It is primarily used in applied machine learning to estimate the performance of a model on unseen data.

## 1. K-Fold Cross-Validation

In K-Fold Cross-Validation, the dataset is divided into `k` subsets, also known as "folds". The model is trained on `k-1` folds and tested on the remaining one fold. This process is repeated `k` times, with each fold serving as the test set exactly once. The final result is the average of the scores from all the folds.

- **Steps**:
  1. Split the data into `k` equal-sized folds.
  2. For each fold:
     - Train the model on the remaining `k-1` folds.
     - Test the model on the current fold.
  3. Calculate the average performance across all `k` folds.

- **Diagram**:

    ```plaintext
    Data: [D1, D2, D3, D4, D5]

    Fold 1: Train on [D2, D3, D4, D5], Test on [D1]
    Fold 2: Train on [D1, D3, D4, D5], Test on [D2]
    Fold 3: Train on [D1, D2, D4, D5], Test on [D3]
    Fold 4: Train on [D1, D2, D3, D5], Test on [D4]
    Fold 5: Train on [D1, D2, D3, D4], Test on [D5]
    ```

## 2. Leave-One-Out Cross-Validation (LOOCV)

LOOCV is a special case of K-Fold Cross-Validation where `k` equals the number of data points in the dataset. In each iteration, the model is trained on all data points except one, which is used as the test set.

- **Steps**:
  1. For each data point:
     - Train the model on all other data points.
     - Test the model on the current data point.
  2. Calculate the average performance.

- **Diagram**:

    ```plaintext
    Data: [D1, D2, D3, D4, D5]

    Iteration 1: Train on [D2, D3, D4, D5], Test on [D1]
    Iteration 2: Train on [D1, D3, D4, D5], Test on [D2]
    Iteration 3: Train on [D1, D2, D4, D5], Test on [D3]
    Iteration 4: Train on [D1, D2, D3, D5], Test on [D4]
    Iteration 5: Train on [D1, D2, D3, D4], Test on [D5]
    ```

## 3. Stratified K-Fold Cross-Validation

Stratified K-Fold Cross-Validation is an extension of K-Fold Cross-Validation where the folds are selected so that they contain roughly the same proportions of classes as the original dataset. This is particularly useful when dealing with imbalanced datasets.

- **Steps**:
  1. Split the data into `k` equal-sized folds, maintaining the class distribution.
  2. Follow the same procedure as K-Fold Cross-Validation.

# Evaluation Metrics in Machine Learning

Different evaluation metrics are used to assess the performance of machine learning models. These metrics help in comparing models and choosing the best one for the task.

## 1. Accuracy

Accuracy is the ratio of correctly predicted observations to the total observations. It is one of the simplest metrics but can be misleading in cases of imbalanced datasets.

- **Formula**:

    ```plaintext
    Accuracy = (True Positives + True Negatives) / Total Samples
    ```

## 2. Precision

Precision is the ratio of correctly predicted positive observations to the total predicted positive observations. It is useful when the cost of false positives is high.

- **Formula**:

    ```plaintext
    Precision = True Positives / (True Positives + False Positives)
    ```

## 3. Recall (Sensitivity)

Recall is the ratio of correctly predicted positive observations to all observations in the actual class. It is important when the cost of false negatives is high.

- **Formula**:

    ```plaintext
    Recall = True Positives / (True Positives + False Negatives)
    ```

## 4. F1 Score

The F1 Score is the harmonic mean of Precision and Recall. It is a good measure when you need to balance Precision and Recall.

- **Formula**:

    ```plaintext
    F1 Score = 2 * (Precision * Recall) / (Precision + Recall)
    ```

## 5. ROC-AUC (Receiver Operating Characteristic - Area Under Curve)

ROC-AUC is a performance measurement for classification problems at various threshold settings. It represents the degree of separability and tells how much the model is capable of distinguishing between classes.

- **ROC Curve**: Plots the True Positive Rate (Recall) against the False Positive Rate.

# Diagram: Differences Between Evaluation Metrics

```plaintext
           +-----------------------------+-----------------------------+
           |                             |                             |
           |   Predicted Class: Positive |   Predicted Class: Negative |
           |                             |                             |
+----------+-----------------------------+-----------------------------+
|          |                             |                             |
|  Actual  |  True Positive (TP)          |  False Negative (FN)        |
|  Class:  |                             |                             |
| Positive |  Precision = TP / (TP + FP) |  Recall = TP / (TP + FN)    |
|          |                             |                             |
+----------+-----------------------------+-----------------------------+
|          |                             |                             |
|  Actual  |  False Positive (FP)         |  True Negative (TN)         |
|  Class:  |                             |                             |
| Negative |  Accuracy = (TP + TN) /      |                             |
|          |  (TP + TN + FP + FN)         |                             |
+----------+-----------------------------+-----------------------------+

F1 Score balances Precision and Recall by taking the harmonic mean:
F1 Score = 2 * (Precision * Recall) / (Precision + Recall)
