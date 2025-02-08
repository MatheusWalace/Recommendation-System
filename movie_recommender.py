import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("movies.csv")

vectorizer = TfidfVectorizer(stop_words='english')
genres_matrix = vectorizer.fit_transform(df['genres'].fillna(''))

df['rating'] = df['rating'] / df['rating'].max()

similarity_matrix = cosine_similarity(genres_matrix)

def recomendar_filmes(titulo, df, similarity_matrix):
    if titulo not in df['title'].values:
        return "Filme não encontrado."

    idx = df[df['title'] == titulo].index[0]

    similar_filmes = list(enumerate(similarity_matrix[idx]))

    similar_filmes = sorted(similar_filmes, key=lambda x: x[1], reverse=True)

    filmes_recomendados = [df.iloc[i[0]]['title'] for i in similar_filmes[1:6]]

    return filmes_recomendados

titulo_filme = "The Matrix"
print(f"Filmes recomendados para '{titulo_filme}':")
print(recomendar_filmes(titulo_filme, df, similarity_matrix))
