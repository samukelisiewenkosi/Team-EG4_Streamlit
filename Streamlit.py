import streamlit as st

# Title of the app
st.title("My Streamlit App")

# Add a header
st.header("Welcome to my Streamlit app")

# Add a subheader
st.subheader("This is a basic skeleton app")

# Add some text
st.write("This app doesn't use any vectorizers. It's a simple skeleton for you to build upon.")

# Add a slider
slider_value = st.slider("Select a value", 0, 100)
st.write("Selected value:", slider_value)

# Add a button
if st.button("Click me"):
    st.write("Button clicked!")
