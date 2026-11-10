import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Iris Data.csv')
data.head()

# Check dataset information
data.info()

# Check number of rows and columns
print(data.shape)

# Check missing values
print(data.isnull().sum())

# Statistical information
data.describe()

data = data.dropna()

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Separate the target column
y = data.pop('species')

# Convert species names into numbers
le = LabelEncoder()
y = le.fit_transform(y)

# Remaining columns are input features
X = data

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

error_rates = []

for k in range(1, 40):

    knn = KNeighborsClassifier(n_neighbors=k)

    knn.fit(X_train, y_train)

    preds = knn.predict(X_test)

    error_rates.append(np.mean(y_test != preds))

# Calculate accuracy
accuracy = accuracy_score(y_test, preds)

print("Model Accuracy:", accuracy * 100, "%")
plt.figure(figsize=(10, 7))

plt.plot(
    range(1, 40),
    error_rates,
    color='blue',
    linestyle='dashed',
    marker='o',
    markerfacecolor='red',
    markersize=10
)

plt.title('Error Rate vs. K Value')
plt.xlabel('K Value')
plt.ylabel('Error Rate')

plt.show()
best_k = error_rates.index(min(error_rates)) + 1

print("Best K Value:", best_k)
print("Minimum Error Rate:", min(error_rates))
