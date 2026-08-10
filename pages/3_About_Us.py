import streamlit as st
from auth import check_password, logout

if not check_password():
    st.stop()

logout()

st.title("ℹ️ About Us")

st.markdown(
    """
    # BEACON AI Access Assistant

    The **BEACON AI Access Assistant** is a web
    application designed to help users troubleshoot access
    issues and identify the appropriate roles required to
    access functions within the BEACON platform.

    The application uses **OpenAI GPT-4o mini** to interpret
    natural-language requests and combines this with
    structured datasets to provide relevant access
    recommendations and troubleshooting guidance.
    """
)


# ============================================================
# 1. PROJECT SCOPE
# ============================================================

st.header("1. Project Scope")

st.write(
    """
    The scope of this project is to develop a functional AI
    assistant that supports two main use cases within a
    BEACON environment:
    """
)

st.markdown(
    """
    **Use Case 1 — Chat with Information**

    Users can describe an access or platform issue using
    natural language. The AI assistant interprets the issue
    and provides relevant troubleshooting information from
    the application's knowledge base.

    Examples include:

    - Unable to view an HPS screen
    - Unable to verify a housing case
    - Receiving a "connection refused" message
    - Access has been approved but the screen is still unavailable
    - BEACON being temporarily inaccessible


    **Use Case 2 — Intelligent Search**

    Users can describe the function or information they need
    access to without needing to know the exact role name.

    The system identifies the relevant:

    - Department
    - Page or function
    - Action
    - Access level

    It then searches the role dataset and presents
    potentially relevant roles to the user.
    """
)

st.write(
    """
    The covers three business
    departments:
    """
)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("AAD")
    st.write("Accounts Accumulation Department")

with col2:
    st.subheader("HIS")
    st.write("Housing and Investment Systems")

with col3:
    st.subheader("RDD")
    st.write("Retirement Decumulation Department")

st.info(
    """
    A GENERAL category is also used for platform-wide
    troubleshooting scenarios such as connection issues,
    maintenance, and access provisioning problems.
    """
)


# ============================================================
# 2. PROJECT OBJECTIVES
# ============================================================

st.header("2. Project Objectives")

st.markdown(
    """
    The main objectives of the project are:

    **1. Improve accessibility of access information**

    Allow users to describe what they need in natural
    language rather than requiring them to know specific
    role or permission names.

    **2. Provide AI-assisted troubleshooting**

    Help users understand common BEACON access problems and
    provide appropriate next steps.

    **3. Demonstrate the application of AI**

    Demonstrate how a large language model can interpret
    natural-language queries and convert them into structured
    information that can be used by a software application.

    **4. Provide role recommendations**

    Help users identify potentially relevant roles based
    on the BEACON function they are trying to access.

    **5. Protect confidential information**

    Demonstrate the concept using data rather
    than actual internal roles, permissions, or system
    information.

    **6. Provide a simple and user-friendly interface**

    Present the AI functionality through an accessible
    Streamlit web application.
    """
)


# ============================================================
# 3. DATA SOURCES
# ============================================================

st.header("3. Data Sources")

st.write(
    """
    To protect privacy and avoid exposing actual internal
    information, this does not use production
    BEACON data.

    Instead, the application uses datasets
    created specifically for this project.
    """
)

st.subheader("Role Dataset")

st.markdown(
    """
    **`roles.csv`**

    Contains examples of:

    - BEACON roles
    - Departments
    - Permissions
    - Pages and functions
    - Actions
    - Access descriptions

    The dataset includes **PREPARER**, **VERIFIER** and
    **VIP** roles to demonstrate different levels of access.
    """
)

st.subheader("Troubleshooting Dataset")

st.markdown(
    """
    **`troubleshooting.csv`**

    Contains troubleshooting scenarios covering:

    - Access and permission problems
    - HPS and housing-related issues
    - Account and retirement-related issues
    - Connection errors
    - Platform availability issues
    - Access requests that have not yet been reflected
    - General platform problems

    Each scenario contains a possible cause and a
    recommended action.
    """
)


# ============================================================
# 4. KEY FEATURES
# ============================================================

st.header("4. Key Features")

st.subheader("💬 AI Chat Assistant")

st.write(
    """
    Users can describe an access problem in natural language.
    GPT-4o mini identifies the relevant department, page,
    action and issue before the application retrieves
    relevant troubleshooting information from the mock
    dataset.
    """
)

st.subheader("🔍 Intelligent Search")

st.write(
    """
    Users can describe the BEACON function they need access
    to. The AI identifies the user's intended department,
    page, action and access level, allowing the application
    to find matching roles.
    """
)

st.subheader("🔐 VIP Access Guidance")

st.write(
    """
    When a user searches for confidential or VIP-level
    information, the application identifies the relevant
    VIP role while reminding the user that VIP access
    should be cleared with their supervisor before requesting
    the role.
    """
)

st.subheader("⚠️ Out-of-Scope Handling")

st.write(
    """
    The Chat Assistant is designed specifically for BEACON
    access-related questions. Questions unrelated to BEACON
    access are identified as being outside the scope of the
    assistant rather than being treated as platform issues.
    """
)

st.subheader("🌐 Web-Based Interface")

st.write(
    """
    The application is built using Streamlit and provides a
    simple web interface through which users can interact
    with both AI use cases.
    """
)


# ============================================================
# 5. TECHNOLOGY
# ============================================================

st.header("5. Technologies Used")

tech_col1, tech_col2 = st.columns(2)

with tech_col1:

    st.markdown(
        """
        **Streamlit**

        Used to develop the interactive web application
        interface.

        **Python**

        Used for application logic, data processing and
        integration between the user interface, AI model
        and datasets.
        """
    )

with tech_col2:

    st.markdown(
        """
        **OpenAI GPT-4o mini**

        Used to interpret natural-language user queries and
        identify relevant structured information.

        **Pandas / CSV**

        Used to store and process the role and
        troubleshooting datasets.
        """
    )


# ============================================================
# 6. PROJECT LIMITATIONS
# ============================================================

st.header("6. Project Limitations")

st.markdown(
    """
    This application is **developed for
    the purposes of this project**.

    It does not:

    - Connect to the actual BEACON platform
    - Access production databases
    - Grant or revoke user permissions
    - Authenticate users against an internal identity system
    - Determine whether a user is actually authorised to
      receive a role
    - Replace existing access approval processes

    Role recommendations provided by the application are
    based entirely on the datasets created for it.
    """
)


# ============================================================
# 7. DOCUMENTATION
# ============================================================

st.header("7. Project Documentation")

st.write(
    """
    This application contains a separate **Methodology**
    page explaining how the system works, including the data
    flows and implementation approach for both use cases.
    """
)

st.markdown(
    """
    **Methodology**

    The Methodology page documents:

    - Overall application architecture
    - Chat Assistant data flow
    - Intelligent Search data flow
    - Use of GPT-4o mini
    - Processing of datasets
    - Role matching logic
    - Troubleshooting retrieval
    - Flowcharts for both use cases
    """
)