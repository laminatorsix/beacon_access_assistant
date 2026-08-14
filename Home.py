import streamlit as st
from auth import check_password, logout

if not check_password():
    st.stop()

logout()

st.set_page_config(
    page_title="BEACON Troubleshooting Assistant",
    page_icon="🔐",
    layout="wide"
)

with st.expander("⚠️ IMPORTANT NOTICE — Proof of Concept", expanded=True):

    st.warning(
        """
        **IMPORTANT NOTICE:** This web application is developed as a
        proof-of-concept prototype.

        The information provided here is **NOT intended for actual usage**
        and should not be relied upon for making any decisions, especially
        those related to financial, legal, or healthcare matters.

        **Furthermore, please be aware that the LLM may generate inaccurate
        or incorrect information. You assume full responsibility for how
        you use any generated output.**

        Always consult with qualified professionals for accurate and
        personalised advice.
        """
    )

st.title("🔐 BEACON Troubleshooting Assistant")

st.write(
    """
    Welcome to the BEACON Troubleshooting Assistant!

    This application helps users troubleshoot access and permissions issues
    for various screens on the BEACON platform, and identify the roles required
    to access the functions you need! 
    """
)

st.info(
    "Use the navigation menu on the left to access the "
    "Chat Assistant, Intelligent Role Search, About Us, or Methodology pages."
)

st.subheader("Available Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 💬 Chat Assistant")
    st.write(
        "Ask questions about BEACON screen access and receive "
        "AI-assisted guidance."
    )

with col2:
    st.markdown("### 🔍 Intelligent Role Search")
    st.write(
        "Search for the roles and permissions required "
        "to access specific functions."
    )