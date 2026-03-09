import streamlit as st
from ui import render_header, render_tool_selector, render_output, render_history

# Initialize history storage
if "history" not in st.session_state:
    st.session_state.history = []

render_header()

feature, idea = render_tool_selector()

result = ""

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
- Primary users experiencing this problem
- Early adopters interested in productivity tools

### Core Features
- Core functionality solving the primary problem
- Simple interface
- Reliable performance

### Success Metrics
- User adoption
- Retention rate
- Feature engagement
"""

    elif feature == "Generate User Stories":
        result = f"""
## User Stories

1. As a user, I want to use **{idea}** so that I can solve my problem efficiently.

2. As a user, I want a simple interface so that I can interact with the system easily.
"""

    elif feature == "Feature Prioritization":
        result = f"""
## Feature Prioritization (RICE)

Feature: **{idea}**

Reach: Medium  
Impact: High  
Confidence: Medium  
Effort: Medium
"""

    elif feature == "Define MVP Scope":
        result = f"""
## MVP Scope

Core Features:
- Basic implementation of **{idea}**
- Core workflow functionality
- Simple onboarding
"""

    st.session_state.history.append({
        "idea": idea,
        "feature": feature,
        "result": result
    })

render_output(result)
render_history(st.session_state.history)
