import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# 1. Load the historical library records
df = pd.read_csv('library_records.csv')

# 2. Separate features (X) from the target outcome (y)
X = df[['user_type', 'books_out', 'days_past_due']]
y = df['returned_late']

# 3. Initialize and train the Decision Tree Classifier
# random_state ensures the math results stay consistent every time you run it
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# 4. Prediction Function for the Librarian Dashboard
def predict_delinquency(user_type, books_out, days_past_due):
    # Format the new input data to match the training setup
    new_user = pd.DataFrame([[user_type, books_out, days_past_due]], 
                            columns=['user_type', 'books_out', 'days_past_due'])
    
    # Run the prediction (0 or 1)
    prediction = model.predict(new_user)[0]
    
    print(f"📊 Analyzing active borrow profile...")
    print(f"User Profile -> Type: {'Faculty' if user_type==1 else 'Student'} | Active Loans: {books_out} | Overdue Days: {days_past_due}")
    
    if prediction == 1:
        print("🚨 Prediction: HIGH RISK of delinquency. Action: Trigger automated email alert warning.")
    else:
        print("✅ Prediction: LOW RISK. Action: Standard return window active.")

# --- Test the AI Predictor ---
if __name__ == '__main__':
    # Test Scenario: A student (0) who has 6 books out and is already 3 days past the target date
    predict_delinquency(user_type=0, books_out=6, days_past_due=3)
 
