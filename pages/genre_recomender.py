import streamlit as st
import joblib
import pandas as pd
import os
import pickle

# Load the pickled files
vectorizer = joblib.load('C:/Users/samuk/Desktop/Team-EG4_Streamlit/tfidf_vectorizer.pkl')
anime_data = pd.read_pickle('C:/Users/samuk/Desktop/Team-EG4_Streamlit/anime_data.pkl')

def recommend_anime_by_genre(selected_genre, top_n=10):
    # Filter anime based on selected genre
    filtered_anime = anime_data[anime_data['genre'].str.contains(selected_genre, case=False, na=False)]
    
    if filtered_anime.empty:
        return pd.DataFrame({'name': ['No anime found for this genre.']})

    # Convert descriptions to feature vectors
    descriptions = filtered_anime['genre']  # Use genre instead of description
    description_vectors = vectorizer.transform(descriptions)

    # Compute similarity matrix
    similarity_matrix = description_vectors * description_vectors.T
    sim_scores = list(enumerate(similarity_matrix.sum(axis=1).tolist()))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[:top_n]
    anime_indices = [i[0] for i in sim_scores]

    return filtered_anime.iloc[anime_indices]

def app():  # Ensure this function is named 'app'
    st.markdown("""
    <style>
        .main {
            background-color: #f8f8f8;
            padding: 20px;
        }
        .title {
            font-size: 2em;
            font-weight: bold;
            color: #444;
            text-align: center;
            margin-top: 20px;
        }
        .subheader {
            font-size: 1.5em;
            color: #777;
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
        .disclaimer {
            font-size: 0.9em;
            color: #f44;
            text-align: center;
            margin-top: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">Genre-Based Anime Recommender System</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Find anime based on your favorite genre!</div>', unsafe_allow_html=True)

    # List of available genres
    genres = ['Action', 'Adventure', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Mystery', 'Romance', 'Sci-Fi', 'Slice of Life']
    genre = st.selectbox('Select a genre:', genres)

    st.markdown('<div class="disclaimer">Please start the genre name with a capital letter.</div>', unsafe_allow_html=True)

    if genre:
        recommendations = recommend_anime_by_genre(genre)
        if 'No anime found for this genre' in recommendations['name'].values:
            st.markdown(f'<div class="recommendations">{recommendations.iloc[0, 0]}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="recommendations"><h3>Recommended Anime:</h3></div>', unsafe_allow_html=True)
            for _, row in recommendations.iterrows():
                st.markdown(f'<div class="recommendations">{row["name"]} (Rating: {row["rating"]})</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="recommendations">Please select a genre to get recommendations.</div>', unsafe_allow_html=True)