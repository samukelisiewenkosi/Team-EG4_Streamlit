import streamlit as st

# Import pages
from pages import   user_guide ,classifier01 ,FAQs ,creator_info ,teams

# Define the main app function
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Home", "user_guide", "classifier01","FAQs","creator_info"])

    if page == "Home":
        home()
    elif page == "user_guide":
        user_guide.app()
    elif page == "classsifier01":
        classifier01.app()
    elif page == "FAQs":
        FAQs.app()
    elif page == "creator_info":
        creator_info.app()
    
    
def home():
    #st.title("Welcome to the Anime Recommender System")
    
    # Custom CSS for styling
    st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;  /* Light grey background */
            padding: 20px;
        }
        .header {
            font-size: 36px;
            font-weight: bold;
            color: #FF6347;  /* Tomato color */
            text-align: center;
        }
        .description {
            font-size: 18px;
            color: #4682B4;  /* Steel blue color */
        }
        .video {
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            width: 1120px; /* 2x of 560px */
            height: 630px; /* 2x of 315px */
        }
        .feature-list {
            font-size: 16px;
            color: #333;
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

    # Add a video from YouTube
    st.markdown("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/ih2reyE8xgM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen class="video"></iframe>
    """, unsafe_allow_html=True)

    st.markdown("""
    <ul class="feature-list">
    <li><strong>Recommendation:</strong> Get personalized anime recommendations.</li>
    <li><strong>Anime Classifier:</strong> Input anime details to classify and predict its rating.</li>
    <li><strong>FAQs:</strong> Find answers to common questions and ask new ones.</li>
    <li><strong>Contact_info:</strong> Provide your feedback and get in touch with us the EG4 Studios.</li>
    <li><strong>Trailers:</strong> Watch trailers of popular and upcoming anime titles.</li>
    <li><strong>User_guide:</strong> Learn how to use the app and understand its features.</li>
    </ul>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Run the main app function
if __name__ == "__main__":
    main()