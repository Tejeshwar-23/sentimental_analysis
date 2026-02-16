async function analyzeSentiment() {
    const textarea = document.getElementById("userText");
    const text = textarea.value.trim();
    const analyzeBtn = document.getElementById("analyzeBtn");
    const btnText = analyzeBtn.querySelector(".btn-text");
    const loadingSpinner = analyzeBtn.querySelector(".loading-spinner");

    const resultContainer = document.getElementById("resultContainer");
    const resultText = document.getElementById("resultText");
    const resultIcon = document.getElementById("resultIcon");
    const barFill = document.getElementById("barFill");

    if (!text) {
        showErrorToast("Please enter some text to analyze.");
        return;
    }

    // Set Loading State
    analyzeBtn.disabled = true;
    btnText.innerText = "Analyzing...";
    loadingSpinner.classList.remove("hidden");
    resultContainer.classList.add("hidden");
    barFill.style.width = "0%";

    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: text })
        });

        if (!response.ok) throw new Error('API request failed');

        const data = await response.json();
        const prediction = data.prediction;

        // Reset Button
        analyzeBtn.disabled = false;
        btnText.innerText = "Analyze Now";
        loadingSpinner.classList.add("hidden");

        // Display Result
        resultContainer.classList.remove("hidden");
        resultText.innerText = prediction;

        // Remove existing theme classes
        resultContainer.classList.remove("theme-depressive", "theme-non-depressive");

        if (prediction.toLowerCase().includes("depressive") && !prediction.toLowerCase().includes("non")) {
            resultContainer.classList.add("theme-depressive");
            resultIcon.innerHTML = '<i class="fas fa-cloud-rain"></i>';
            barFill.style.backgroundColor = getComputedStyle(document.documentElement).getPropertyValue('--error');
        } else {
            resultContainer.classList.add("theme-non-depressive");
            resultIcon.innerHTML = '<i class="fas fa-sun"></i>';
            barFill.style.backgroundColor = getComputedStyle(document.documentElement).getPropertyValue('--success');
        }

        // Animate Bar (Simulated confidence for visual effect as model doesn't return it yet)
        setTimeout(() => {
            barFill.style.width = "100%";
        }, 50);

    } catch (error) {
        console.error('Error:', error);
        analyzeBtn.disabled = false;
        btnText.innerText = "Analyze Now";
        loadingSpinner.classList.add("hidden");

        resultContainer.classList.remove("hidden");
        resultContainer.classList.remove("theme-depressive", "theme-non-depressive");
        resultText.innerText = "Backend Connection Error";
        resultIcon.innerHTML = '<i class="fas fa-exclamation-triangle"></i>';
        barFill.style.width = "0%";
    }
}

function showErrorToast(msg) {
    // Simple alert for now, but can be improved with a custom toast
    alert(msg);
}
