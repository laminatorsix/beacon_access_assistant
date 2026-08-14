import streamlit as st


def check_password():

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if st.session_state.authenticated:
        return True

    st.title("🔐 BEACON Troubleshooting Assistant")

    st.write(
        "Please enter the password to access the application."
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if password == st.secrets["APP_PASSWORD"]:

            st.session_state.authenticated = True
            st.rerun()

        else:

            st.error("Incorrect password.")

    return False

def logout():

    if st.sidebar.button("🚪 Logout"):

        st.session_state.authenticated = False
        st.rerun()