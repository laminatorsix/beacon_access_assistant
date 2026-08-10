import streamlit as st
import pandas as pd

from openai_client import interpret_search_query
from auth import check_password, logout

if not check_password():
    st.stop()

logout()

st.title("🔍 Intelligent Search")

st.write(
    "Describe the BEACON function or information "
    "you need access to."
)


# Load role data
roles_df = pd.read_csv("data/roles.csv")


query = st.text_input(
    "What do you need access to?",
    placeholder="e.g. I need to check confidential HPS information"
)


if st.button("Search"):

    if not query:
        st.warning("Please enter an access requirement.")

    else:

        with st.spinner("Understanding your request..."):

            intent = interpret_search_query(query)

        if (
            intent["department"] == "UNKNOWN"
            and intent["page"] == "UNKNOWN"
            and intent["action"] == "UNKNOWN"
            and intent["access_level"] == "UNKNOWN"
        ):
            st.warning(
                "No matching roles were found. "
                "Please describe the BEACON function or information "
                "you need access to."
            )
            st.stop()


        # Display what the AI understood
        st.subheader("🔎 Request Analysis")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.write("**Department**")
            st.write(intent["department"])

        with col2:
            st.write("**Page / Function**")
            st.write(intent["page"])

        with col3:
            st.write("**Action**")
            st.write(intent["action"])

        with col4:
            st.write("**Access Level**")
            st.write(intent["access_level"])


        # Start with all data
        results = roles_df.copy()


        # Filter department
        if intent["department"] != "UNKNOWN":

            results = results[
                results["department"].str.contains(
                    intent["department"],
                    case=False,
                    na=False
                )
            ]


        # # Filter page/function
        if intent["page"] != "UNKNOWN":

            page_keywords = intent["page"].replace(
                " Verification", ""
            ).replace(
                " Preparation", ""
            )

            results = results[
                results["page"].str.contains(
                    page_keywords,
                    case=False,
                    na=False
                )
            ]


        # Filter access level
        if intent["access_level"] == "VIP":

            results = results[
                results["role"].str.contains(
                    "VIP",
                    case=False,
                    na=False
                )
            ]


        elif intent["access_level"] == "STANDARD":

            results = results[
                ~results["role"].str.contains(
                    "VIP",
                    case=False,
                    na=False
                )
            ]


        # Filter by action
        if intent["action"] == "VERIFY":

            results = results[
                results["role"].str.contains(
                    "VERIFIER",
                    case=False,
                    na=False
                )
            ]

        elif intent["action"] == "PREPARE":

            results = results[
                results["role"].str.contains(
                    "PREPARER",
                    case=False,
                    na=False
                )
            ]

        # Display results
        st.subheader("🎯 Matching Roles")


        if not results.empty:

            display_columns = [
                "role",
                "department",
                "permission",
                "page",
                "function",
                "description"
            ]

            st.dataframe(
                results[display_columns],
                use_container_width=True,
                hide_index=True
            )

            # VIP access notice
            if intent["access_level"] == "VIP":

                st.warning(
                    "⚠️ VIP access provides access to confidential "
                    "or sensitive information. Please clear the "
                    "request for VIP access with your supervisor "
                    "before applying for or requesting this role."
                )

        else:
            st.warning(
                "No matching roles were found."
            )