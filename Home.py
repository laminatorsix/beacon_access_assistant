import streamlit as st
from auth import check_password, logout

if not check_password():
    st.stop()

logout()

st.set_page_config(
    page_title="BEACON Access Assistant",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 BEACON Access Assistant")

st.write(
    """
    Welcome to the BEACON Access Assistant!

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