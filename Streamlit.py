import streamlit as st

# Title of the app
st.title("My First Streamlit App")

# Display text
st.write("Hello, Streamlit!")

# Display a dataframe
import pandas as pd
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40]
})
st.write("Here's a sample dataframe:")
st.write(df)

# Add a slider
slider_value = st.slider("Select a value", 0, 100, 50)
st.write("Slider value is:", slider_value)

# Add a button
if st.button("Click me!"):
    st.write("Button clicked!")
