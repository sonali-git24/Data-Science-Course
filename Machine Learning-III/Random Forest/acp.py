
# Airline Passenger Satisfaction Prediction
# Using Random Forest Classifier

# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# Step 2: Upload the dataset
uploaded = files.upload()

# Step 3: Read the dataset
file_name = list(uploaded.keys())[0]
df = pd.read_csv(file_name)

print("First Five Rows:")
print(df.head())

# Step 4: Data Exploration
print("\nDataset Information:")
print(df.info())

print("\nDataset Shape:")
print(df.shape)

print("\nStatistical Description:")
print(df.describe())

# Step 5: Check and handle missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove unnecessary columns
df.drop(columns=['id', 'Unnamed: 0'],
        errors='ignore', inplace=True)

# Separate features and target
X = df.drop('satisfaction', axis=1)
y = df['satisfaction']

# Identify numerical and categorical columns
numerical_columns = X.select_dtypes(
    include=['int64', 'float64']
).columns

categorical_columns = X.select_dtypes(
    include=['object', 'category']
).columns

# Step 6: Data Preprocessing
numeric_transformer = SimpleImputer(strategy='median')

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', numeric_transformer, numerical_columns),
    ('cat', categorical_transformer, categorical_columns)
])

# Step 7: Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Data:", X_train.shape)
print("Testing Data:", X_test.shape)

# Step 8: Build Random Forest Classifier
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    ))
])

# Step 9: Train the model
model.fit(X_train, y_train)

print("\nModel Training Completed Successfully!")

# Step 10: Make predictions
y_pred = model.predict(X_test)

print("\nPredicted Passenger Satisfaction:")
print(y_pred[:10])

# Step 11: Calculate accuracy
train_accuracy = accuracy_score(
    y_train, model.predict(X_train)
)

test_accuracy = accuracy_score(y_test, y_pred)

print("\nTraining Accuracy:",
      round(train_accuracy * 100, 2), "%")

print("Testing Accuracy:",
      round(test_accuracy * 100, 2), "%")

# Step 12: Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Step 13: Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')

plt.xlabel("Predicted Values")
plt.ylabel("Actual Values")
plt.title("Passenger Satisfaction Confusion Matrix")
plt.show()

# Step 14: Conclusion
print("\nCONCLUSION")
print("--------------------------------")
print("Random Forest Classifier was used")
print("to predict airline passenger satisfaction.")
print("Testing Accuracy:",
      round(test_accuracy * 100, 2), "%")

print("The model predicts whether passengers")
print("are satisfied or neutral/dissatisfied.")
