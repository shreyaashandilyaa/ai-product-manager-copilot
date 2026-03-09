import streamlit as st

st.title("AI Product Manager Copilot")
st.write("Prototype tool that converts product ideas into structured PM artifacts.")

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

    if feature == "Generate PRD":
        result = f"""
### Problem Statement
Users struggle with the following problem: {idea}

### Target Users
- Primary users who face this challenge
- Early adopters interested in productivity tools

### Proposed Solution
A product that addresses the problem through automation and intelligent workflows.

### Success Metrics
- User adoption rate
- Feature engagement
- Retention rate
"""

    elif feature == "Generate User Stories":
        result = f"""
### User Stories

1. As a user, I want to use {idea} so that I can solve my problem efficiently.
2. As a user, I want a simple interface so that I can quickly interact with the system.
3. As a product team, we want analytics so we can measure feature adoption.
"""

    elif feature == "Feature Prioritization":
        result = f"""
### Feature Prioritization (RICE)

Feature: {idea}

Reach: Medium  
Impact: High  
Confidence: Medium  
Effort: Medium  

Priority Score: High priority for MVP experimentation.
"""

    else:
        result = f"""
### MVP Scope

Core Features:
- Basic version of {idea}
- Simple onboarding
- Core workflow functionality

Future Enhancements:
- Advanced automation
- Integrations with other tools
- Personalization features
"""

    st.markdown(result)
