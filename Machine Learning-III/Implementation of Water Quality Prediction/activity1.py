import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('water_potability.csv')
df.head()

df.shape

df.isnull().sum()

df.info()

df.describe()

df.fillna(df.mean(), inplace=True)
df.isnull().sum()

df.Potability.value_counts()

sns.countplot(df['Potability'])
plt.show()

sns.distplot(df['ph'])
plt.show()

df.hist(figsize=(14,14))
plt.show()

plt.figure(figsize=(13,8))
sns.heatmap(df.corr(), annot=True, cmap='terrain')
plt.show()

df.boxplot(figsize=(14,7))

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=101, shuffle=True)

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
dt=DecisionTreeClassifier(criterion='gini', min_samples_split=10, splitter='best')
dt.fit(X_train,Y_train)

prediction=dt.predict(X_test)
print(f"Accuracy Score = {accuracy_score(Y_test,prediction)*100}")
print(f"Confusion Matrix =\n {confusion_matrix(Y_test,prediction)}")
print(f"Classification Report =\n {classification_report(Y_test,prediction)}")

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 10)
print(knn.fit(X_train, Y_train))

prediction=knn.predict(X_test)
print(f"Accuracy Score = {accuracy_score(Y_test, prediction)*100}")
print(f"Confusion Matrix =\n {confusion_matrix(Y_test, prediction)}")
print(f"Classification Report =\n {classification_report(Y_test, prediction)}")

from sklearn.linear_model import LogisticRegression
log = LogisticRegression(random_state = 0)
print(log.fit(X_train, Y_train))

prediction=log.predict(X_test)
print(f"Accuracy Score = {accuracy_score(Y_test,prediction)*100}")
print(f"Confusion Matrix =\n {confusion_matrix(Y_test,prediction)}")
print(f"Classification Report =\n {classification_report(Y_test,prediction)}")