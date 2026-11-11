
# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

from sklearn.cluster import KMeans
from google.colab import files

import warnings
warnings.filterwarnings('ignore')


# Step 1: Upload Dataset
uploaded = files.upload()

df = pd.read_csv('customers.csv', index_col=0)

print("First 5 Records:")
print(df.head())

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("\nStatistical Description:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())


# Step 2: Distribution Plots
plt.figure(figsize=(15, 6))

columns = ['Age', 'Annual Income (k$)',
           'Spending Score (1-100)']

for n, col in enumerate(columns, 1):
    plt.subplot(1, 3, n)
    sns.histplot(df[col], bins=15, kde=True)
    plt.title(f'Distribution of {col}')
    
plt.tight_layout()
plt.show()


# Step 3: Pair Plot
sns.pairplot(
    df,
    vars=['Spending Score (1-100)',
          'Annual Income (k$)', 'Age'],
    hue='Gender'
)
plt.show()


# Step 4: Scatter Plot of Age vs Spending Score
plt.figure(figsize=(15, 7))

plt.title('Age vs Spending Score', fontsize=20)
plt.xlabel('Age')
plt.ylabel('Spending Score (1-100)')

plt.scatter(
    df['Age'],
    df['Spending Score (1-100)'],
    s=100
)

plt.show()


# Step 5: Clustering Based on Age and Spending Score

x1 = df[['Age', 'Spending Score (1-100)']].values

inertia = []

for n in range(1, 15):
    model = KMeans(
        n_clusters=n,
        init='k-means++',
        n_init=10,
        max_iter=300,
        random_state=111
    )
    model.fit(x1)
    inertia.append(model.inertia_)

# Elbow Graph
plt.figure(figsize=(15, 6))
plt.plot(range(1, 15), inertia, 'o-')

plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method - Age and Spending Score')
plt.show()


# Applying KMeans with 4 Clusters
kmeans1 = KMeans(
    n_clusters=4,
    init='k-means++',
    n_init=10,
    max_iter=300,
    random_state=111
)

labels1 = kmeans1.fit_predict(x1)
centroids1 = kmeans1.cluster_centers_


# Plotting Clusters
plt.figure(figsize=(15, 7))

plt.scatter(
    x1[:, 0],
    x1[:, 1],
    c=labels1,
    s=100,
    cmap='Pastel2'
)

plt.scatter(
    centroids1[:, 0],
    centroids1[:, 1],
    s=300,
    c='red',
    alpha=0.5,
    label='Centroids'
)

plt.xlabel('Age')
plt.ylabel('Spending Score (1-100)')
plt.title('Customer Clusters: Age vs Spending Score')
plt.legend()
plt.show()


# Step 6: Clustering Based on Annual Income and Spending Score

x2 = df[['Annual Income (k$)',
         'Spending Score (1-100)']].values

inertia = []

for n in range(1, 11):
    model = KMeans(
        n_clusters=n,
        init='k-means++',
        n_init=10,
        max_iter=300,
        random_state=111
    )
    model.fit(x2)
    inertia.append(model.inertia_)


# Elbow Graph
plt.figure(figsize=(15, 6))

plt.plot(range(1, 11), inertia, 'o-')

plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method - Income and Spending Score')
plt.show()


# Applying KMeans with 5 Clusters
kmeans2 = KMeans(
    n_clusters=5,
    init='k-means++',
    n_init=10,
    max_iter=300,
    random_state=111
)

labels2 = kmeans2.fit_predict(x2)
centroids2 = kmeans2.cluster_centers_


# Plotting Clusters
plt.figure(figsize=(15, 8))

plt.scatter(
    x2[:, 0],
    x2[:, 1],
    c=labels2,
    s=100,
    cmap='Pastel2'
)

plt.scatter(
    centroids2[:, 0],
    centroids2[:, 1],
    s=300,
    c='red',
    alpha=0.5,
    label='Centroids'
)

plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('Customer Clusters: Income vs Spending Score')
plt.legend()
plt.show()


# Step 7: Clustering Based on Three Features

X3 = df[['Age',
         'Annual Income (k$)',
         'Spending Score (1-100)']].values

inertia = []

for n in range(1, 11):
    model = KMeans(
        n_clusters=n,
        init='k-means++',
        n_init=10,
        max_iter=300,
        random_state=111
    )
    model.fit(X3)
    inertia.append(model.inertia_)


# Elbow Graph
plt.figure(figsize=(15, 6))

plt.plot(range(1, 11), inertia, 'o-')

plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method - Three Features')
plt.show()


# Applying KMeans with 6 Clusters
kmeans3 = KMeans(
    n_clusters=6,
    init='k-means++',
    n_init=10,
    max_iter=300,
    random_state=111
)

y_kmeans = kmeans3.fit_predict(X3)

labels3 = kmeans3.labels_
centroids3 = kmeans3.cluster_centers_


# Adding Cluster Labels to Dataset
df['cluster'] = y_kmeans

print("\nCustomer Data with Cluster Labels:")
print(df.head())

print("\nNumber of Customers in Each Cluster:")
print(df['cluster'].value_counts().sort_index())


# Step 8: 3D Cluster Visualization

trace1 = go.Scatter3d(
    x=df['Age'],
    y=df['Spending Score (1-100)'],
    z=df['Annual Income (k$)'],
    mode='markers',
    marker=dict(
        color=df['cluster'],
        colorscale='Viridis',
        size=7,
        line=dict(
            color=df['cluster'],
            width=1
        ),
        opacity=0.8
    )
)

# Centroid Visualization
trace2 = go.Scatter3d(
    x=centroids3[:, 0],
    y=centroids3[:, 2],
    z=centroids3[:, 1],
    mode='markers',
    marker=dict(
        color='red',
        size=10,
        symbol='diamond'
    ),
    name='Centroids'
)

fig = go.Figure(data=[trace1, trace2])

fig.update_layout(
    title='Customer Clusters Based on Age, Income and Spending Score',
    scene=dict(
        xaxis_title='Age',
        yaxis_title='Spending Score',
        zaxis_title='Annual Income'
    )
)

fig.show()


# Step 9: Save Clustered Dataset
df.to_csv('customer_clusters.csv')

print("\nClustered dataset saved successfully!")
