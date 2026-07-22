import streamlit as st

st.set_page_config(page_title="User Details", page_icon="👤")

st.title("👤 Member Details")

st.write("Enter the member's borrowing details.")

st.markdown("---")

member_name = st.text_input("Member Name")

member_email = st.text_input(
    "Member Email",
    placeholder="member@gmail.com"
)

user_role = st.selectbox(
    "User Role",
    ["Student", "Faculty", "Public"]
)

book_category = st.selectbox(
    "Book Category",
    [
        "Fiction",
        "Science",
        "History",
        "Novel",
        "Computer",
        "Biography",
        "Arts"
    ]
)

reservation_status = st.selectbox(
    "Reservation Status",
    ["Yes", "No"]
)

borrow_month = st.selectbox(
    "Borrow Month",
    [
        "January","February","March","April",
        "May","June","July","August",
        "September","October","November","December"
    ]
)

loan_duration = st.slider(
    "Loan Duration (Days)",
    7,
    30,
    14
)

previous_late_returns = st.slider(
    "Previous Late Returns",
    0,
    10,
    0
)

borrow_frequency = st.slider(
    "Borrow Frequency (Books per Month)",
    1,
    10,
    5
)

if st.button("Save & Continue"):

    st.session_state["member_name"] = member_name
    st.session_state["member_email"] = member_email
    st.session_state["user_role"] = user_role
    st.session_state["book_category"] = book_category
    st.session_state["reservation_status"] = reservation_status
    st.session_state["borrow_month"] = borrow_month
    st.session_state["loan_duration"] = loan_duration
    st.session_state["previous_late_returns"] = previous_late_returns
    st.session_state["borrow_frequency"] = borrow_frequency

    st.success("Member details saved successfully!")

    st.info("👉 Open the 'Prediction' page from the sidebar.")