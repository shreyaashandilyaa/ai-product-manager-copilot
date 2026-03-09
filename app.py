import streamlit as st
from huggingface_hub import InferenceClient

st.title("AI Product Manager Copilot")
st.write("AI assistant for product managers to generate product documentation.")

client = InferenceClient(model="mistralai/Mistral-7B-Instruct-v0.2")

feature = st.selectbox(
    "Choose a tool",
    [
        "Generate PRD",
        "Generate User Stories",
        "Feature Prioritization",
        "Define MVP Scope"
    ]
)

idea = st.text_area("Enter your product idea")

if st.button("Run AI Tool"):

    prompt = f"""
    You are an expert product manager.

    Based on this product idea:
    {idea}

    Perform the task: {feature}

    Provide a structured answer.
    """

    response = client.text_generation(prompt, max_new_tokens=500)

    st.write(response)
