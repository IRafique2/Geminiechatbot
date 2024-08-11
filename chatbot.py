import google.generativeai as genai
import streamlit as st
#add apikey here
API_KEY="AIzaSyDXuiZzPCmavxg2DH7NN5_rvKO5nM0xNaA"
genai.configure(api_key=API_KEY)
#initialize model
model = genai.GenerativeModel('gemini-1.5-flash')
#create a function to get response
def GetResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text
st.title("Geminie Chatbot")

user_input=st.text_input("Enter your prompt")
if st.button("Get Response"):
    if user_input:
        output=GetResponseFromModel(user_input)
        st.write(f"Chatbot Response: {output}")
    else:
        st.write("Enter Promopt")