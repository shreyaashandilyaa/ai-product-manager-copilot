import streamlit as st
from ui import sidebar_navigation, render_tool_cards, render_input, render_output, render_history
from utils import generate_pdf

st.set_page_config(
    page_title="AI Product Studio",
    page_icon="🚀",
    layout="wide"
)

if "history" not in st.session_state:
    st.session_state.history = []

if "tool" not in st.session_state:
    st.session_state.tool = None


page = sidebar_navigation()


if page == "Generate Artifacts":

    st.title("AI Product Studio")

    st.caption("Generate structured Product Management artifacts from product ideas.")

    render_tool_cards()

    idea = render_input()

    result = ""

    if st.session_state.tool and st.button("Generate"):

        tool = st.session_state.tool

        if tool == "Generate PRD":

            result = f"""
## Product Requirement Document

### Product Idea
{idea}

### Problem Statement
Users currently lack efficient solutions for this problem.

### Target Users
- Individuals facing this challenge
- Early adopters interested in productivity solutions

### Core Features
- Core functionality addressing the problem
- Simple interface
- Reliable performance

### Success Metrics
- Adoption rate
- Engagement
- Retention
"""

        elif tool == "Generate User Stories":

            result = f"""
## User Stories

1. As a user, I want to use {idea} so that I can solve my problem quickly.

2. As a user, I want a simple interface so I can interact easily.
"""

        elif tool == "Feature Prioritization":

            result = f"""
## Feature Prioritization

Feature: {idea}

Reach: Medium  
Impact: High  
Confidence: Medium  
Effort: Medium
"""

        elif tool == "Define MVP Scope":

            result = f"""
## MVP Scope

Core Features
- Basic implementation of {idea}
- Simple onboarding
- Core workflow functionality
"""

        pdf_file = generate_pdf(result)

        st.session_state.history.append({
            "idea": idea,
            "feature": tool,
            "result": result
        })

        render_output(result, pdf_file)


elif page == "History":

    render_history(st.session_state.history)
