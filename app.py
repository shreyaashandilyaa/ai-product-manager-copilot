import streamlit as st
from openai import OpenAI
import os

st.title("AI Product Manager Copilot")
st.write("AI assistant to help product managers generate product documentation.")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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

    Based on the following idea:

    {idea}

    Perform this task: {feature}

    Provide a structured response.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    st.write(response.choices[0].message.content)
