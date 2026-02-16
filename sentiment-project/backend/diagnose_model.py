import joblib
import re
import string

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.strip()
    return text

try:
    model = joblib.load('sentiment_svm_model.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    
    sentences = [
        "I feel so lonely and everything seems so dark today.",
        "I am so happy today, the sun is shining!",
        "Life is wonderful and I love my friends.",
        "I just want to stay in bed all day and cry."
    ]
    
    for test_text in sentences:
        cleaned = clean_text(test_text)
        vectorized = vectorizer.transform([cleaned])
        decision_value = model.decision_function(vectorized)[0]
        prediction = model.predict(vectorized)[0]
        print(f"Text: {test_text}")
        print(f"Decision: {decision_value}, Prediction: {prediction}\n")

except Exception as e:
    print(f"Error: {e}")
