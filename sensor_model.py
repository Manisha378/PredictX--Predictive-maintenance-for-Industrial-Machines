import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
df = pd.read_csv("predictive___maintenance.csv")

# Drop unnecessary columns
df = df.drop(["UDI", "Product ID", "Failure Type"], axis=1)

# Encode categorical column 'Type'
df["Type"] = df["Type"].map({"L": 0, "M": 1, "H": 2})

# Define features and target
X = df.drop("Target", axis=1)
y = df["Target"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")

# Save the model
joblib.dump(model, "maintenance_model.pkl")
print("✅ Model saved as 'maintenance_model.pkl'")