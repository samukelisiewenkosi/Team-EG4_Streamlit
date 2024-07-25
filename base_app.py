"""

    Simple Streamlit webserver application for serving developed classification
	models.

    Author: ExploreAI Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend the functionality of this script
	as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
import joblib,os

# Data dependencies
import pandas as pd

# Vectorizer
#news_vectorizer = open("streamlit/tfidfvect.pkl","rb")
#test_cv = joblib.load(news_vectorizer) # loading your vectorizer from the pkl file

# Load your raw data
#raw = pd.read_csv("streamlit/train.csv")

# The main function where we will build the actual app
def main():
    """Anime Recommender System App with Streamlit"""
    
    # Creates a main title and subheader on your page -
    # these are static across all pages
    st.title("Anime Recommender System")
    st.subheader("Discover your next favorite anime")
    
    # Creating sidebar with selection box -
    # you can create multiple pages this way
    options = ["Prediction", "Information"]
    selection = st.sidebar.selectbox("Choose Option", options)
    
    # Building out the "Information" page
    if selection == "Information":
        st.info("General Information")
        # You can read a markdown file from supporting resources folder
        st.markdown("Some information here")
    
    # Building out the prediction page
    if selection == "Prediction":
        st.info("Anime Recommendation")
        # Creating a text box for user input
        anime_title = st.text_area("Enter Anime Title", "Type Here")
        
        if st.button("Recommend"):
            # For demonstration purposes, we will assume you have a trained model and vectorizer
            try:
                # Load the vectorizer and model (example paths)
                vectorizer = joblib.load(open(os.path.join("models/tfidf_vectorizer.pkl"), "rb"))
                model = joblib.load(open(os.path.join("models/anime_recommender.pkl"), "rb"))
                
                # Transforming user input with vectorizer
                vect_text = vectorizer.transform([anime_title]).toarray()
                
                # Make predictions
                prediction = model.predict(vect_text)
                
                # When model has successfully run, will print prediction
                # You can use a dictionary or similar structure to make this output
                # more human interpretable.
                st.success("Recommended Anime: {}".format(prediction))
            
            except Exception as e:
                st.error(f"Error: {e}")

# Required to let Streamlit instantiate our web app.
if __name__ == '__main__':
    main()