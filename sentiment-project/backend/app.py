# ================================
# Sentiment Analysis Flask Backend
# ================================

from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import re
import string

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load trained model and vectorizer
model = joblib.load('sentiment_svm_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Text cleaning function (must match training preprocessing)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.strip()
    return text

@app.route('/')
def home():
    return "Sentiment Analysis API is running! Use the /predict endpoint with a POST request to get predictions."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    user_text = data['text']

    cleaned = clean_text(user_text)
    vectorized = vectorizer.transform([cleaned])
    
    # Use decision_function for calibrated thresholding
    # Values > -0.9 are considered depressive (calibrated for sensitivity)
    decision_score = model.decision_function(vectorized)[0]
    
    if decision_score > -0.9:
        prediction_label = "Depressive Sentiment"
    else:
        prediction_label = "Non-Depressive Sentiment"
        
    print(f"Text: {user_text[:50]}... | Score: {decision_score} | Prediction: {prediction_label}")
    
    return jsonify({
        'prediction': prediction_label,
        'confidence_score': decision_score # Optional: could be used by frontend
    })

if __name__ == '__main__':
    app.run(debug=True)
