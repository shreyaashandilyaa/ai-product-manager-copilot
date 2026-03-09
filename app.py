import streamlit as st
from openai import OpenAI

st.title("AI Product Manager Copilot")
st.write("AI assistant for product managers to generate product documentation and prioritization.")

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

feature = st.selectbox(
    "Choose a tool",
    [
        "Generate PRD",
        "Generate User Stories",
        "Feature Prioritization (RICE)",
        "Define MVP Scope"
    ]
)

user_input = st.text_area("Enter your product idea or feature")

if st.button("Run AI Tool"):

    prompt = f"""
    You are an expert product manager.

    Based on the following input:

    {user_input}

    Perform this task: {feature}

    Provide a structured response.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    st.write(response.choices[0].message.content)