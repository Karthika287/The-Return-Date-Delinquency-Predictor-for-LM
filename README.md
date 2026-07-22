# 📚 Library Return date delinquency Prediction System

## 📌 Overview

The **Library Return Prediction System** is an AI-based application that predicts the probability of a user returning a borrowed book late.

The system uses Machine Learning to analyze borrower details such as previous late returns, borrowing frequency, loan duration, user role, book category, and reservation status to classify users into:

- 🟢 Low Risk
- 🟡 Medium Risk
- 🔴 High Risk

The goal of this system is to help libraries identify possible late returns in advance and improve book management efficiency.

---

# 🎯 Objectives

- Predict the possibility of late book returns.
- Reduce delays in book circulation.
- Help librarians manage high-risk borrowers.
- Provide quick risk analysis through an easy-to-use interface.
- Demonstrate the use of Machine Learning in library management.

---

# ✨ Features

## 👤 Member Details Input

Users can provide:

- User Role
- Book Category
- Reservation Status
- Borrow Month
- Loan Duration
- Previous Late Returns
- Borrow Frequency

---

## 🤖 AI-Based Prediction

The system processes user details using a trained Machine Learning model and predicts:

- Risk Category
- Late Return Probability
- Prediction confidence

---

## 📊 Risk Classification

### 🟢 Low Risk
Users who usually return books on time.

Example:
- Previous late returns: 0-1
- High borrowing frequency
- Normal loan duration

---

### 🟡 Medium Risk
Users with occasional delays.

Example:
- Previous late returns: 2-3
- Longer loan duration
- Moderate borrowing frequency

---

### 🔴 High Risk
Users with a higher possibility of late return.

Example:
- Multiple previous late returns
- Long loan duration
- Low borrowing frequency

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Machine Learning

- Scikit-learn
- Pandas
- NumPy

## Frontend

- Streamlit

## Model

- Classification Algorithm
  - Random Forest Classifier

## Data Processing

- Label Encoding
- Feature Selection
- Data Cleaning

---

# 📂 Project Structure

