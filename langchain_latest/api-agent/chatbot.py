import streamlit as st
import requests


# Function to get response from FastAPI
def get_gemini_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke", 
                             json={'input' : {
                                     'topic': input_text
                                    }})
    if response.status_code == 200:
        return response.json()['output']['content']
    return {
        'status':response.status_code,
        'response': response['output']['content']}

def get_anthropic_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke", 
                             json={'input':{
                                     'topic': input_text
                                     }})
    if response.status_code == 200:
        return response.json()
    return {
        'status':response.status_code,
        'response': response}

# Set the title of the app
st.title("Langserve API Client")

option = st.selectbox("Choose response type:", ["Poem", "Essay"])

user_input = st.text_input("Enter your prompt:")

# Process user input and display response
if user_input:
    if option == "Essay":
        response = get_gemini_response(user_input)
    else:
        response = get_anthropic_response(user_input)
    
    st.text_area("Chatbot Response:", value=response, height=200)
