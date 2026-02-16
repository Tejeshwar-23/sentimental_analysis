document.addEventListener('DOMContentLoaded', () => {
    const textInput = document.getElementById('text-input');
    const analyzeBtn = document.getElementById('analyze-btn');
    const resultContainer = document.getElementById('result-container');
    const predictionText = document.getElementById('prediction-text');
    const loader = document.getElementById('loader');
    const btnText = analyzeBtn.querySelector('span');

    const API_URL = 'http://127.0.0.1:5000/predict';

    analyzeBtn.addEventListener('click', async () => {
        const text = textInput.value.trim();

        if (!text) {
            alert('Please enter some text to analyze.');
            return;
        }

        // UI State: Loading
        setLoading(true);
        resultContainer.classList.add('hidden');

        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text })
            });

            if (!response.ok) {
                throw new Error('Analysis failed. Please try again.');
            }

            const data = await response.json();
            displayResult(data.prediction);

        } catch (error) {
            console.error('Error:', error);
            alert(error.message);
        } finally {
            setLoading(false);
        }
    });

    function setLoading(isLoading) {
        if (isLoading) {
            analyzeBtn.disabled = true;
            loader.style.display = 'block';
            btnText.textContent = 'Analyzing...';
        } else {
            analyzeBtn.disabled = false;
            loader.style.display = 'none';
            btnText.textContent = 'Analyze Sentiment';
        }
    }

    function displayResult(prediction) {
        predictionText.textContent = prediction;

        // Remove old classes
        predictionText.classList.remove('depressive', 'non-depressive');

        // Add class based on prediction
        if (prediction === 'Depressive Sentiment') {
            predictionText.classList.add('depressive');
        } else {
            predictionText.classList.add('non-depressive');
        }

        resultContainer.classList.remove('hidden');
    }
});
