async function askQuestion() {
    const question = document.getElementById("question").value;
    const result = document.getElementById("answer");

    result.innerText = "Thinking...";

    const response = await fetch("/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question: question })
    });

    const data = await response.json();
    result.innerText = data.answer;
}


async function explainTopic() {
    const topic = document.getElementById("explainTopic").value;
    const result = document.getElementById("explainResult");

    result.innerText = "Generating explanation...";

    const response = await fetch("/explain", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ topic: topic })
    });

    const data = await response.json();
    result.innerText = data.answer;
}


async function summarizeText() {
    const text = document.getElementById("summaryText").value;
    const result = document.getElementById("summaryResult");

    result.innerText = "Summarizing...";

    const response = await fetch("/summarize", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    });

    const data = await response.json();
    result.innerText = data.answer;
}


async function generateQuiz() {
    const topic = document.getElementById("quizTopic").value;
    const result = document.getElementById("quizResult");

    result.innerText = "Generating quiz...";

    const response = await fetch("/quiz", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ topic: topic })
    });

    const data = await response.json();
    result.innerText = data.answer;
}


async function generateLearningPath() {
    const topic = document.getElementById("learningTopic").value;
    const result = document.getElementById("learningResult");

    result.innerText = "Creating learning path...";

    const response = await fetch("/learning-path", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ topic: topic })
    });

    const data = await response.json();
    result.innerText = data.answer;
}