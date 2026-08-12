import streamlit as st
import pandas as pd

from openai_client import interpret_troubleshooting_query
from auth import check_password, logout

if not check_password():
    st.stop()

logout()

st.title("💬 Chat Assistant")

st.write(
    "Describe your BEACON access issue and the assistant "
    "will provide troubleshooting guidance."
)

# Load troubleshooting data
troubleshooting_df = pd.read_csv(
    "data/troubleshooting.csv"
)

# Initialise chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Example questions
st.write("**Try an example:**")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button(
        "🏠 Housing case",
        use_container_width=True
    ):
        st.session_state.example_prompt = (
            "Why can't I verify a housing case?"
        )

with col2:
    if st.button(
        "🔌 Connection refused",
        use_container_width=True
    ):
        st.session_state.example_prompt = (
            "Why is BEACON showing connection refused?"
        )

with col3:
    if st.button(
        "⏳ Access approved",
        use_container_width=True
    ):
        st.session_state.example_prompt = (
            "I applied for access already but I still can't see the screen."
        )

with col4:
    if st.button(
        "⚠️ Confidential information",
        use_container_width=True
    ):
        st.session_state.example_prompt = (
            "I can't view confidential information."
        )

# Chat input
prompt = st.chat_input(
    "Describe your access issue..."
)

# Use example question if one was selected
if "example_prompt" in st.session_state:

    if prompt is None:
        prompt = st.session_state.example_prompt

    del st.session_state.example_prompt

if prompt:
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Understand the problem
    with st.spinner("Analysing your issue..."):

        intent = interpret_troubleshooting_query(prompt)

    # Check whether this is a BEACON access issue
    if not intent["is_beacon_access_issue"]:

        response = (
            "I'm designed to help troubleshoot access issues "
            "within the BEACON platform. "
            "This question does not appear to be related to "
            "BEACON access."
        )

        with st.chat_message("assistant"):
            st.markdown(response)

    else:

        # Find relevant troubleshooting information
        results = troubleshooting_df.copy()

        # Filter by department
        if intent["department"] != "UNKNOWN":

            results = results[
                results["department"].str.contains(
                    intent["department"],
                    case=False,
                    na=False
                )
            ]

        # Filter by page
        if intent["page"] != "UNKNOWN":

            results = results[
                results["page"].str.contains(
                    intent["page"],
                    case=False,
                    na=False
                )
            ]

        # Filter by action
        if intent["action"] != "UNKNOWN":
            if intent["action"] == "VERIFY":

                results = results[
                    results["issue"].str.contains(
                        "verify",
                        case=False,
                        na=False
                    )
                ]

            elif intent["action"] == "PREPARE":

                results = results[
                    results["issue"].str.contains(
                        "update|prepare|create",
                        case=False,
                        na=False
                    )
                ]

        # If no specific department or page was identified,
        # search using the identified issue.
        # Filter by identified issue
        if intent["issue"] != "UNKNOWN":

            results = results[
                results["issue"].str.contains(
                    intent["issue"],
                    case=False,
                    na=False,
                    regex=False
                )
            ]

        # Generate response
        with st.chat_message("assistant"):

            if not results.empty:

                result = results.iloc[0]

                response = f"""
    **Possible cause:**  
    {result["possible_cause"]}

    **Recommended action:**  
    {result["recommended_action"]}

    **Department:**  
    {result["department"]}

    **Page:**  
    {result["page"]}
    """

            else:

                response = (
                    "I couldn't find a matching troubleshooting "
                    "scenario in the knowledge base. "
                    "Please check that you have the appropriate "
                    "BEACON access role or contact your administrator."
                )

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )