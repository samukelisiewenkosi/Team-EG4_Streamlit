import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import joblib
import os

# Load pickled files for the genre recommender
vectorizer = joblib.load('C:/Users/samuk/Desktop/Team-EG4_Streamlit/tfidf_vectorizer.pkl')
anime_data = pd.read_pickle('C:/Users/samuk/Desktop/Team-EG4_Streamlit/anime_data.pkl')

# Load data for EDA
def load_data():
    train_df = pd.read_csv('train.csv')
    test_df = pd.read_csv('test.csv')
    anime_df = pd.read_csv('anime.csv')
    return train_df, test_df, anime_df

# Home page
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

    # Add a video from YouTube with autoplay enabled
    st.markdown("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/ZrpEIw8IWwk?autoplay=1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen class="video"></iframe>
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

# EDA page
def eda():
    st.markdown("""
    <style>
        .main {
            background-color: #f0f0f0;
            padding: 20px;
            border-radius: 10px;
        }
        .stTitle {
            font-size: 60px;
            color: #333333;
        }
        .stHeader {
            font-size: 48px;
            color: #333333;
        }
        .stSubheader {
            font-size: 36px;
            color: #333333;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main">', unsafe_allow_html=True)

    st.title("Exploratory Data Analysis (EDA)")

    # Check if the image file exists and display it
    if os.path.exists('anim.png'):
        st.image('anim.png', use_column_width=True)
    else:
        st.error("Image file 'anim.png' not found in the directory")

    train_df, test_df, anime_df = load_data()

    st.header("Data Preview")
    st.write("**Train DataFrame:**")
    st.write(train_df.head())
    st.write("**Test DataFrame:**")
    st.write(test_df.head())
    st.write("**Anime DataFrame:**")
    st.write(anime_df.head())

    st.header("Descriptive Statistics")
    st.write(anime_df.describe())
    st.markdown(""" **Interpretation**:
                
    -Count:

    The anime_id and members columns have 12,294 entries, indicating complete data.
    The rating column has 12,064 entries, showing that there are some missing values.
                
    -Mean:

    The average anime_id is 14,058.22, which doesn't have a meaningful interpretation since IDs are arbitrary.
    The average rating is 6.47, suggesting a generally positive reception for most anime.
    The average number of members per anime is 18,017.34, indicating the typical popularity level.
                
    -Standard Deviation:

    The anime_id has a high standard deviation due to the wide range of IDs.
    The rating standard deviation is 1.03, indicating moderate variability in ratings.
    The members standard deviation is quite large (54,820.68), reflecting significant differences in popularity among anime titles.
                
    -Minimum and Maximum:

    The minimum rating is 1.67, and the maximum is 10, showing the full range of possible ratings.
    The number of members ranges from 5 to 1,013,917, highlighting the wide disparity in anime popularity.
                
    -Percentiles:

    The 25th percentile for rating is 5.88, and the 75th percentile is 7.18, indicating that half of the anime titles have ratings within this range.
    Similarly, the number of members shows significant spread, with 25% of anime having fewer than 225 members and 75% having fewer than 9,437 members.
    These descriptive statistics provide a comprehensive overview of the dataset, allowing you to understand the distribution, central tendency, and variability of the key attributes in your anime dataset.
    """)

    st.header("Missing Values")
    st.write(anime_df.isnull().sum())

    st.header("Data Visualization")
    
    # Generate word cloud for genres
    st.subheader("Word Cloud of Genres")
    anime_df_expanded = anime_df.assign(genre=anime_df['genre'].str.split(',')).explode('genre')
    generate_wordcloud(' '.join(anime_df_expanded['genre'].dropna()), 'Word Cloud of Genres')

    st.markdown("""
    **Interpretation:**
    The word cloud indicates the most common genres in our dataset, highlighting that 'Action', 'Sci-Fi', 'Adventure', and 'Comedy' are particularly prevalent. Note the appearance of combinations like 'Action Adventure' and 'Adventure Comedy', which show popular genre pairings.
    """)

    # Total Members by Top 10 Genres
    st.subheader("Total Members by Top 10 Genres")
    genre_total_members = anime_df_expanded.groupby('genre')['members'].sum().reset_index()
    genre_total_members = genre_total_members.sort_values(by='members', ascending=False)
    top_10_genres = genre_total_members.head(10)
    
    plt.figure(figsize=(12, 6))
    bars = plt.bar(top_10_genres['genre'], top_10_genres['members'], color='skyblue')
    plt.xlabel('Top 10 Genres')
    plt.ylabel('Total Members')
    plt.title('Total Members by Top 10 Genres')
    plt.xticks(rotation=45, ha='right')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    st.pyplot(plt)

    st.markdown("""
    **Interpretation:**
    Comedy and Action genres have the highest number of members, suggesting their broad appeal. The top 10 genres reveal a diverse set of interests among the anime community.
    """)

    # Average Rating by Type
    st.subheader("Average Rating by Anime Type")
    type_avg_rating = anime_df.groupby('type')['rating'].mean().sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    bars = plt.bar(type_avg_rating.index, type_avg_rating.values, color='lightgreen')
    plt.xlabel('Anime Type')
    plt.ylabel('Average Rating')
    plt.title('Average Rating by Anime Type')
    plt.xticks(rotation=45, ha='right')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    st.pyplot(plt)

    st.markdown("""
    **Interpretation:**
    The graph shows that TV Series have the highest average ratings among anime types, followed by Movies and OVAs. This may indicate a preference for longer-form storytelling in the anime community.
    """)

    # Average Rating vs. Members
    st.subheader("Average Rating vs. Members")
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x='members', y='rating', data=anime_df, alpha=0.6)
    plt.xlabel('Members')
    plt.ylabel('Rating')
    plt.title('Average Rating vs. Members')

    plt.tight_layout()
    st.pyplot(plt)

    st.markdown("""
    **Interpretation:**
    The scatter plot indicates no strong correlation between the number of members and average rating. Popular anime (those with many members) do not necessarily have high ratings, and vice versa. This suggests that an anime's popularity doesn't directly correlate with its quality as perceived by its audience.
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# FAQs page
def faqs():
    st.title("Frequently Asked Questions (FAQs)")
    st.write("""
    **Q: What is the purpose of this app?**
    A: This app provides personalized anime recommendations, classifies anime based on input details, and offers a platform for users to find answers to common questions.

    **Q: How do I get personalized anime recommendations?**
    A: Navigate to the 'Recommendation' page, enter your preferences, and get a list of recommended anime titles.

    **Q: How is the anime rating predicted?**
    A: The app uses machine learning algorithms to predict ratings based on the input details provided by the user.

    **Q: How can I contact the support team?**
    A: Go to the 'Contact_info' page and fill out the contact form with your details and message. The support team will get back to you as soon as possible.
    """)

    # Add an input box for users to ask questions
    st.write("**Have a question that's not listed here? Ask us below!**")
    question = st.text_input("Type your question here:")
    if st.button("Submit"):
        st.write("Thank you for your question! Our team will review it and get back to you.")

# Teams page
def teams():
    st.title("Our Team")
    st.write("""
    **Team Members:**
    - Alice
    - Bob
    - Charlie
    - Dave
    """)

    st.write("""
    **Team Lead:**
    - Eve

    **Project Manager:**
    - Frank
    """)

    st.write("""
    **About Us:**
    Our team is dedicated to providing the best anime recommendations and classifications. With a strong background in data science and machine learning, we strive to deliver accurate and personalized results to enhance your anime viewing experience.
    """)

# User Guide page
def user_guide():
    st.title("User Guide")
    st.write("""
    Welcome to the Anime Recommender System! This guide will help you navigate through the app and make the most out of its features.

    **Home Page:**
    - The home page provides an overview of the app and its features. You can watch a video introduction and learn about the different functionalities available.

    **Recommendation Page:**
    - Enter your preferences and get personalized anime recommendations. You can filter the recommendations based on different criteria.

    **Anime Classifier:**
    - Input anime details to classify and predict its rating. This feature helps you discover the potential rating of an anime based on various attributes.

    **FAQs:**
    - Find answers to common questions and ask new ones. Our FAQ section is designed to help you with any queries you might have about the app.

    **Contact_info:**
    - Provide your feedback and get in touch with us. We value your input and are here to assist you with any concerns.

    **Trailers:**
    - Watch trailers of popular and upcoming anime titles. Stay updated with the latest anime releases and get a glimpse of what's to come.

    **User Guide:**
    - This page contains all the information you need to navigate and use the app effectively.
    """)

# Title-based Recommender page
def title_recomender():
    st.title("Anime Title Recommender")

    anime_data = pd.read_csv("anime.csv")
    titles = anime_data['name'].tolist()

    selected_title = st.selectbox("Select an Anime Title", titles)
    
    if st.button("Recommend"):
        recommended_titles = recommend_titles(selected_title)
        st.write("Recommended Titles:")
        for title in recommended_titles:
            st.write(title)

def recommend_titles(selected_title):
    selected_index = anime_data[anime_data['name'] == selected_title].index[0]
    tfidf_matrix = vectorizer.transform(anime_data['name'])
    cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix[selected_index])
    similar_indices = cosine_similarities.argsort().flatten()[-10:]
    similar_titles = anime_data.iloc[similar_indices]['name'].tolist()
    return similar_titles

# Genre-based Recommender page
def genre_recomender():
    st.title("Anime Genre Recommender")

    genres = anime_data['genre'].apply(lambda x: x.split(", ")).explode().unique().tolist()
    selected_genres = st.multiselect("Select Genres", genres)

    if st.button("Recommend"):
        recommended_anime = recommend_genre(selected_genres)
        st.write("Recommended Anime:")
        for anime in recommended_anime:
            st.write(anime)

def recommend_genre(selected_genres):
    mask = anime_data['genre'].apply(lambda x: any(genre in x for genre in selected_genres))
    recommended_anime = anime_data[mask]['name'].tolist()
    return recommended_anime

# Top Rated Anime page
def top_rated_anime():
    st.title("Top Rated Anime")
    
    anime_df = pd.read_csv("anime.csv")
    top_rated = anime_df.sort_values(by='rating', ascending=False).head(10)
    
    st.write("Top 10 Rated Anime:")
    for index, row in top_rated.iterrows():
        st.write(f"{row['name']} - Rating: {row['rating']}")

# Main app
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "User Guide", "EDA", "FAQs", "Teams", "Title Recommender", "Genre Recommender", "Top Rated Anime"])

    if page == "Home":
        home()
    elif page == "User Guide":
        user_guide()
    elif page == "EDA":
        eda()
    elif page == "FAQs":
        faqs()
    elif page == "Teams":
        teams()
    elif page == "Title Recommender":
        title_recomender()
    elif page == "Genre Recommender":
        genre_recomender()
    elif page == "Top Rated Anime":
        top_rated_anime()

if __name__ == "__main__":
    main()