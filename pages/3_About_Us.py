import streamlit as st
from auth import check_password, logout

if not check_password():
    st.stop()

logout()

st.title("ℹ️ About Us")

st.markdown(
    """
    # BEACON AI Troubleshooting Assistant

    The **BEACON AI Troubleshooting Assistant** is an educational web
    application prototype designed to help users troubleshoot
    access-related issues and identify potentially relevant
    roles for functions within the BEACON platform.

    The application combines **OpenAI GPT-4o mini**, Python
    application logic and structured datasets to interpret
    natural-language requests and provide relevant information.

    The project demonstrates how AI can be integrated into a
    practical web application while keeping access decisions
    controlled by predefined application data and logic.
    """
)

# ============================================================
# 1. PROJECT SCOPE
# ============================================================

st.header("1. Project Scope")

st.write(
    """
    The project focuses on two main use cases that support
    BEACON access-related tasks.
    """
)

st.subheader("💬 Use Case 1 — Chat with Information")

st.write(
    """
    The Chat Assistant allows users to describe an access or
    platform issue using natural language. GPT-4o mini interprets
    the request and the application retrieves relevant
    troubleshooting information from the knowledge base.
    """
)

st.markdown(
    """
    **Example scenarios:**

    - Unable to view an HPS screen
    - Unable to verify a housing case
    - Receiving a "connection refused" message
    - Access has been approved but the screen is still unavailable
    - BEACON being temporarily inaccessible
    - Access requests that have not yet been reflected
    """
)

st.subheader("🔍 Use Case 2 — Intelligent Search")

st.write(
    """
    Intelligent Search allows users to describe the BEACON
    function or information they need without having to know
    the exact role name.

    GPT-4o mini interprets the request and identifies:
    """
)

st.markdown(
    """
    - **Department**
    - **Page / Function**
    - **Action**
    - **Access Level**

    The application then uses these attributes to search the
    role dataset and display potentially relevant roles.
    """
)

st.info(
    """
    The Intelligent Search function recommends potentially
    relevant roles. It does not grant, approve or provision
    access.
    """
)

# ============================================================
# 2. DEPARTMENTS
# ============================================================

st.header("2. BEACON Departments")

st.write(
    """
    The prototype represents three business
    departments within the BEACON platform:
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
    A **GENERAL** category is also used for platform-wide
    troubleshooting scenarios, such as connection issues,
    maintenance, platform availability and access provisioning
    problems.
    """
)

# ============================================================
# 3. PROJECT OBJECTIVES
# ============================================================

st.header("3. Project Objectives")

st.markdown(
    """
    ### 1. Improve accessibility of access information

    Allow users to describe their requirements in natural
    language rather than requiring them to know specific role
    or permission names.

    ### 2. Provide AI-assisted troubleshooting

    Help users identify possible causes of common BEACON access
    issues and provide appropriate next steps.

    ### 3. Demonstrate practical use of AI

    Demonstrate how a large language model can interpret
    natural-language requests and convert them into structured
    information that can be processed by a software application.

    ### 4. Provide role recommendations

    Help users identify potentially relevant roles based on
    the BEACON function they are trying to access.

    ### 5. Provide a user-friendly interface

    Present both AI use cases through a simple, accessible
    multi-page Streamlit web application.
    """
)

# ============================================================
# 4. DATA SOURCES
# ============================================================

st.header("4. Data Sources")

st.subheader("📋 Role Dataset — roles.csv")

st.write(
    """
    The role dataset provides the structured information used
    by the Intelligent Search function.
    """
)

st.markdown(
    """
    **The dataset contains examples of:**

    - BEACON roles
    - Departments
    - Permissions
    - Pages and functions
    - Actions
    - Access levels
    - Role descriptions

    The prototype includes **PREPARER**, **VERIFIER** and
    **VIP** roles to demonstrate different access requirements.
    """
)

st.subheader("🛠️ Troubleshooting Dataset — troubleshooting.csv")

st.write(
    """
    The troubleshooting dataset provides the knowledge base
    used by the Chat Assistant.
    """
)

st.markdown(
    """
    **The dataset contains scenarios covering:**

    - Access and permission problems
    - HPS and housing-related issues
    - Account-related issues
    - Retirement-related issues
    - Connection errors
    - Platform availability issues
    - Access requests that have not yet been reflected
    - General platform problems

    Each scenario contains information such as the possible
    cause and recommended action.
    """
)

