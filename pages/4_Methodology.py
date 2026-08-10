import streamlit as st
from auth import check_password, logout

if not check_password():
    st.stop()

logout()

st.title("📖 Methodology")

st.markdown(
    """
    This page describes the methodology used to develop the
    BEACON AI Access Assistant, including the overall
    architecture, data flows, AI processing and implementation
    approach for the two main use cases.
    """
)


# ============================================================
# 1. OVERALL SYSTEM ARCHITECTURE
# ============================================================

st.header("1. Overall System Architecture")

st.markdown(
    """
    The application follows a simple architecture consisting
    of four main components:

    1. **Streamlit** – Provides the web application interface.
    2. **OpenAI GPT-4o mini** – Interprets natural-language
       user requests.
    3. **Python application logic** – Processes the AI output
       and determines how the request should be handled.
    4. **CSV datasets** – Provide the role and
       troubleshooting information used by the application.
    """
)

st.code(
    """
                    ┌─────────────────────┐
                    │        User         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Streamlit       │
                    │    Web Interface    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   OpenAI GPT-4o     │
                    │       mini          │
                    └──────────┬──────────┘
                               │
                         Structured
                           intent
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Python Logic      │
                    └──────────┬──────────┘
                               │
                  ┌────────────┴────────────┐
                  ▼                         ▼
        ┌──────────────────┐      ┌────────────────────┐
        │    roles.csv     │      │troubleshooting.csv │
        └────────┬─────────┘      └──────────┬─────────┘
                 │                           │
                 └─────────────┬─────────────┘
                               ▼
                    ┌─────────────────────┐
                    │   Result / Advice   │
                    └─────────────────────┘
    """,
    language="text"
)


# ============================================================
# 2. USE CASE 1 - CHAT ASSISTANT
# ============================================================

st.header("2. Use Case 1 — Chat Assistant")

st.write(
    """
    The Chat Assistant allows users to describe BEACON access
    or platform problems using natural language.

    The system uses GPT-4o mini to determine whether the query
    relates to BEACON access and, if so, identifies the relevant
    department, page, action and issue. Python then searches
    the troubleshooting dataset for a relevant scenario.
    """
)


st.subheader("Chat Assistant Data Flow")

st.code(
    """
    ┌──────────────────────────────┐
    │ User enters a question      │
    │ "Why can't I verify a       │
    │  housing case?"             │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │ Streamlit Chat Interface     │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │ GPT-4o mini                  │
    │                              │
    │ Identifies:                  │
    │ • Access issue?              │
    │ • Department                 │
    │ • Page                       │
    │ • Action                     │
    │ • Issue                      │
    └──────────────┬───────────────┘
                   │
                   ▼
          ┌───────────────────┐
          │ BEACON issue?    │
          └───────┬───────────┘
                  │
          ┌───────┴────────┐
          │                │
         NO               YES
          │                │
          ▼                ▼
    ┌─────────────┐  ┌───────────────────┐
    │ Out of      │  │ Search            │
    │ scope       │  │ troubleshooting   │
    │ response    │  │ dataset           │
    └─────────────┘  └─────────┬─────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Matching scenario   │
                    │                     │
                    │ • Possible cause    │
                    │ • Recommended       │
                    │   action            │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Display response    │
                    │ to user             │
                    └─────────────────────┘
    """,
    language="text"
)


st.subheader("Example")

st.markdown(
    """
    **User query:**

    > Why can't I verify a housing case?

    **GPT-4o mini identifies:**

    - Access issue: `TRUE`
    - Department: `HIS`
    - Page: `Housing Case`
    - Action: `VERIFY`
    - Issue: `Cannot verify a housing case`

    **Python then searches `troubleshooting.csv`** and
    retrieves the corresponding scenario.

    **Result:**

    > Possible cause: User may not have verification access.
    >
    > Recommended action: Check whether the user has the HIS
    > VERIFIER role.
    """
)


# ============================================================
# 3. GENERAL TROUBLESHOOTING
# ============================================================

st.subheader("Platform-Wide Troubleshooting")

st.write(
    """
    Some problems are not specific to a particular department
    or page. These are classified under the 
    `GENERAL` category.
    """
)

st.markdown(
    """
    Examples include:

    - Connection refused
    - BEACON being unavailable
    - Scheduled maintenance
    - Access requests still being processed
    - Approved access not yet appearing
    - Pages continuously loading
    - Platform performance issues
    """
)

st.write(
    """
    For these cases, the AI can identify the issue as a
    platform-wide problem and retrieve the relevant
    troubleshooting guidance without requiring a specific
    department or page.
    """
)


# ============================================================
# 4. USE CASE 2 - INTELLIGENT SEARCH
# ============================================================

st.header("3. Use Case 2 — Intelligent Search")

st.write(
    """
    The Intelligent Search function helps users determine
    which role may be appropriate for a particular
    BEACON function.

    Instead of requiring users to know the role name, they
    can describe what they want to do using natural language.
    """
)


st.subheader("Intelligent Search Data Flow")

