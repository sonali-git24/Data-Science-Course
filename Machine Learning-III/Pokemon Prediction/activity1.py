
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Pokemon Data.csv')

print(data.head())

# Handle missing values
data['Type 2'] = data['Type 2'].fillna('None')
print(data.isnull().sum())

# Data visualization
data['Type 1'].value_counts().plot.bar()
plt.show()

data['Type 2'].value_counts().plot.bar()
plt.show()

data['Legendary'].value_counts().plot.bar()
plt.show()

# Check unique values
print(data['Type 1'].unique())
print(data['Type 2'].unique())

# Convert Legendary into numbers
from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
data['Legendary'] = lb.fit_transform(data['Legendary'])

print(data.head())

# Remove Name column
data.drop('Name', axis=1, inplace=True)

# Convert categorical columns into numerical columns
data = pd.get_dummies(data)

print(data.shape)

# Separate input and output
X = data.drop('Legendary', axis=1)
y = data['Legendary']

# Split the dataset
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

clf_model = DecisionTreeClassifier(random_state=42)

# Train the model
clf_model.fit(X_train, y_train)

# Make predictions
y_predict = clf_model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_predict)

print("Decision Tree Accuracy:", accuracy * 100, "%")
