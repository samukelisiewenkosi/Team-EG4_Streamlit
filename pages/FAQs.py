import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
import os

def send_email(user_email, user_question):
    sender_email = "your_email@example.com"
    receiver_email = "your_email@example.com"
    password = "your_password"

    message = MIMEMultipart("alternative")
    message["Subject"] = "New FAQ Question"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = f"""
    You have received a new question from {user_email}:
    {user_question}
    """
    part = MIMEText(text, "plain")
    message.attach(part)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return True
    except Exception as e:
        st.error(f"Error: {e}")
        return False

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
    
    st.title("FAQs")
    st.markdown("## Frequently Asked Questions")

    st.markdown("""
    ### What is this application about?
    This application is an anime recommender system that suggests anime titles based on your preferences.

    ### How does the recommendation system work?
    The system uses collaborative and content-based filtering techniques to predict and recommend anime titles you might enjoy.

    ### What data is used for recommendations?
    The recommendations are based on user ratings and anime metadata from MyAnimeList.

    ### How can I get personalized recommendations?
    Navigate to the "Recommendation" page, input your preferences, and the system will generate recommendations for you.

    ### Can I provide feedback on the recommendations?
    Yes, you can use the "Contact" page to provide feedback and get in touch with us.

    ### How do I use the Anime Classifier?
    - Go to the "Anime Classifier" page.
    - Input details such as the anime title, genre, number of episodes, rating, and members.
    - Click on the "Classify" button to get a prediction based on your input.

    ### Is my data safe?
    Yes, we ensure that your data is kept confidential and used only for providing better recommendations.

    ### Who can I contact for more information?
    For more information, please visit the "Contact" page and reach out to us with your queries.
    """)

    st.markdown("## Ask a Question")
    st.write("If you have any questions that are not addressed here, please feel free to ask us.")

    with st.form(key='question_form'):
        user_email = st.text_input("Your Email")
        user_question = st.text_area("Your Question")
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if user_email and user_question:
            if send_email(user_email, user_question):
                # Store the form data in a CSV file
                data = {'Email': [user_email], 'Question': [user_question]}
                df = pd.DataFrame(data)

                if not os.path.isfile('faq_submissions.csv'):
                    df.to_csv('faq_submissions.csv', index=False)
                else:
                    df.to_csv('faq_submissions.csv', mode='a', header=False, index=False)

                st.success("Thank you for your question! We will get back to you soon.")
            else:
                st.error("There was an error submitting your question. Please try again later.")
        else:
            st.error("Please fill in both the email and question fields.")
    
    st.markdown('</div>', unsafe_allow_html=True)
app()