st.code(
    """
    ┌──────────────────────────────┐
    │ User enters a request       │
    │ "I need to verify a         │
    │  housing case"              │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │ Streamlit Search Interface   │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │ GPT-4o mini                  │
    │                              │
    │ Identifies:                  │
    │ • Department                 │
    │ • Page                       │
    │ • Action                     │
    │ • Access level               │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │ Python filtering logic       │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │       roles.csv              │
    │                              │
    │ Filter by:                   │
    │ • Department                 │
    │ • Page                      │
    │ • Action                     │
    │ • Access level               │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │ Matching role(s)        │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │ Display role recommendation  │
    │ to user                      │
    └──────────────────────────────┘
    """,
    language="text"
)


# ============================================================
# 5. INTELLIGENT SEARCH EXAMPLE
# ============================================================

st.subheader("Example")

st.markdown(
    """
    **User query:**

    > I need to verify a housing case.

    **GPT-4o mini identifies:**

    - Department: `HIS`
    - Page: `Housing Case`
    - Action: `VERIFY`
    - Access Level: `STANDARD`

    **Python searches `roles.csv`** using these attributes.

    The application may return:

    > `BEACON_HIS_VERIFIER`

    The role shown is a  role created specifically
    for this application.
    """
)


# ============================================================
# 6. VIP ACCESS
# ============================================================

st.subheader("VIP Access Handling")

st.write(
    """
    The Intelligent Search function also supports a 
    VIP access level for scenarios involving more confidential
    information.
    """
)

st.markdown(
    """
    When a user requests VIP-level access:

    1. GPT-4o mini identifies the request as `VIP`.
    2. Python searches the role dataset.
    3. Relevant  VIP roles are displayed.
    4. The application displays a warning reminding the user
       to clear the access request with their supervisor.
    """
)

st.warning(
    """
    The application does not grant or approve VIP access.
    It only identifies a potentially relevant  role.
    Actual authorisation would remain with the appropriate
    organisational approval process.
    """
)


# ============================================================
# 7. AI IMPLEMENTATION
# ============================================================

st.header("4. AI Implementation")

st.write(
    """
    GPT-4o mini is primarily used for **natural-language
    understanding**, rather than as the source of truth for
    role or troubleshooting information.
    """
)

st.markdown(
    """
    The application follows a structured approach:

    **Step 1 — User input**

    The user submits a natural-language request.

    **Step 2 — Prompt processing**

    The request is sent to GPT-4o mini together with
    instructions describing the expected output.

    **Step 3 — Structured output**

    The AI returns structured information in JSON format.

    **Step 4 — Application logic**

    Python parses the JSON and uses the identified fields
    to search the relevant dataset.

    **Step 5 — Response**

    The matching information is presented through Streamlit.
    """
)


st.subheader("Example Structured Output")

st.code(
    """
{
    "department": "HIS",
    "page": "Housing Case",
    "action": "VERIFY",
    "access_level": "STANDARD"
}
    """,
    language="json"
)


# ============================================================
# 8. DATA PROCESSING
# ============================================================

st.header("5. Data Processing")

st.write(
    """
    The application uses two separate CSV datasets because
    the two use cases require different types of information.
    """
)

st.markdown(
    """
    ### `roles.csv`

    Used by Intelligent Search to identify potentially
    relevant roles based on:

    - Department
    - Page
    - Action
    - Access level


    ### `troubleshooting.csv`

    Used by Chat Assistant to retrieve:

    - Possible causes
    - Recommended actions
    - Department
    - Page
    - Troubleshooting scenarios
    """
)


# ============================================================
# 9. ERROR HANDLING
# ============================================================

st.header("6. Error Handling")

st.write(
    """
    The application includes basic handling for situations
    where the AI response cannot be interpreted or where no
    matching information exists in the datasets.
    """
)

st.markdown(
    """
    **Invalid AI response**

    If the AI response cannot be parsed as JSON, the
    application falls back to an `UNKNOWN` classification.

    **No matching role**

    If Intelligent Search cannot find a suitable role, the
    application informs the user that no matching role was
    found.

    **No troubleshooting scenario**

    If Chat Assistant cannot find a relevant scenario, the
    application recommends contacting the BEACON team.

    **Out-of-scope query**

    If a question is clearly unrelated to BEACON access,
    the Chat Assistant informs the user that the question
    is outside its intended scope.
    """
)


# ============================================================
# 10. LIMITATIONS
# ============================================================

st.header("7. Methodology Limitations")

st.markdown(
    """
    As this is a application, the methodology has several
    limitations:

    - The datasets contain  information.
    - The application does not connect to real BEACON systems.
    - AI interpretation may not always be completely accurate.
    - Role recommendations are based only on the dataset.
    - The application does not verify a user's actual identity
      or existing permissions.
    - The application does not perform real access provisioning.
    """
)


# ============================================================
# 11. SUMMARY
# ============================================================

st.header("8. Summary")

st.write(
    """
    The BEACON AI Access Assistant demonstrates how a
    natural-language AI interface can be combined with
    structured application logic and datasets to support
    access-related tasks.

    GPT-4o mini provides the natural-language interpretation,
    while Python and the structured datasets remain responsible
    for retrieving and presenting the relevant information.

    This separation allows the application to demonstrate
    practical AI functionality while keeping the underlying
    access information controlled and transparent.
    """
)