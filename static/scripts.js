document.addEventListener("DOMContentLoaded", function () {
    const chatForm = document.querySelector("form");
    const chatHistory = document.querySelector(".chat-history");
    const botinput = document.querySelector("#question");

    const appendMessage = (className, text) => {
        const message = document.createElement("div");
        message.classList.add("chat-message", className);
        const messageText = document.createElement("p");
        messageText.textContent = text;
        message.appendChild(messageText);
        chatHistory.appendChild(message);
        chatHistory.scrollTop = chatHistory.scrollHeight;
    };

    chatForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const question = botinput.value.trim();
        if (!question) {
            botinput.value = ""; // Clear the input field if the message is empty
            return;
        }

        appendMessage("question", question);
        botinput.value = "";

        const response = await fetch("/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ question }),
        });

        const { answer } = await response.json();
        appendMessage("answer", answer);
    });
});
