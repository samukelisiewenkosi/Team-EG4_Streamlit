import streamlit as st

def app():
    # Custom CSS
    st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
            padding: 20px;
        }
        .header {
            font-size: 36px;
            font-weight: bold;
            color: #FF6347;
            text-align: center;
            margin-bottom: 20px;
        }
        .subheader {
            font-size: 24px;
            font-weight: bold;
            color: #4682B4;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .team-member {
            font-size: 20px;
            font-weight: bold;
            color: #2E8B57;
        }
        .role {
            font-size: 18px;
            font-weight: bold;
            color: #6A5ACD;
        }
        .description {
            font-size: 16px;
            color: #696969;
            margin-bottom: 20px;
        }
        .contact-info {
            font-size: 16px;
            color: #000000;
            margin-top: 20px;
        }
        .contact-info li {
            margin-bottom: 10px;
        }
        .member-card {
            background-color: #fff;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .member-card-content {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="main">', unsafe_allow_html=True)
    
    st.markdown('<p class="header">Meet the Team!</p>', unsafe_allow_html=True)
    
    st.write("Our team consists of six passionate members, each bringing their unique skills and expertise to the table:")
    
    team_members = [
        {"name": "Mieke Spaans", "role": "Data Scientist", "description": "Mieke specializes in data preprocessing and feature engineering. She ensures that the data we use is clean and ready for model training."},
        {"name": "Sinenkosi Sikhakhane", "role": "Machine Learning Engineer", "description": "Sinenkosi is responsible for building and fine-tuning our collaborative and content-based filtering models."},
        {"name": "Carroll Tshabane", "role": "NLP Expert", "description": "Carroll works on natural language processing tasks, including text analysis and word embeddings, to improve our content-based recommendations."},
        {"name": "Nduvho Nesengani Davhana", "role": "Software Engineer", "description": "Nduvho focuses on the backend development and integration of our recommendation system with the Streamlit app."},
        {"name": "Lavhelesani Ashley Leshiba", "role": "Frontend Developer", "description": "Lavhelesani designs and implements the user interface of our app, ensuring it is user-friendly and visually appealing."},
        {"name": "Samukelisiwe Nkosi", "role": "MLOps Specialist", "description": "Samukelisiwe handles the deployment, monitoring, and maintenance of our models, ensuring they run smoothly in a production environment."}
    ]

    for member in team_members:
        st.markdown(f"""
        <div class="member-card">
            <div class="member-card-content">
                <p class="team-member">{member['name']}</p>
                <p class="role">{member['role']}</p>
                <p class="description">{member['description']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<p class="subheader">Contact Us</p>', unsafe_allow_html=True)
    
    st.write("""
    We would love to hear from you! If you have any questions, suggestions, or feedback, feel free to reach out to us:
    """)
    
    st.markdown("""
    <ul class="contact-info">
    <li><strong>Email:</strong> <a href="mailto:contact@eg4studios.com">contact@eg4studios.com</a></li>
    <li><strong>Phone:</strong> +2712-346-7890</li>
    <li><strong>Website:</strong> <a href="http://www.eg4studios.com" target="_blank">www.eg4studios.com</a></li>
    <li><strong>Facebook:</strong> <a href="http://facebook.com/eg4studios" target="_blank">facebook.com/eg4studios</a></li>
    <li><strong>Twitter:</strong> <a href="http://twitter.com/eg4studios" target="_blank">twitter.com/eg4studios</a></li>
    <li><strong>Instagram:</strong> <a href="http://instagram.com/eg4studios" target="_blank">instagram.com/eg4studios</a></li>
    </ul>
    """, unsafe_allow_html=True)
    
    st.write("Thank you for using our Anime Recommender System. We hope you enjoy discovering new anime titles that you'll love!")
    
    st.markdown('</div>', unsafe_allow_html=True)

# To run the app, uncomment the following line
app()