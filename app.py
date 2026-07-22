import streamlit as st

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Library Return Delinquency Predictor",
    page_icon="📚",
    layout="wide"
)

# ----------------------------
# Home Page
# ----------------------------
st.title("📚 Library Return Delinquency Predictor")

st.markdown("---")

st.header("Welcome!")

st.write("""
This AI-powered system predicts whether a library member is likely to
return a borrowed book late.

The prediction helps librarians take proactive actions such as:

- 📧 Sending reminder emails
- 📱 Sending SMS reminders
""")

st.markdown("---")

st.subheader("Project Workflow")

st.info("""
1️⃣ Enter Member Details

2️⃣ Predict Late Return Risk

3️⃣ View AI Recommendations

4️⃣ Send Reminder Email and/or SMS Notification
""")

st.markdown("---")

st.success("👈 Select **User Details** from the left sidebar to begin.")