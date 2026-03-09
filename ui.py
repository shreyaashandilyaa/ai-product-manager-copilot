import streamlit as st


def render_header():

    st.title("🚀 AI Product Strategy Copilot")
    st.caption("Generate structured Product Management artifacts from product ideas")


def render_tool_selector():

    feature = st.selectbox(
        "Choose a tool",
        [
            "Generate PRD",
            "Generate User Stories",
            "Feature Prioritization",
            "Define MVP Scope"
        ]
    )

    idea = st.text_area(
        "Enter your product idea",
        placeholder="Example: An app that helps drivers find parking spaces in crowded cities"
    )

    return feature, idea


def render_output(result, pdf_file=None):

    if result:

        st.subheader("Generated Artifact")

        st.markdown(result)

        col1, col2 = st.columns(2)

        with col1:

            st.download_button(
                label="Download Markdown",
                data=result,
                file_name="artifact.md",
                mime="text/markdown"
            )

        if pdf_file:

            with col2:

                with open(pdf_file, "rb") as f:

                    st.download_button(
                        label="Download PDF",
                        data=f,
                        file_name="artifact.pdf",
                        mime="application/pdf"
                    )


def render_history(history):

    st.divider()
    st.subheader("Generated Outputs History")

    for index, item in enumerate(reversed(history)):

        with st.expander(f"{item['feature']} – {item['idea'][:40]}"):

            st.markdown(item["result"])

            st.download_button(
                label="Download Markdown",
                data=item["result"],
                file_name=f"{item['feature'].replace(' ', '_')}_{index}.md",
                mime="text/markdown",
                key=f"history_{index}"
            )
