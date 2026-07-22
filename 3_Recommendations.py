import streamlit as st

st.set_page_config(page_title="Recommendations", page_icon="💡")

st.title("💡 AI Recommendations")

if "prediction" not in st.session_state:
    st.warning("⚠ Please complete the Prediction page first.")
    st.stop()

prediction = st.session_state["prediction"]
probability = st.session_state["probability"]

st.subheader("Prediction Summary")

if prediction == "Late":

    st.error("🔴 HIGH RISK")
    st.metric("Late Return Probability", f"{probability:.1f}%")
    st.progress(int(probability))

    st.markdown("---")

    st.subheader("Recommended Actions")

    st.write("📧 Send Reminder Email")
    st.write("📱 Send SMS Reminder")

    st.info("👉 Open the 'Notification Center' page from the sidebar.")

else:

    st.success("🟢 LOW RISK")
    st.metric("On-Time Return Probability", f"{probability:.1f}%")
    st.progress(int(probability))

    st.markdown("---")

    st.success("🎉 No reminder is required.")

    st.write("The member is likely to return the book on time.")

    st.info("No notification needs to be sent.")