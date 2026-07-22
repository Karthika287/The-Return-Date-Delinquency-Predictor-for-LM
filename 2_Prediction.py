import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Prediction", page_icon="🤖")

st.title("🤖 Prediction")

# Check whether user details are available
if "user_role" not in st.session_state:
    st.warning("⚠ Please complete the User Details page first.")
    st.stop()

# Load model and encoders
model = joblib.load("models/library_model.pkl")
encoders = joblib.load("models/encoders.pkl")

# Read data from session
user_role = st.session_state["user_role"]
book_category = st.session_state["book_category"]
reservation_status = st.session_state["reservation_status"]
borrow_month = st.session_state["borrow_month"]
loan_duration = st.session_state["loan_duration"]
previous_late_returns = st.session_state["previous_late_returns"]
borrow_frequency = st.session_state["borrow_frequency"]

# Display entered details
st.subheader("Member Details")

st.write("**User Role:**", user_role)
st.write("**Book Category:**", book_category)
st.write("**Reservation Status:**", reservation_status)
st.write("**Borrow Month:**", borrow_month)
st.write("**Loan Duration:**", loan_duration, "Days")
st.write("**Previous Late Returns:**", previous_late_returns)
st.write("**Borrow Frequency:**", borrow_frequency)

st.markdown("---")

if st.button("🔍 Predict"):

    input_data = {
        "user_role": encoders["user_role"].transform([user_role])[0],
        "book_category": encoders["book_category"].transform([book_category])[0],
        "reservation_status": encoders["reservation_status"].transform([reservation_status])[0],
        "borrow_month": encoders["borrow_month"].transform([borrow_month])[0],
        "loan_duration": loan_duration,
        "previous_late_returns": previous_late_returns,
        "borrow_frequency": borrow_frequency
    }

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]

    predicted_label = encoders["overdue_status"].inverse_transform([prediction])[0]

    probability = max(probabilities) * 100

    # Save prediction for next pages
    st.session_state["prediction"] = predicted_label
    st.session_state["probability"] = probability

    st.subheader("Prediction Result")

    if predicted_label == "Late":
        st.error("🔴 HIGH RISK")
        st.metric("Late Return Probability", f"{probability:.1f}%")
    else:
        st.success("🟢 LOW RISK")
        st.metric("On-Time Return Probability", f"{probability:.1f}%")

    st.progress(int(probability))

    st.success("Prediction completed successfully!")

    st.info("👉 Open the 'Recommendations' page from the sidebar.")