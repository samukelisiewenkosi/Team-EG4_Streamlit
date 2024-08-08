import streamlit as st
import os
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Import pages

from pages import user_guide ,genre_recomender ,tittle_recomender,top_rated_anime ,EDA ,Teams ,FAQs

# Define the main app function
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ['Home', 'user_guide',  'genre_recomender', 'tittle_recomender', 'top_rated_anime', 'EDA', 'Teams', 'FAQs'])

    if page == "Home":
        home()
    elif page == "user_guide":
        user_guide.app()
    
    elif page == "EDA":
        EDA.app()
    elif page == "FAQs":
        FAQs.app()
    elif page == "Teams":
        Teams.app()
    elif page == "tittle_recomender":
        tittle_recomender.app()
    elif page == "genre_recomender":
        genre_recomender.app()
    elif page == "top_rated_anime":
        top_rated_anime.app()

def home():
    # Custom CSS for styling
    st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;  /* Light grey background */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .header {
            font-size: 36px;
            font-weight: bold;
            color: #FF6347;  /* Tomato color */
            text-align: center;
            margin-bottom: 20px;
        }
        .description {
            font-size: 18px;
            color: #4682B4;  /* Steel blue color */
            text-align: center;
            margin-bottom: 20px;
        }
        .video {
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            width: 100%;
            max-width: 800px;
            margin: 0 auto 20px;
        }
        .feature-list {
            font-size: 16px;
            color: #333;
            list-style-type: none;
            padding: 0;
            text-align: center;
        }
        .feature-list li {
            margin-bottom: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<p class="header">Welcome to the Anime Recommender System</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <p class="description">
    In today’s technology-driven world, recommender systems are socially and economically critical for ensuring that individuals can make appropriate choices surrounding the content they engage with on a daily basis. One application where this is especially true surrounds movie content recommendations; where intelligent algorithms can help viewers find great titles from tens of thousands of options.
    </p>
    """, unsafe_allow_html=True)

    # Add a new video from YouTube
    st.markdown("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/ZrpEIw8IWwk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen class="video"></iframe>
    """, unsafe_allow_html=True)

    st.markdown("""
    <ul class="feature-list">
    <li><strong>Recommendation:</strong> Get personalized anime recommendations.</li>
    <li><strong>Anime Classifier:</strong> Input anime details to classify and predict its rating.</li>
    <li><strong>FAQs:</strong> Find answers to common questions and ask new ones.</li>
    <li><strong>Contact_info:</strong> Provide your feedback and get in touch with us at EG4 Studios.</li>
    <li><strong>Trailers:</strong> Watch trailers of popular and upcoming anime titles.</li>
    <li><strong>User_guide:</strong> Learn how to use the app and understand its features.</li>
    </ul>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Run the main app function
if __name__ == "__main__":
    main()
