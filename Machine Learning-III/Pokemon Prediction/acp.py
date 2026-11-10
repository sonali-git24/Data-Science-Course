
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
data = pd.read_csv('Airline Data.csv')

# A. Data Exploration
print("First five rows:")
print(data.head())

print("\nDataset Information:")
print(data.info())

print("\nDataset Description:")
print(data.describe())

print("\nMissing Values:")
print(data.isnull().sum())

print("\nDataset Shape:")
print(data.shape)

# Remove unnecessary ID columns, if present
data.drop(columns=['Unnamed: 0', 'id'], errors='ignore', inplace=True)

# Handle missing values
for column in data.columns:
    if data[column].isnull().sum() > 0:
        if data[column].dtype == 'object':
            data[column] = data[column].fillna(data[column].mode()[0])
        else:
            data[column] = data[column].fillna(data[column].median())

print("\nMissing Values After Handling:")
print(data.isnull().sum())

# Display satisfaction count
data['satisfaction'].value_counts().plot.bar()
plt.title("Passenger Satisfaction")
plt.xlabel("Satisfaction")
plt.ylabel("Count")
plt.show()

# B. Data Preprocessing

# Separate input and output
X = data.drop('satisfaction', axis=1)
y = data['satisfaction']

# Convert categorical columns into numerical columns
X = pd.get_dummies(X, drop_first=True)

# Convert target values into numbers
from sklearn.preprocessing import LabelEncoder

lb = LabelEncoder()
y = lb.fit_transform(y)

print("\nPreprocessed Data:")
print(X.head())

# C. Split Data into Training and Testing
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale the data for Logistic Regression and KNN
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train_scaled = sc.fit_transform(X_train)
X_test_scaled = sc.transform(X_test)

# D. Model Building

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. Logistic Regression
LogReg = LogisticRegression(max_iter=1000)

LogReg.fit(X_train_scaled, y_train)

ypred1 = LogReg.predict(X_test_scaled)

accuracy1 = accuracy_score(y_test, ypred1)

print("\nLogistic Regression Accuracy:", accuracy1 * 100, "%")

# 2. KNN Classifier
knn_model = KNeighborsClassifier(n_neighbors=5)

knn_model.fit(X_train_scaled, y_train)

ypred2 = knn_model.predict(X_test_scaled)

accuracy2 = accuracy_score(y_test, ypred2)

print("\nKNN Accuracy:", accuracy2 * 100, "%")

# 3. Decision Tree Classifier
clf_model = DecisionTreeClassifier(random_state=42)

clf_model.fit(X_train, y_train)

ypred3 = clf_model.predict(X_test)

accuracy3 = accuracy_score(y_test, ypred3)

print("\nDecision Tree Accuracy:", accuracy3 * 100, "%")

# Compare all three models
print("\nModel Accuracy Comparison:")
print("Logistic Regression:", round(accuracy1 * 100, 2), "%")
print("KNN:", round(accuracy2 * 100, 2), "%")
print("Decision Tree:", round(accuracy3 * 100, 2), "%")

# Display accuracy graph
models = ['Logistic Regression', 'KNN', 'Decision Tree']
accuracies = [accuracy1 * 100, accuracy2 * 100, accuracy3 * 100]

plt.figure(figsize=(8, 5))
plt.bar(models, accuracies)
plt.title("Accuracy Comparison of Machine Learning Models")
plt.xlabel("Models")
plt.ylabel("Accuracy (%)")
plt.ylim(0, 100)
plt.show()

# E. Conclusion
best_model = models[np.argmax(accuracies)]

print("\nConclusion:")
print("All three machine learning models were successfully trained.")
print("The models predict whether an airline passenger is satisfied.")
print("The best-performing model is:", best_model)
print("Its accuracy is:", round(max(accuracies) * 100, 2), "%")

# Comment about the dataset
print("\nDataset Comment:")
print("The airline dataset contains passenger details and their travel")
print("experiences, such as age, flight distance, seat comfort,")
print("in-flight services and delays.")
print("The satisfaction column indicates whether passengers are satisfied")
print("or dissatisfied with the airline services.")
