import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as sns  

 

data = pd.read_csv('sample_data.csv')  
data.head()

from sklearn.model_selection import train_test_split

y = data.pop('TARGET CLASS')
X = data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.tree import DecisionTreeClassifier
clf_model = DecisionTreeClassifier()
clf_model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score
y_predict = clf_model.predict(X_test)
accuracy_score(y_test, y_predict)