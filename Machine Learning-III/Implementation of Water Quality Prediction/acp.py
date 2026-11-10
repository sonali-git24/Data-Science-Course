
# Water Potability Prediction using Machine Learning

# Step 1: Import necessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, f1_score

# Step 2: Upload the dataset

uploaded = files.upload()

# Step 3: Read the dataset

file_name = list(uploaded.keys())[0]
df = pd.read_csv(file_name)

print("First Five Rows of Dataset:")
print(df.head())

# Step 4: Data Exploration

print("\nDataset Information:")
print(df.info())

print("\nDataset Shape:")
print(df.shape)

print("\nStatistical Description:")
print(df.describe())

# Step 5: Check Missing Values

print("\nMissing Values:")
print(df.isnull().sum())

# Step 6: Separate Features and Target

X = df.drop('Potability', axis=1)
y = df['Potability']

# Step 7: Split Data into Training and Testing

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

# Step 8: Create Four Machine Learning Models

models = {
    "Logistic Regression": Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler()),
        ('model', LogisticRegression(max_iter=2000))
    ]),

    "KNN Classifier": Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler()),
        ('model', KNeighborsClassifier(n_neighbors=5))
    ]),

    "Decision Tree": Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('model', DecisionTreeClassifier(random_state=42))
    ]),

    "Random Forest": Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('model', RandomForestClassifier(
            n_estimators=100,
            random_state=42
        ))
    ])
}

# Step 9: Train Models and Calculate Accuracy

results = []

for name, model in models.items():

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Calculate F1 score
    f1 = f1_score(y_test, y_pred, zero_division=0)

    results.append({
        'Algorithm': name,
        'Accuracy': round(accuracy * 100, 2),
        'F1 Score': round(f1, 3)
    })

    print("\nModel:", name)
    print("Accuracy:", round(accuracy * 100, 2), "%")
    print("F1 Score:", round(f1, 3))

# Step 10: Compare All Models

comparison = pd.DataFrame(results)

print("\nMODEL COMPARISON:")
print(comparison.sort_values(
    by='Accuracy', ascending=False
).to_string(index=False))

# Step 11: Find the Best Performing Model

best_model = comparison.loc[
    comparison['Accuracy'].idxmax()
]

print("\nBEST PERFORMING ALGORITHM:")
print("Algorithm:", best_model['Algorithm'])
print("Accuracy:", best_model['Accuracy'], "%")

# Step 12: Visualize Model Accuracy

plt.figure(figsize=(9, 5))

sns.barplot(
    data=comparison,
    x='Algorithm',
    y='Accuracy'
)

plt.title("Comparison of Machine Learning Models")
plt.xlabel("Classification Algorithms")
plt.ylabel("Accuracy (%)")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# Step 13: Conclusion

print("\nCONCLUSION")
print("------------------------------------")

print("Four classification algorithms were implemented.")
print("Their accuracy scores were calculated and compared.")

print("The best performing model is:",
      best_model['Algorithm'])

print("Its testing accuracy is:",
      best_model['Accuracy'], "%")

print("\nThe model predicts whether water is")
print("potable (safe for drinking) or not potable.")
