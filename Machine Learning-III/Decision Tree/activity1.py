# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

# Create the dataset
data = {
    'Temperature': ['Hot', 'Hot', 'Hot', 'Hot', 'Cold', 'Cold', 'Cold', 'Cold'],
    'Raining': ['No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes'],
    'Windy': ['No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes'],
    'Walk': ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No']
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Convert text values into numbers
le = LabelEncoder()

for column in df.columns:
    df[column] = le.fit_transform(df[column])

# Separate input and output
X = df[['Temperature', 'Raining', 'Windy']]
y = df['Walk']

# Create the Decision Tree model
model = DecisionTreeClassifier(criterion='entropy', random_state=0)

# Train the model
model.fit(X, y)

# Display the Decision Tree
plt.figure(figsize=(12, 8))

tree.plot_tree(
    model,
    feature_names=['Temperature', 'Raining', 'Windy'],
    class_names=['No', 'Yes'],
    filled=True
)

plt.show()

# Predict whether a person will go for a walk
# Temperature = Cold (0), Raining = No (0), Windy = Yes (1)

prediction = model.predict([[0, 0, 1]])

if prediction[0] == 1:
    print("Person will go for a walk!")
else:
    print("Person will not go for a walk!")

# Display model accuracy on the given dataset
accuracy = model.score(X, y)
print("Model Accuracy:", accuracy * 100, "%")