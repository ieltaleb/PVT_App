import streamlit as st

# Title
st.title("My Streamlit App")

# Sidebar with widgets
user_input = st.sidebar.text_input("Enter your name:")
st.sidebar.button("Say Hello")

# Main content
st.write(f"Hello, {user_input}!")

# Data visualization
import pandas as pd

df = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})
st.line_chart(df)
