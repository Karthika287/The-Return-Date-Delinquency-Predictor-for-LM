import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def load_data():
    # Load dataset
    df = pd.read_csv("data/library_return_prediction_dataset_1000.csv")

    # Create label encoders
    encoders = {}

    # Encode categorical columns
    categorical_columns = [
        "user_role",
        "book_category",
        "reservation_status",
        "borrow_month",
        "overdue_status"
    ]

    for col in categorical_columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le

    # Features
    X = df.drop("overdue_status", axis=1)

    # Target
    y = df["overdue_status"]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    return X_train, X_test, y_train, y_test, encoders