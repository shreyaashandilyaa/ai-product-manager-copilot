import streamlit as st


def render_header():
    st.title("AI Product Strategy Copilot")
    st.caption("AI-powered assistant for generating Product Management artifacts")


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

    idea = st.text_area("Enter your product idea")

    return feature, idea


def render_output(result):

    if result:
        st.subheader("Generated Output")

        st.markdown(result)

        st.download_button(
            label="Download Output",
            data=result,
            file_name="pm_output.md",
            mime="text/markdown"
        )


def render_history(history):

    st.divider()
    st.subheader("Generated Outputs History")

    for index, item in enumerate(reversed(history)):

        with st.expander(f"{item['feature']} – {item['idea'][:40]}"):

            st.markdown(item["result"])

            st.download_button(
                label="Download this output",
                data=item["result"],
                file_name=f"{item['feature'].replace(' ', '_')}_{index}.md",
                mime="text/markdown",
                key=f"download_{index}"
            )
