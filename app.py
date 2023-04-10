import openai
import pandas as pd
import spacy
from flask import Flask, render_template, request
import spacy.cli
from subprocess import run
from conversation_history import conversation_history

spacy.cli.download("en_core_web_sm")

p = run(["python", "-m", "spacy", "download", "en_core_web_sm"], capture_output=True)
print("Installation:", p)

# Load the spaCy pre-trained model for English language
nlp = spacy.load('en_core_web_sm')

# Load the embeddings file
df = pd.read_csv("embeddings.csv")

# Set the OpenAI API key
openai.api_key = "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"

# Define the function to generate embeddings for given text
def generate_embedding(text):
    tokens = [token for token in nlp(text) if not token.is_stop and token.is_alpha]
    lemmas = [token.lemma_ for token in tokens]
    embedding = []
    for lemma in lemmas:
        try:
            row = df[df['sentence'] == lemma].iloc[0].tolist()[1:]
            embedding.extend(row)
        except IndexError:
            continue
    return embedding

# Define a function to search for an answer in the embeddings file
def get_answer_from_embeddings(input):
    input_embedding = generate_embedding(input)

    if len(input_embedding) > 0:
        similarity_scores = []
        for i, row in df.iterrows():
            score = 0
            for j, val in enumerate(input_embedding):
                score += (row[j+1] - val)**2
            similarity_scores.append(score)
        similarity_scores.remove(0.0)
        closest_row = df.loc[similarity_scores.index(min(similarity_scores))]

        return closest_row['sentence']
    else:
        conversation_history_dict = dict(conversation_history)
        conversation_history_dict.update({"role": "user", "content": input})

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history_dict,
            temperature=0.85,
            max_tokens=1000,
            n=1,
            stop=None,
            presence_penalty=0.6,
            frequency_penalty=0.6,
        )
        response = completion["choices"][0]['message']['content']
        conversation_history_dict.update({"role": "assistant", "content": response})
        return response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    botinput = None
    reply = None

    if request.method == "POST":
        botinput = request.form.get("botinput")
        print(botinput)
        reply = get_answer_from_embeddings(botinput)

    return render_template(
        "index.html",
        reply=reply,
        botinput=botinput)

if __name__ == "__main__":
    app.run(debug=True)
