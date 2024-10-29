import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Load the dataset
df = pd.read_csv(r"C:\Users\USER\Desktop\datascience\heart.csv")

# Check for missing values
if df.isnull().sum().any():
    print("Warning: Missing values detected in the dataset.")

# Split the data into features and target
X = df.drop('output', axis=1)  # Features
y = df['output']                # Target variable

# Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Save the trained model
with open('heart_disease_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved successfully.")
