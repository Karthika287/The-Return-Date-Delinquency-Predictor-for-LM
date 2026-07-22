import streamlit as st

st.set_page_config(page_title="Notification Center", page_icon="🔔")

st.title("🔔 Notification Center")

if "prediction" not in st.session_state:
    st.warning("⚠ Please complete the Prediction page first.")
    st.stop()

prediction = st.session_state["prediction"]

# If Low Risk, stop here
if prediction != "Late":

    st.success("🟢 This member is predicted to return the book on time.")

    st.info("No email or SMS reminder is required.")

    st.stop()

member_name = st.session_state.get("member_name", "Member")
member_email = st.session_state.get("member_email", "")

# -----------------------------
# EMAIL
# -----------------------------

st.subheader("📧 Reminder Email")

recipient = st.text_input(
    "Recipient",
    value=member_email
)

subject = st.text_input(
    "Subject",
    value="Library Book Return Reminder"
)

email_body = f"""Dear {member_name},

Our AI prediction system predicts that your borrowed library book may be returned after the due date.

Please return or renew your borrowed book before the due date to avoid overdue fines.

Thank you.

Regards,
Library Management
"""

message = st.text_area(
    "Message",
    value=email_body,
    height=180
)

if st.button("📧 Send Reminder Email"):
    st.toast("Email sent successfully! ✅")

st.divider()

# -----------------------------
# SMS
# -----------------------------

st.subheader("📱 SMS Reminder")

sms_message = st.text_area(
    "SMS Message",
    value=f"""Hi {member_name},

Please return or renew your library book before the due date to avoid overdue fines.

- Library Management""",
    height=100
)

if st.button("📱 Send SMS"):
    st.toast("SMS sent successfully! ✅")