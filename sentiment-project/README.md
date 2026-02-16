# Sentiment Analysis System

This project is a sentiment analysis tool that uses a Support Vector Machine (SVM) model to classify text as either "Depressive Sentiment" or "Non-Depressive Sentiment".

## Project Structure

```text
backend/
├── app.py                   # Flask server
├── sentiment_svm_model.pkl  # Trained SVM model
├── tfidf_vectorizer.pkl     # TF-IDF Vectorizer
└── requirements.txt         # Dependencies

frontend/
├── index.html               # Main UI
├── style.css                # Styling
└── script.js                # Frontend logic
```

## How To Run

### Step 1: Install Dependencies
Navigate to the `backend` folder and install the required Python packages:

```bash
cd backend
pip install -r requirements.txt
```

### Step 2: Run the Backend
Start the Flask server:

```bash
python app.py
```

You should see an output indicating the server is running:
`Running on http://127.0.0.1:5000`

### Step 3: Open the Frontend
Open `frontend/index.html` in your web browser.

1. Type your text in the text area.
2. Click the **Analyze** button.
3. The system will process the text using the SVM model and display the result.
