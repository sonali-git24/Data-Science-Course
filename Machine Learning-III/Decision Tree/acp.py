
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score


# Read the dataset
data = pd.read_csv('Iris_Data.csv')

# A. Data Exploration
print("First five rows of the dataset:")
print(data.head())

print("\nDataset Information:")
print(data.info())

print("\nDataset Description:")
print(data.describe())

print("\nChecking missing values:")
print(data.isnull().sum())

# Remove unnecessary ID and empty columns, if present
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
data = data.drop(columns=['Id', 'ID'], errors='ignore')

# Identify the target column
target_column = next(
    (col for col in data.columns if col.lower() in ['species', 'class', 'target']),
    data.columns[-1]
)

# Handle missing values
for column in data.columns:
    if data[column].isnull().sum() > 0:
        if data[column].dtype == 'object':
            data[column] = data[column].fillna(data[column].mode()[0])
        else:
            data[column] = data[column].fillna(data[column].median())

# B. Data Preprocessing
# Separate input features and target
X = data.drop(columns=[target_column])
X = X.select_dtypes(include=np.number)

y = data[target_column]

# Convert species names into numbers
le = LabelEncoder()
y = le.fit_transform(y)

print("\nPreprocessed Data:")
print(X.head())

# C. Split Data into Training and Testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# D. Model Building
# Create the Decision Tree classifier
model = DecisionTreeClassifier(criterion='entropy', random_state=42)

# Train the model
model.fit(X_train, y_train)

# Predict the species
predictions = model.predict(X_test)

# Calculate model accuracy
accuracy = accuracy_score(y_test, predictions)

print("\nActual Species:", le.inverse_transform(y_test))
print("Predicted Species:", le.inverse_transform(predictions))

print("\nModel Accuracy:", accuracy * 100, "%")

# Display the Decision Tree
plt.figure(figsize=(15, 8))
plot_tree(
    model,
    feature_names=X.columns,
    class_names=le.classes_,
    filled=True
)
plt.title("Decision Tree Classifier - Iris Dataset")
plt.show()

# E. Conclusion
print("\nConclusion:")
print("The Decision Tree model was successfully trained on the Iris dataset.")
print("The model predicts the species of Iris flowers using their measurements.")
print("The accuracy of the model is:", round(accuracy * 100, 2), "%")

# Comment about the dataset
print("\nDataset Comment:")
print("The Iris dataset contains flower measurements such as sepal length,")
print("sepal width, petal length and petal width.")
print("It is used to classify flowers into Setosa, Versicolor and Virginica.")
