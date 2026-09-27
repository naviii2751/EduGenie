async function askQuestion() {
    const question = document.getElementById("question").value;
    const answer = document.getElementById("answer");

    if (!question.trim()) {
        answer.innerText = "Please enter a question.";
        return;
    }

    answer.innerText = "Thinking...";

    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: question
            })
        });

        const data = await response.json();
        answer.innerText = data.answer;
    } catch (error) {
        answer.innerText = "Something went wrong.";
    }
}
