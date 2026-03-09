import streamlit as st

# Initialize history storage
if "history" not in st.session_state:
    st.session_state.history = []

st.title("AI Product Strategy Copilot")
st.write("Prototype tool that converts product ideas into structured Product Management artifacts.")

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

result = ""

if st.button("Run AI Tool"):

    if feature == "Generate PRD":
        result = f"""
## Product Requirement Document (PRD)

### 1. Product Overview
The product aims to solve the following problem:

**{idea}**

This solution focuses on improving efficiency, accessibility, and user experience through a streamlined digital workflow.

---

### 2. Problem Statement
Many users currently face friction when dealing with this problem. Existing solutions may be fragmented, manual, or inefficient.

Key challenges include:
- Lack of convenient solutions
- Time-consuming processes
- Poor user experience in existing tools

---

### 3. Target Users
Primary Users:
- Individuals directly experiencing the problem
- Users seeking a faster and more convenient solution

Secondary Users:
- Businesses or stakeholders who benefit indirectly from improved workflows

---

### 4. User Personas
Persona 1: Everyday User  
Needs a simple and intuitive solution to quickly address the problem.

Persona 2: Power User  
Requires more advanced functionality and reliability for frequent usage.

---

### 5. User Stories
1. As a user, I want to use this solution so that I can address the problem quickly.
2. As a user, I want a simple interface so that I can easily navigate the product.
3. As a user, I want reliable results so that I trust the platform.

---

### 6. Core Features
- Core functionality addressing the main problem
- User-friendly interface
- Reliable processing of user inputs
- Scalable architecture for future improvements

---

### 7. MVP Scope
The Minimum Viable Product will include:
- Basic functionality to solve the primary user problem
- Simple onboarding experience
- Core workflow execution
- Basic analytics for product monitoring

---

### 8. Success Metrics
- User adoption rate
- Daily/Monthly active users
- Feature engagement rate
- User retention rate

---

### 9. Risks & Considerations
Potential risks include:
- Low initial adoption
- Technical limitations during early development
- User trust and reliability concerns

Mitigation strategies include iterative development and continuous user feedback.

---

### 10. Future Enhancements
- Advanced automation features
- Personalization capabilities
- Integrations with external platforms
"""

    elif feature == "Generate User Stories":
        result = f"""
## User Stories

1. As a user, I want to use **{idea}** so that I can solve my problem efficiently.

2. As a user, I want a simple interface so that I can quickly interact with the system.

3. As a product team, we want analytics so we can measure feature adoption and improve the product.
"""

    elif feature == "Feature Prioritization":
        result = f"""
## Feature Prioritization (RICE Framework)

Feature Idea: **{idea}**

Reach: Medium  
Impact: High  
Confidence: Medium  
Effort: Medium  

### Priority Score
High priority candidate for MVP experimentation.
"""

    elif feature == "Define MVP Scope":
        result = f"""
## MVP Scope

Core Features:
- Basic implementation of **{idea}**
- Simple onboarding flow
- Core user workflow
- Basic analytics tracking

Future Enhancements:
- Advanced automation
- Integrations with other platforms
- Personalization capabilities
"""

    # Display output
    st.markdown(result)

    # Download button
    st.download_button(
        label="Download Output",
        data=result,
        file_name="pm_output.md",
        mime="text/markdown"
    )

    # Save to history
    st.session_state.history.append({
        "idea": idea,
        "feature": feature,
        "result": result
    })


# History Section
st.divider()
st.subheader("Generated Outputs History")

for item in reversed(st.session_state.history):
    with st.expander(f"{item['feature']} – {item['idea'][:40]}"):
        st.markdown(item["result"])
