document.getElementById('chatForm').addEventListener("DOMContentLoaded", function(event) {
    event.preventDefault();

    const chatForm = document.querySelector("form");
    const chatHistory = document.querySelector(".chat-history");
    const botinput = document.querySelector("#question");
    const chatMessages = document.getElementById('chatMessages');

    const appendMessage = (className, text) => {
        chatMessages.classList.add("chat-message", className);
        const messageText = document.createElement("p");
        messageText.textContent = text;
        chatMessages.appendChild(messageText);
        chatHistory.appendChild(chatMessages);
        chatHistory.scrollTop = chatHistory.scrollHeight;
    };

    chatForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        let question = botinput.value.trim();

        if (!question) {
            botinput.value = ""; // Clear the input field if the message is empty
            return;
        }

        // Sanitize user input
        question = DOMPurify.sanitize(question);

        appendMessage("question", question);
        botinput.value = "";

        try {
            const response = await fetch("/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ question }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok.');
            }

            const { answer } = await response.json();
            appendMessage("answer", answer);
        } catch (error) {
            console.error('There has been a problem with your fetch operation:', error);
            appendMessage("error", 'Error: Unable to get the answer. Please try again later.');
        }
    });

        chatMessages.scrollTop = chatMessages.scrollHeight;

        chatInput.value = '';
});
