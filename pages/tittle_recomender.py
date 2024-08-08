import streamlit as st
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import pickle

# Load the dataset
def load_data():
    # Ensure the correct path and file name
    anime_df = pd.read_csv('C:/Users/samuk/Desktop/Team-EG4_Streamlit/anime.csv', encoding='latin1')
    return anime_df

# Load datasets
anime_df = load_data()

# Preprocess anime titles
def preprocess_title(title):
    return re.sub(r'[^\w\s]', '', title).lower()

# Create anime_ID and title DataFrame
anime_title_ID = anime_df.copy()
anime_title_ID['name'] = anime_title_ID['name'].apply(preprocess_title)
anime_title_ID.drop(['episodes', 'rating', 'members', 'genre', 'type', 'anime_id'], axis=1, inplace=True)

# Initialize TF-IDF Vectorizer and compute cosine similarity matrix
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(anime_title_ID['name'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend_anime_by_name(title, top_n=10):
    title = preprocess_title(title)
    
    # Check if the title exists
    if title not in anime_title_ID['name'].values:
        return pd.DataFrame({'name': ['Anime not found. Please try another title.']})
    
    # Get the index of the given title
    idx = anime_title_ID.index[anime_title_ID['name'] == title][0]
    
    # Get the pairwise similarity scores of all titles with the given title
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort the titles based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the indices of the most similar titles
    sim_scores = sim_scores[1:(top_n+1)]
    anime_indices = [i[0] for i in sim_scores]
    
    # Return the titles of the most similar titles
    return anime_title_ID.iloc[anime_indices]

def app():  # Ensure this function is named 'app'
    st.markdown("""
    <style>
        .main {
            background-color: #f0f0f0;
            padding: 20px;
        }
        .title {
            font-size: 2em;
            font-weight: bold;
            color: #333;
            text-align: center;
            margin-top: 20px;
        }
        .subheader {
            font-size: 1.5em;
            color: #666;
            text-align: center;
            margin-top: 10px;
        }
        .recommendations {
            margin-top: 20px;
            padding: 10px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">Anime Recommender System</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Find your next favorite anime based on a title!</div>', unsafe_allow_html=True)

    title = st.text_input('Enter the title of an anime you like:', '')

    if title:
        recommendations = recommend_anime_by_name(title)
        if 'Anime not found' in recommendations['name'].values:
            st.markdown(f'<div class="recommendations">{recommendations.iloc[0, 0]}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="recommendations"><h3>Recommended Anime:</h3></div>', unsafe_allow_html=True)
            for anime in recommendations['name']:
                st.markdown(f'<div class="recommendations">{anime}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="recommendations">Please enter an anime title to get recommendations.</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
