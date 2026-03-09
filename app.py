import streamlit as st
import base64

from ui import render_header, render_tool_selector, render_output, render_history


# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="AI Product Studio",
    page_icon="🚀",
    layout="wide"
)


# -------------------------
# BACKGROUND IMAGE FUNCTION
# -------------------------

def set_background(image_file):

    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()

    page_bg = f"""
    <style>

    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    .block-container {{
        background: rgba(255, 255, 255, 0.90);
        padding: 2rem;
        border-radius: 15px;
    }}

    </style>
    """

    st.markdown(page_bg, unsafe_allow_html=True)


# Apply background
set_background("assets/background.jpg")


# -------------------------
# SESSION STATE
# -------------------------

if "history" not in st.session_state:
    st.session_state.history = []


# -------------------------
# UI RENDERING
# -------------------------

render_header()

feature, idea = render_tool_selector()

result = ""


# -------------------------
# GENERATION LOGIC
# -------------------------

if st.button("Run AI Tool"):

    if feature == "Generate PRD":

        result = f"""
## Product Requirement Document (PRD)

### Product Overview
**{idea}**

This product aims to solve the problem by delivering a streamlined user experience.

### Problem Statement
Users currently face inefficiencies and lack convenient tools to address this challenge.

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

    elif feature == "Generate User Stories":

        result = f"""
## User Stories

1. As a user, I want to use **{idea}** so that I can solve my problem efficiently.

2. As a user, I want a simple interface so that I can interact with the system easily.
"""

    elif feature == "Feature Prioritization":

        result = f"""
## Feature Prioritization (RICE Framework)

Feature: **{idea}**

Reach: Medium  
Impact: High  
Confidence: Medium  
Effort: Medium
"""

    elif feature == "Define MVP Scope":

        result = f"""
## MVP Scope

Core Features
- Basic implementation of **{idea}**
- Simple onboarding
- Core workflow functionality
"""

    # Save to history
    st.session_state.history.append({
        "idea": idea,
        "feature": feature,
        "result": result
    })


# -------------------------
# DISPLAY OUTPUT
# -------------------------

render_output(result)

render_history(st.session_state.history)
