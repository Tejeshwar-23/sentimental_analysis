# Sentiment Analysis System

A simple web application to predict whether a given text conveys "Depressive" or "Non-Depressive" sentiment using a Support Vector Machine (SVM) model.

## Project Structure

```text
sentiment-project/
├── backend/
│   ├── app.py                  # Flask REST API
│   ├── sentiment_svm_model.pkl   # Trained SVM Model
│   ├── tfidf_vectorizer.pkl      # TF-IDF Vectorizer
│   └── requirements.txt        # Backend dependencies
└── frontend/
    ├── index.html              # Main user interface
    ├── style.css               # Modern UI styling
    └── script.js               # Frontend logic and API calls
```

## Setup Instructions

### Step 1: Backend Setup

1. Open your terminal and navigate to the `backend` directory:
   ```powershell
   cd sentiment-project/backend
   ```
2. Install the required dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Run the Flask server:
   ```powershell
   python app.py
   ```
   The backend should now be running at `http://127.0.0.1:5000`.

### Step 2: Frontend Setup

1. Open the `sentiment-project/frontend/index.html` file in any modern web browser.
2. Type the text you want to analyze in the textarea.
3. Click the **Analyze Sentiment** button to see the prediction.

## Technologies Used

- **Backend**: Python, Flask, Scikit-learn, Joblib
- **Frontend**: HTML5, CSS3 (Modern UI), JavaScript (ES6+ Fetch API)
- **Model**: Support Vector Machine (SVM) with TF-IDF Vectorization
