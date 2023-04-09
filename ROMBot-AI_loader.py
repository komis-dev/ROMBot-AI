import random
import spacy

# load the English language model for NLP
nlp = spacy.load("en_core_web_sm")

# Define the responses dictionary
responses = {
    "hi": ["Hello!", "Hi there!", "Hey! How can I help you today?"],
    "how are you": ["I'm doing well, thank you. What about you?", "Not bad. How about you?", "Can't complain. What's on your mind today?"],
    "what's up": ["Nothing much, how about you?", "Just chillin'. What's on your mind today?", "Not too much. How can I help you today?"],
    "goodbye": ["Goodbye!", "See you later!", "Bye! Have a great day ahead."],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"]
}

# Define the get_response() function
def get_response(input_text):
    # Convert input text to lowercase and remove punctuation
    input_text = input_text.lower().strip('.,?!')

    # Use NLP to identify named entities in user input
    doc = nlp(input_text)
    entities = [ent.text for ent in doc.ents]

    # Check for keywords in input text
    for keyword in responses:
        if keyword in input_text or keyword in entities:
            return random.choice(responses[keyword])

    # Use sentiment analysis to detect negative emotions
    sentiment = doc.sentiment.polarity
    if sentiment < -0.5:
        return "I'm sorry to hear that. Is there anything I can do to help?"

    # If no keyword matches, return a default response
    return random.choice(responses["default"])

# Define the run_bot() function
def run_bot():
    print("Welcome to the chatbot!")
    print("Type 'goodbye' to exit\n")
    while True:
        user_input = input("You: ")
        if user_input == "goodbye":
            print("Chatbot: " + random.choice(responses["goodbye"]))
            break
        else:
            response = get_response(user_input)
            print("Chatbot: " + response)

# Call the run_bot() function
run_bot()
