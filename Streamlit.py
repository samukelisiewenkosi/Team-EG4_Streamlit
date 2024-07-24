import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit app
st.title('Simple Streamlit App')

# Display some text
st.write('Welcome to the simple Streamlit app!')

# User input
name = st.text_input('Enter your name:')
age = st.number_input('Enter your age:', min_value=0, max_value=120, value=0)

# Button to submit
if st.button('Submit'):
    st.write(f'Hello, {name}! You are {age} years old.')

# Display a DataFrame
st.write('Here is a sample DataFrame:')
df = pd.DataFrame({
    'Column A': [1, 2, 3, 4],
    'Column B': [5, 6, 7, 8]
})
st.write(df)

# Plotting a simple chart
st.write('Here is a simple plot:')
fig, ax = plt.subplots()
ax.plot(df['Column A'], df['Column B'], marker='o')
ax.set_title('Sample Plot')
ax.set_xlabel('Column A')
ax.set_ylabel('Column B')
st.pyplot(fig)
