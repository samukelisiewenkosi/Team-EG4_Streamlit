import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os

def load_data():
    train_df = pd.read_csv('train.csv')
    test_df = pd.read_csv('test.csv')
    anime_df = pd.read_csv('anime.csv')
    return train_df, test_df, anime_df

def generate_wordcloud(text_data, title):
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(text_data)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(title, fontsize=20)
    plt.axis('off')
    st.pyplot(plt)

def app():
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

    plt.figure(figsize=(8, 5))
    sns.barplot(x=type_avg_rating.values, y=type_avg_rating.index, palette='viridis')
    plt.title('Average Rating by Anime Type')
    plt.xlabel('Average Rating')
    plt.ylabel('Anime Type')
    plt.tight_layout()
    st.pyplot(plt)



    st.markdown("""
    **Interpretation:**
    This bar chart shows that TV series generally receive higher average ratings compared to other types like Movies or OVAs. This insight is useful for understanding viewer preferences.
    """)

    # Distribution of Ratings
    st.subheader("Distribution of Anime Ratings")
    plt.figure(figsize=(10, 6))
    sns.histplot(anime_df['rating'].dropna(), bins=30, kde=False, color='skyblue')
    plt.title('Distribution of Anime Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)



    st.markdown("""
    **Interpretation:**
    The distribution of ratings shows that most anime are rated between 6 and 10, with fewer titles receiving extremely high or low ratings. This skew towards higher ratings suggests a generally positive reception.
    """)

    # Correlation Heatmap
    st.subheader("Correlation Heatmap of Ratings and Members")
    numeric_cols = anime_df[['rating', 'members']]
    corr_matrix = numeric_cols.corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap of Anime Ratings and Members')
    plt.tight_layout()
    st.pyplot(plt)



    st.markdown("""
    **Interpretation:**
    The heatmap reveals a moderate positive correlation (0.39) between the number of members and ratings. This suggests that more popular anime tend to have higher ratings, though the correlation is not particularly strong.
    """)

    # Box Plots for Movie and TV Show Ratings
    st.subheader("Distribution of Ratings for Movies and TV Shows")
    movie = anime_df[anime_df['type'] == 'Movie']
    tv = anime_df[anime_df['type'] == 'TV']

    fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

    sns.boxplot(ax=axes[0], x=movie['type'], y=movie['rating'], palette='Blues')
    axes[0].set_title('Distribution of Ratings for Movies')

    sns.boxplot(ax=axes[1], x=tv['type'], y=tv['rating'], palette='Greens')
    axes[1].set_title('Distribution of Ratings for TV Shows')

    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("""
    **Interpretation:**
    TV shows have a higher median rating compared to movies, indicating more consistent quality. Movies show a wider range of ratings, suggesting more variability in quality.
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# Run the app function if this script is executed
if __name__ == "__main__":
    app()