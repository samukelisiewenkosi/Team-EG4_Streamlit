import streamlit as st

# Placeholder data for demonstration
anime_list = [
    "Naruto",
    "One Piece",
    "Attack on Titan",
    "My Hero Academia",
    "Demon Slayer",
    "Sword Art Online",
    "Fullmetal Alchemist: Brotherhood",
    "Death Note",
    "Dragon Ball Z",
    "Tokyo Ghoul"
]

# Function to display the about page
def about_page():
    st.title("About This App")
    st.write("""
        Welcome to the Anime Classification and Recommendation App!
        
        This application aims to classify and recommend anime titles based on user preferences and inputs.
        Although the current version does not include a trained model, future updates will incorporate advanced machine learning techniques for personalized recommendations.

        Stay tuned for more features and updates!
    """)

# Function to display the recommendation page
def recommendation_page():
    st.title("Anime Recommendation")
    st.write("Select your favorite anime genre to get recommendations:")

    # User input for favorite genre (placeholder for demo purposes)
    genre = st.selectbox("Choose a genre:", ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Horror", "Mystery", "Romance", "Sci-Fi", "Thriller"])

    # Display placeholder recommendations
    st.write(f"Recommendations for {genre} genre:")
    recommendations = anime_list[:5]  # Displaying the first 5 animes as placeholder
    for anime in recommendations:
        st.write(f"- {anime}")

# Main function to control the app navigation
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["About", "Recommendations"])

    if page == "About":
        about_page()
    elif page == "Recommendations":
        recommendation_page()

if __name__ == "__main__":
    main()