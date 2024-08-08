import streamlit as st

def app():
    # Add custom CSS for background color
    st.markdown("""
    <style>
        .main {
            background-color: #f0f0f0;  /* Light grey background color */
            padding: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main">', unsafe_allow_html=True)
    
    st.title("User Guide")
    st.markdown("""
    ## Overview
    Welcome to the Anime Recommender System! This app helps you discover new anime based on your preferences and viewing history. It combines collaborative and content-based filtering techniques to provide accurate recommendations.

    ## Main Features
    1. **Recommendation**: Get personalized anime recommendations.
    2. **Anime Classifier**: Input anime details to classify and predict its rating.
    3. **FAQs**: Find answers to common questions and ask new ones.
    4. **Contact**: Provide feedback and get in touch with the team.
    5. **Trailers**: Watch trailers of popular anime titles.

    ## Getting Started

    ### Home Page
    When you first open the app, you'll land on the Home Page. Here, you can read an introduction to the app and its purpose. You'll also find a YouTube video explaining how recommendation systems work.

    ### Navigation
    Use the sidebar to navigate between different sections of the app:
    - **Home**
    - **Recommendation**
    - **Anime Classifier**
    - **FAQs**
    - **Contact**
    - **Trailers**

    ### Recommendations
    1. Go to the "Recommendation" page from the sidebar.
    2. The app will display a list of anime recommendations tailored to your preferences.
    3. Provide feedback on the recommendations using the "Contact" page.

    ### Anime Classifier
    1. Navigate to the "Anime Classifier" page.
    2. Input details such as the title, genre, number of episodes, rating, and number of members.
    3. Click on the "Classify" button to get a prediction based on your input.
    4. The app will display the classification result.

    ### FAQs
    1. Visit the "FAQs" page to find answers to common questions.
    2. If your question is not listed, use the question submission form at the bottom of the page.
    3. Enter your email and question, then submit. We will get back to you via email.

    ### Contact
    1. Go to the "Contact" page.
    2. Use the provided form to send feedback or queries.
    3. Enter your name, email, and message, then submit.

    ### Trailers
    1. Navigate to the "Trailers" page to watch trailers of popular and upcoming anime.
    2. Click on the embedded videos to play them directly within the app.

    ## Managing the App
    ### Admin Responsibilities
    - **Content Management**: Regularly update the anime database and ensure the recommendation algorithm is up-to-date.
    - **User Interaction**: Monitor user feedback and questions submitted through the FAQ and Contact pages. Respond to users in a timely manner.
    - **System Maintenance**: Ensure the app runs smoothly by performing routine checks and updates.

    ### Handling Questions from FAQ
    - Questions submitted through the FAQ page will be sent to the designated admin email.
    - Check the admin email regularly for new submissions.
    - Respond to user questions via email, providing detailed answers and assistance.
    """)

    st.markdown('</div>', unsafe_allow_html=True)