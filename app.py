import openai
import pandas as pd
import spacy
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import spacy.cli
from subprocess import run
from conversation_history import conversation_history
import os
import streamlit as st

# api_key = os.environ['API_KEY']
api_key = "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"

spacy.cli.download("en_core_web_sm")

p = run(["python", "-m", "spacy", "download", "en_core_web_sm"], capture_output=True)
print("Installation:", p)

# Load the spaCy pre-trained model for English language
nlp = spacy.load('en_core_web_sm')

# Load the embeddings file
df = pd.read_csv("embeddings.csv")

# Set the OpenAI API key
openai.api_key = api_key

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
        conversation_history.append({"role": "user", "content": input})

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            temperature=0.85,
            max_tokens=1000,
            n=1,
            stop=None,
            presence_penalty=0.6,
            frequency_penalty=0.6,
        )
        response = completion["choices"][0]['message']['content']
        conversation_history.append({"role": "assistant", "content": response})
        return response

app = Flask(__name__)
csrf = CSRFProtect(app)
class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        flash(f"Hello, {form.name.data}!")
        return redirect(url_for('form'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=5005, threaded=False)