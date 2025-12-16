import streamlit as st 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(override=True)

from langchain_google_genai import ChatGoogleGenerativeAI


llm= ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    

st.title("Medical Symptom Checker")
st.set_page_config(page_title="Medical Symptom Checker", page_icon="🩺")
st.set_page_config(page_title="Medical Symptom Checker", layout="centered")
with st.container(border=True):
    symptoms = st.text_area("Describe your symptoms here:", placeholder="e.g., headache, fever, cough", height=150)
    
with st.spinner("Analyzing symptoms..."):
    response= llm.invoke(f"Based on the following symptoms: {symptoms}, suggest possible medical conditions. Keep the explanations simple and friendly.")     
    

    
def get_possible_conditions(symptoms:str)->str:
    prompt = ("You are a helpful medical assistant . based on the following symptoms, suggest 3-5 **possible medical conditions** that could be causing these symptoms. "
        "keep the explanations simple and friendly.\n\n"
        f"Symptoms: {symptoms}\n\n"
        "Response:")
    
    response = llm.invoke(prompt)
    return response.content.strip()


#symptoms = st.text_area("Enter your symptoms here:", height=200)

if st.button("Get Possible Conditions"):
    with st.spinner("Analyzing symptoms..."):
        result=get_possible_conditions(symptoms)
        st.write(result)
        
st.warning("This tool is for informational purposes only and does not replace professional medical advice. Always consult a healthcare provider for medical concerns.")        
        