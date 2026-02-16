import pandas as pd
import re
import string
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import os

# Define paths
base_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(base_dir, '..', '..', 'sentiment_cleaned.csv')
model_path = os.path.join(base_dir, 'sentiment_svm_model.pkl')
vectorizer_path = os.path.join(base_dir, 'tfidf_vectorizer.pkl')

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.strip()
    return text

print("Loading dataset...")
df = pd.read_csv(dataset_path)

# Use the pre-cleaned or raw text column as per the notebook logic
# Notebook renaming: 'message to examine' -> 'text', 'label (depression result)' -> 'label'
# My CSV check showed: text,label,clean_text,label_encoded
X = df['text'].fillna('')
y = df['label']

print("Pre-processing text...")
X_cleaned = X.apply(clean_text)

print("Vectorizing data...")
# Using parameters observed in the notebook (max_features=5000, stop_words='english')
tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
X_tfidf = tfidf.fit_transform(X_cleaned)

print("Training LinearSVC model...")
# Using class_weight='balanced' as seen in the notebook
model = LinearSVC(class_weight='balanced', dual=False)
model.fit(X_tfidf, y)

print(f"Saving model to {model_path}...")
joblib.dump(model, model_path)

print(f"Saving vectorizer to {vectorizer_path}...")
joblib.dump(tfidf, vectorizer_path)

print("Done! Model and vectorizer are ready.")
