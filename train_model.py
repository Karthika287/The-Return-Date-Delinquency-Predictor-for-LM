from preprocess import load_data
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# Load preprocessed data
X_train, X_test, y_train, y_test, encoders = load_data()

# Create model
model = RandomForestClassifier(random_state=42)

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Create models folder if it doesn't exist
os.makedirs("models", exist_ok=True)

# Save model
joblib.dump(model, "models/library_model.pkl")

# Save encoders
joblib.dump(encoders, "models/encoders.pkl")

print("\nModel saved successfully!")