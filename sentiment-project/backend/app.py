# ================================
# Sentiment Analysis Flask Backend
# ================================

from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import re
import string
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend interaction

# Define paths
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'sentiment_svm_model.pkl')
vectorizer_path = os.path.join(base_dir, 'tfidf_vectorizer.pkl')

# Load trained model and vectorizer
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# Text cleaning function (must match training preprocessing)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.strip()
    return text

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    user_text = data.get('text', '')
    
    if not user_text:
        return jsonify({"error": "No text provided"}), 400

    cleaned = clean_text(user_text)
    vectorized = vectorizer.transform([cleaned])

    # Use decision_function for calibrated thresholding as per project notebook
    decision_score = model.decision_function(vectorized)[0]
    
    # Calibrated threshold for better sensitivity (found in original project files)
    if decision_score > -0.9:
        result = "Depressive Sentiment"
    else:
        result = "Non-Depressive Sentiment"

    return jsonify({
        "prediction": result,
        "confidence_score": float(decision_score)
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)
