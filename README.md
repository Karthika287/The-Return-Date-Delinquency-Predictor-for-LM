# AI-Powered Book Recommender Engine for LMS 📚

A minimalist, high-performance Machine Learning feature designed for a **Library Management System (LMS)**. This system automatically analyzes book descriptions using natural language processing (NLP) and suggests relevant books to users based on their reading patterns.

## 🚀 Features
* **Content-Based Filtering:** Analyzes the actual plot, genre, and keywords of book descriptions.
* **TF-IDF Vectorization:** Converts raw text strings into numerical matrices by evaluating word importance and removing common filler words.
* **Cosine Similarity:** Uses mathematical dot-products to instantly rank and find the closest matching books in the database.
* **Lightweight & Flat Design:** No bulky frameworks or databases required—runs purely using a local CSV file.

## 📁 Repository Structure
```text
library-lms-ai/
├── books.csv           # The library's book database (Title & Plot Description)
├── recommender.py      # Core Machine Learning engine and recommendation logic
└── requirements.txt    # List of mandatory Python library dependencies
