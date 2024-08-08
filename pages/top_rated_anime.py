import streamlit as st
import pandas as pd
import os
import pickle

# Load the pickled files
anime_data = pd.read_pickle('C:/Users/samuk/Desktop/Team-EG4_Streamlit/anime_data.pkl')
ratings_data = pd.read_pickle('C:/Users/samuk/Desktop/Team-EG4_Streamlit/ratings_data.pkl')

def recommend_anime_by_rating(top_n=40):  # Changed to top 30
    # Calculate average rating for each anime
    avg_ratings = ratings_data.groupby('anime_id')['rating'].mean().reset_index()
    avg_ratings.columns = ['anime_id', 'average_rating']
    
    # Merge with anime data to get titles and other details
    merged_data = pd.merge(anime_data, avg_ratings, on='anime_id')
    
    # Sort by average rating and get top_n recommendations
    top_anime = merged_data.sort_values(by='average_rating', ascending=False).head(top_n)
    return top_anime

def app():  # Ensure this function is named 'app'
    st.markdown("""
    <style>
        .main {
            background-color: #e0f7fa;
            padding: 20px;
        }
        .title {
            font-size: 2em;
            font-weight: bold;
            color: #00796b;
            text-align: center;
            margin-top: 20px;
        }
        .subheader {
            font-size: 1.5em;
            color: #004d40;
            text-align: center;
            margin-top: 10px;
        }
        .recommendations {
            margin-top: 20px;
            padding: 10px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">Top Rated Anime Recommender System</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Discover highly rated anime based on average ratings!</div>', unsafe_allow_html=True)

    recommendations = recommend_anime_by_rating()  # No need to pass top_n as we set default to 30
    st.markdown('<div class="recommendations"><h3>Top Rated Anime:</h3></div>', unsafe_allow_html=True)
    for _, row in recommendations.iterrows():
        st.markdown(f'<div class="recommendations">{row["name"]} (Rating: {row["average_rating"]:.2f})</div>', unsafe_allow_html=True)

# Call the app function to run the Streamlit app
if __name__ == '__main__':
    app()
