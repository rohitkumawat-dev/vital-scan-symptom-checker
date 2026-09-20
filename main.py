import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# ---------------- CONFIG ----------------
load_dotenv()

st.set_page_config(
    page_title="Vital Scan",
    page_icon="🩺",
    layout="centered"
)

# ---------------- LLM ----------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    
)
if "messages" not in st.session_state:
    st.session_state.messages = []
    

# ---------------- UI ----------------
st.title("Vital Scan 🩺")

with st.container(border=True):
    symptoms = st.text_area(
        "Describe your symptoms here:",
        placeholder="e.g., headache, body pain, sore throat",
        height=150
    )

# ---------------- FUNCTION ----------------
def get_possible_conditions(symptoms: str) -> str:
    prompt = (
        "You are a helpful medical assistant. Based on the following symptoms, "
        "suggest 3–5 **possible medical conditions**.\n"
        "- Keep explanations simple and friendly.\n"
        "- If user uses Hinglish, respond in Hinglish, otherwise use English.\n"
        "- Always include a disclaimer that you are an AI and not a doctor at the end with 🚨symbol at the beginning .\n"
        "- If it sounds like an emergency, advise immediate medical attention.Based on the conversation, do the following:\n\n"
        "1. Decide the severity level:\n"
        "   🔴 Emergency\n"
        "   🟠 Moderate\n"
        "   🟢 Mild\n\n"
        "2. Show severity at the TOP in this exact format:\n"
        "**Severity: 🔴 Emergency** (or 🟠 Moderate / 🟢 Mild)\n\n"
        "3. Then explain:\n"
        "- Why this severity was chosen\n"
        "- Possible causes (2–4)\n"
        "- What the user should do next\n\n"
        "Rules:\n"
        "- Use simple language\n"
        #"- Use Hinglish if the user uses Hinglish\n"
        "- If 🔴 Emergency → clearly say to seek immediate medical help\n"
        "- If 🟢 Mild → mention that home remedies MAY help\n\n"
        f"Symptoms: {symptoms}\n\n"
        "Response:"
    )

    response = llm.invoke(prompt)
    return response.content.strip()

# ---------------- BUTTON ----------------
if st.button("Get Possible Conditions"):
    if not symptoms.strip():
        st.warning("Please enter your symptoms first.")
    else:
        with st.spinner("Analyzing symptoms..."):
            result = get_possible_conditions(symptoms)
            st.write(result)
            


# ---------------- FOOTER ----------------
st.warning(
    "🚨 This tool is for informational purposes only and does not replace professional medical advice."
)


