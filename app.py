import streamlit as st
import pandas as pd

# Load the Excel data (adjust the file path as per your environment)
file_path = '/mnt/data/queries_responses.xlsx'
data = pd.read_excel(file_path)

# Function to match the user query with the dataset and return a response
def get_response(user_query, data):
    for index, row in data.iterrows():
        if any(keyword.lower() in user_query.lower() for keyword in row['Query'].split()):
            return row['Response']
    return "I'm sorry, I couldn't find an answer to your query."

# Streamlit UI
st.title("Academic Query Resolution Chatbot")
st.write("Welcome to the academic query resolution chatbot. Ask your queries below:")

# Input box for user query
user_query = st.text_input("Enter your query:")

# Display the response once a query is entered
if st.button('Get Answer'):
    if user_query:
        response = get_response(user_query, data)
        st.write(f"**Answer:** {response}")
    else:
        st.write("Please enter a query to get a response.")

# Professional UI adjustments
st.sidebar.title("About")
st.sidebar.info("""
This chatbot is designed to answer frequently asked questions about academic processes, campus facilities, and more.
For any further assistance, please contact the academic office.
""")

st.markdown("""
<style>
    .stApp {
        background-color: #f4f4f4;
        font-family: Arial, sans-serif;
    }
    .css-1cpxqw2 {
        border-radius: 10px;
    }
    .css-17lntkn {
        font-size: 18px;
    }
    h1 {
        color: #2c3e50;
    }
    h2, h3, h4, h5, h6 {
        color: #2980b9;
    }
</style>
""", unsafe_allow_html=True)
