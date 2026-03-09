import streamlit as st


def sidebar_navigation():

    st.sidebar.title("AI Product Studio")

    page = st.sidebar.radio(
        "Navigation",
        ["Generate Artifacts", "History"]
    )

    return page


def render_tool_cards():

    st.subheader("Choose a Product Tool")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📄 Generate PRD"):
            st.session_state.tool = "Generate PRD"

        if st.button("🧩 Feature Prioritization"):
            st.session_state.tool = "Feature Prioritization"

    with col2:
        if st.button("📝 User Stories"):
            st.session_state.tool = "Generate User Stories"

        if st.button("🚀 Define MVP Scope"):
            st.session_state.tool = "Define MVP Scope"


def render_input():

    idea = st.text_area(
        "Enter your product idea",
        placeholder="Example: An app that helps drivers find parking spots in busy cities"
    )

    return idea


def render_output(result, pdf_file):

    if result:

        st.subheader("Generated Artifact")

        st.markdown(result)

        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                "Download Markdown",
                data=result,
                file_name="artifact.md",
                mime="text/markdown"
            )

        with col2:
            with open(pdf_file, "rb") as f:
                st.download_button(
                    "Download PDF",
                    data=f,
                    file_name="artifact.pdf",
                    mime="application/pdf"
                )


def render_history(history):

    st.title("Artifact History")

    for index, item in enumerate(reversed(history)):

        with st.expander(f"{item['feature']} – {item['idea'][:40]}"):

            st.markdown(item["result"])

            st.download_button(
                "Download",
                data=item["result"],
                file_name=f"{item['feature']}_{index}.md",
                mime="text/markdown",
                key=f"history_{index}"
            )
