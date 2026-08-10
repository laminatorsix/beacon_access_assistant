import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def interpret_search_query(query):

    prompt = f"""
You are helping users search the BEACON platform.

BEACON has three departments:

- AAD = Accounts Accumulation Department
- HIS = Housing and Investment Systems
- RDD = Retirement Decumulation Department

The platform contains different pages and functions.

Possible access levels:
- STANDARD
- VIP
- UNKNOWN

Analyse the user's request and identify:

1. department
2. page
3. action
4. access_level

Use these rules:

Department:
- If the request concerns accounts or contributions, use AAD.
- If the request concerns housing, HPS, or investments, use HIS.
- If the request concerns retirement, payouts, or retirement claims, use RDD.

Access level:
- Use VIP if the user explicitly mentions confidential,
  sensitive, restricted, or VIP information.
- Otherwise use STANDARD.
- Use UNKNOWN only when the access level genuinely cannot
  be determined.

Action:
- Use VIEW when the user wants to view, check, see, or enquire. This corresponds to VIEWER role.
- Use PREPARE when the user wants to prepare, create, or update. This corresponds to PREPARER role.
- Use VERIFY when the user wants to verify, review, or approve. This corresponds to VERIFIER role.
- Use UNKNOWN if the action cannot be determined.

Page:
Identify the base BEACON page involved in the request.

Use simple page names such as:
- Account Enquiry
- Contribution Enquiry
- Transaction Enquiry
- HPS Enquiry
- HPS Claims
- Housing Enquiry
- Housing Case
- Investment Enquiry
- Retirement Enquiry
- Payout Enquiry
- Claims
- Retirement Case

Do not include the action in the page name.
For example, return "Housing Case", not
"Housing Case Verification".

Return ONLY valid JSON in exactly this format:

{{
    "department": "HIS",
    "page": "HPS Enquiry",
    "action": "VIEW",
    "access_level": "STANDARD"
}}

User request:
{query}
"""

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    result = response.output_text.strip()

    # Remove Markdown code fences
    if result.startswith("```"):
        result = result.replace("```json", "")
        result = result.replace("```", "")
        result = result.strip()

    try:
        return json.loads(result)

    except json.JSONDecodeError:
        print("Could not parse AI response as JSON.")

        return {
            "department": "UNKNOWN",
            "page": "UNKNOWN",
            "action": "UNKNOWN",
            "access_level": "UNKNOWN"
        }

def interpret_troubleshooting_query(query):

    prompt = f"""
You are an access troubleshooting assistant for the
BEACON platform.

Your job is to identify whether a user's question is related
to accessing or using the BEACON platform.

BEACON has three business departments:

- AAD = Accounts Accumulation Department
- HIS = Housing and Investment Systems
- RDD = Retirement Decumulation Department

There is also:
- GENERAL = Platform-wide issues

IMPORTANT:
Any question about BEACON access, permissions, pages,
screens, roles, applications, errors, or availability
should be considered a BEACON access issue.

Examples of BEACON access issues:

"I can't view HPS coverage"
"I cannot verify a housing case"
"Why can't I access the HPS claims screen?"
"I applied for access but still can't see the screen"
"Why am I getting connection refused?"
"Why is BEACON unavailable?"
"BEACON is not working"
"Why can't I log in to BEACON?"
"Why is the BEACON page blank?"
"BEACON is inaccessible during certain hours"

These should all have:

"is_beacon_access_issue": true

Only set is_beacon_access_issue to false when the
question is clearly unrelated to BEACON.

For example:

"Why is my computer slow?"
"What is the weather today?"
"How do I cook pasta?"

These should have:

"is_beacon_access_issue": false

Identify:

1. is_beacon_access_issue
2. department
3. page
4. action
5. issue

Department:
- AAD for accounts, contributions or transactions
- HIS for housing, HPS or investments
- RDD for retirement, payouts or claims
- GENERAL for platform-wide issues
- UNKNOWN if genuinely unclear

Page:
Use the base page name only.

Examples:
- Account Enquiry
- Contribution Enquiry
- Transaction Enquiry
- HPS Enquiry
- HPS Claims
- Housing Enquiry
- Housing Case
- Investment Enquiry
- Retirement Enquiry
- Payout Enquiry
- Claims
- Retirement Case
- UNKNOWN for general platform issues

Do not include the action in the page name.

Action:
- VIEW = view, see, check, enquire
- PREPARE = create, prepare, update, submit
- VERIFY = verify, review, approve
- UNKNOWN if unclear

For general platform issues, action should usually be UNKNOWN.

Return ONLY valid JSON.

Example 1:

{{
    "is_beacon_access_issue": true,
    "department": "HIS",
    "page": "HPS Enquiry",
    "action": "VIEW",
    "issue": "Cannot view HPS coverage"
}}

Example 2:

{{
    "is_beacon_access_issue": true,
    "department": "HIS",
    "page": "Housing Case",
    "action": "VERIFY",
    "issue": "Cannot verify a housing case"
}}

Example 3:

{{
    "is_beacon_access_issue": true,
    "department": "GENERAL",
    "page": "UNKNOWN",
    "action": "UNKNOWN",
    "issue": "Connection refused"
}}

Example 4:

{{
    "is_beacon_access_issue": false,
    "department": "UNKNOWN",
    "page": "UNKNOWN",
    "action": "UNKNOWN",
    "issue": "Computer is slow"
}}

User question:
{query}
"""

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    result = response.output_text.strip()

    # Remove Markdown code fences
    if result.startswith("```"):
        result = result.replace("```json", "")
        result = result.replace("```", "")
        result = result.strip()

    try:
        return json.loads(result)

    except json.JSONDecodeError:

        print("Could not parse troubleshooting response.")

        return {
            "is_beacon_access_issue": False,
            "department": "UNKNOWN",
            "page": "UNKNOWN",
            "action": "UNKNOWN",
            "issue": "UNKNOWN"
        }