import spacy
import pandas as pd
import openai
import numpy as np
from functools import lru_cache
from multiprocessing import Pool

nlp = spacy.load('en_core_web_sm')

# Load the embeddings file into memory
df = pd.concat([pd.read_csv(filename) for filename in ['embeddings1.csv', 'embeddings2.csv']])
df_dict = df.set_index('sentences').T.to_dict()

# Set the OpenAI API key
openai.api_key = "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"

# Define a function to generate embeddings for given text
@lru_cache(maxsize=None)
def generate_embedding(text):
    tokens = [token for token in nlp(text) if not token.is_stop and token.is_alpha]
    lemmas = [token.lemma_ for token in tokens]
    embedding = []
    for lemma in lemmas:
        if lemma in df_dict:
            embedding.extend(df_dict[lemma].values())
    return np.array(embedding)

# Define a function to search for an answer in the embeddings file
def get_closest_row(args):
    row, input_embedding = args
    score = np.sum(np.square(row - input_embedding))
    return score

def get_answer_from_embeddings(input):
    # Get the embedding vector for the input message
    input_embedding = generate_embedding(input)

    # If embedding is present for the input message, find the most similar message from the embeddings file
    if len(input_embedding) > 0:
        with Pool() as p:
            similarity_scores = p.map(get_closest_row, [(row.values()[1:], input_embedding) for _, row in df_dict.items()])
        closest_row = df.loc[similarity_scores.index(min(similarity_scores))]
        return closest_row['sentence_response']

    # If no matching embedding is found, use OpenAI API to generate response
    else:
        messages = [
            {"id": "1", "text": input},
            {"id": "2", "text": "Hi, how can I help you today?"},
            {"role": "system", "content": "You are a helpful and kind AI Assistant, who is an expert on the ROM Global project."}
        ]
        prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])
        completion = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            temperature=0.85,
            max_tokens=1000,
            n=1,
            stop=None,

            # Set the presence_penalty and frequency_penalty to encourage more diverse responses
            presence_penalty=0.6,
            frequency_penalty=0.6,
        )
        response = completion["choices"][0]["text"]
        return response
