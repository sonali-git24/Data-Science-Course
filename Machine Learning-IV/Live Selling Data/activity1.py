# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')



df = pd.read_csv('Live.csv')

# Exploratory data analysis
df.shape
df.head()
df.info()
df.isnull().sum()

# Drop redundant columns
df.drop(['Column1', 'Column2', 'Column3', 'Column4'], axis=1, inplace=True)

df.info()
df.describe()

# Explore categorical variables
df['status_id'].unique()
len(df['status_id'].unique())

df['status_published'].unique()
len(df['status_published'].unique())

df['status_type'].unique()
len(df['status_type'].unique())

# Drop unnecessary columns
df.drop(['status_id', 'status_published'], axis=1, inplace=True)

df.info()
df.head()

# Declare feature vector and target variable
X = df.copy()
y = df['status_type']

# Convert categorical variable into integers
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
X['status_type'] = le.fit_transform(X['status_type'])
y = le.transform(y)

X.info()
X.head()

# Feature scaling
cols = X.columns

from sklearn.preprocessing import MinMaxScaler

ms = MinMaxScaler()
X = ms.fit_transform(X)
X = pd.DataFrame(X, columns=cols)

X.head()

# K-Means model with two clusters
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)

# Cluster centers
kmeans.cluster_centers_

# Check classification accuracy
labels = kmeans.labels_

correct_labels = sum(y == labels)

print("Result: %d out of %d samples were correctly labeled." % 
      (correct_labels, y.size))

print('Accuracy score: {0:0.2f}'.format(
    correct_labels / float(y.size)
))

# Elbow method
cs = []

for i in range(1, 11):
    kmeans = KMeans(
        n_clusters=i,
        init='k-means++',
        max_iter=300,
        n_init=10,
        random_state=0
    )
    kmeans.fit(X)
    cs.append(kmeans.inertia_)

plt.plot(range(1, 11), cs)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('CS')
plt.show()

# Final K-Means model
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)

labels = kmeans.labels_

correct_labels = sum(y == labels)

print("Result: %d out of %d samples were correctly labeled." % 
      (correct_labels, y.size))

print('Accuracy score: {0:0.2f}'.format(
    correct_labels / float(y.size)
))