# ============================================================
# 5. KEY FEATURES
# ============================================================

st.header("5. Key Features")

st.subheader("💬 AI Chat Assistant")

st.write(
    """
    Users can describe an access problem using natural language.
    GPT-4o mini interprets the request and identifies relevant
    information before the application retrieves a matching
    troubleshooting scenario.
    """
)

st.subheader("🔍 Intelligent Search")

st.write(
    """
    Users can describe the BEACON function they need access to.
    The AI identifies the intended department, page, action and
    access level, allowing the application to search for matching
    roles.
    """
)

st.subheader("🔐 VIP Access Guidance")

st.write(
    """
    VIP roles represent access to more confidential or sensitive
    information within the platform.

    When VIP access is identified, the application displays a
    reminder that the request should be cleared with the user's
    supervisor before requesting the role.
    """
)

st.subheader("⚠️ Out-of-Scope Handling")

st.write(
    """
    The Chat Assistant is designed specifically for BEACON
    access-related questions. Requests that are unrelated to
    BEACON access are not treated as platform issues.
    """
)

st.subheader("🛡️ Basic Security Safeguards")

st.write(
    """
    The prototype includes basic safeguards to reduce misuse
    of the AI functionality.
    """
)

st.markdown(
    """
    - The application is password protected.
    - User input is treated as untrusted input.
    - The AI is instructed not to follow attempts to override
      its system instructions.
    - The AI does not directly grant or provision access.
    - Role recommendations are determined using the structured
      dataset and application logic.
    - VIP requests include an explicit supervisor approval
      reminder.
    - API credentials and application secrets are stored using
      Streamlit Secrets rather than directly in the source code.
    """
)

# ============================================================
# 6. TECHNOLOGY
# ============================================================

st.header("6. Technologies Used")

tech_col1, tech_col2 = st.columns(2)

with tech_col1:
    st.markdown(
        """
        **Streamlit**

        Used to develop the multi-page web application and
        interactive user interface.

        **Python**

        Used for application logic, data processing and
        integration between the interface, AI model and
        datasets.
        """
    )

with tech_col2:
    st.markdown(
        """
        **OpenAI GPT-4o mini**

        Used to interpret natural-language requests and
        identify structured information such as department,
        page, action and access level.

        **Pandas / CSV**

        Used to store and process the role and
        troubleshooting datasets.
        """
    )

# ============================================================
# 7. HOW THE AI IS USED
# ============================================================

st.header("7. How AI Is Used")

st.write(
    """
    GPT-4o mini is used primarily for **natural-language
    understanding**, rather than as the source of truth for
    roles or permissions.
    """
)

st.markdown(
    """
    The general process is:

    **User request**

    ↓

    **GPT-4o mini interprets the request**

    ↓

    **Structured information is produced**

    ↓

    **Python validates and processes the information**

    ↓

    **dataset is searched**

    ↓

    **Relevant information is presented to the user**
    """
)

st.info(
    """
    Separating AI interpretation from the application's
    deterministic role-matching logic helps prevent the AI
    from directly making access decisions.
    """
)

# ============================================================
# 8. PROJECT LIMITATIONS
# ============================================================

st.header("8. Project Limitations")


st.markdown(
    """
    **The application does not:**

    - Connect to the actual BEACON platform
    - Access production databases
    - Grant or revoke user permissions
    - Provision roles
    - Authenticate users against an internal identity system
    - Determine whether a real user is authorised to receive
      a role
    - Replace existing access approval processes
    - Provide actual confidential BEACON information

    Role recommendations and troubleshooting responses are
    based on the datasets created for this
    project.
    """
)

# ============================================================
# 9. DOCUMENTATION
# ============================================================

st.header("9. Project Documentation")

st.write(
    """
    The application includes a dedicated Methodology page that
    provides further technical documentation of the system.
    """
)

st.markdown(
    """
    **The Methodology page covers:**

    - Overall application architecture
    - Data sources and data processing
    - Chat Assistant data flow
    - Intelligent Search data flow
    - Prompt engineering
    - AI output processing
    - Role matching logic
    - Troubleshooting retrieval
    - Security and prompt-injection safeguards
    - Error handling
    - System limitations
    """
)

st.success(
    """
    For a detailed explanation of how the application works,
    see the **Methodology** page.
    """
)