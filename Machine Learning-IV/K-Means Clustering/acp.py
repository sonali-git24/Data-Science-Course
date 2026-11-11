# STEP 1: Download Dataset
import gdown

file_id = '1arBvdOivd6pOyqozTkIkDSLypODJeoZ_'
url = f'https://drive.google.com/uc?id={file_id}'

gdown.download(url, 'College.csv', quiet=False)


# STEP 2: Import Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix, classification_report

from scipy.optimize import linear_sum_assignment

import warnings
warnings.filterwarnings('ignore')


# STEP 3: Load Dataset

df = pd.read_csv('College.csv')

print("First 5 Rows:")
print(df.head())


# STEP 4: Data Exploration

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("\nStatistical Description:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())


# STEP 5: Handling Null Values

# Fill missing numerical values with median
for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].median())

# Fill missing categorical values with mode
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing Values After Treatment:")
print(df.isnull().sum())


# STEP 6: Data Preprocessing

# Remove unnecessary index column if present
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Remove college names if present
if 'Unnamed: 0' in df.columns:
    df.drop('Unnamed: 0', axis=1, inplace=True)

# Convert Private column into numerical values
le = LabelEncoder()
df['Private'] = le.fit_transform(df['Private'])

# Separate actual labels
y = df['Private']

# Select numerical features for clustering
X = df.drop('Private', axis=1)

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\nPreprocessing Completed!")
print("Features Shape:", X_scaled.shape)


# STEP 7: Scatterplot of Grad.Rate vs Room.Board

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x='Grad.Rate',
    y='Room.Board',
    hue='Private',
    palette='Set1'
)

plt.title('Graduation Rate vs Room Board')
plt.xlabel('Graduation Rate')
plt.ylabel('Room Board')
plt.show()


# STEP 8: Scatterplot of F.Undergrad vs Outstate

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x='F.Undergrad',
    y='Outstate',
    hue='Private',
    palette='Set1'
)

plt.title('Full-time Undergraduate Students vs Outstate Tuition')
plt.xlabel('Full-time Undergraduate Students')
plt.ylabel('Outstate Tuition')
plt.show()


# STEP 9: Histogram of Grad.Rate

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x='Grad.Rate',
    bins=20,
    kde=True
)

plt.title('Distribution of Graduation Rate')
plt.xlabel('Graduation Rate')
plt.ylabel('Number of Colleges')
plt.show()


# STEP 10: K-Means Clustering

# Create 2 clusters
kmeans = KMeans(
    n_clusters=2,
    init='k-means++',
    n_init=10,
    max_iter=300,
    random_state=42
)

cluster_labels = kmeans.fit_predict(X_scaled)

# Add cluster labels to dataset
df['Cluster'] = cluster_labels

print("\nClustered Dataset:")
print(df.head())

print("\nNumber of Colleges in Each Cluster:")
print(df['Cluster'].value_counts())


# STEP 11: Visualize Clusters

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x='Grad.Rate',
    y='Room.Board',
    hue='Cluster',
    palette='Set1',
    s=70
)

plt.title('K-Means Clustering of US Colleges')
plt.xlabel('Graduation Rate')
plt.ylabel('Room Board')
plt.show()


# STEP 12: Create Confusion Matrix

# Match cluster labels with actual labels
cm = confusion_matrix(y, cluster_labels)

# Use Hungarian algorithm to find the best cluster-label mapping
row_ind, col_ind = linear_sum_assignment(-cm)

# Create mapping from cluster number to actual class
cluster_to_class = {
    cluster: actual
    for actual, cluster in zip(row_ind, col_ind)
}

# Convert cluster numbers into predicted class labels
y_pred = np.array([
    cluster_to_class[cluster]
    for cluster in cluster_labels
])

# Display Confusion Matrix
cm_final = confusion_matrix(y, y_pred)

plt.figure(figsize=(7, 5))

sns.heatmap(
    cm_final,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=le.classes_,
    yticklabels=le.classes_
)

plt.title('Confusion Matrix')
plt.xlabel('Predicted Class')
plt.ylabel('Actual Class')
plt.show()


# STEP 13: Classification Report

print("\nClassification Report:")

print(
    classification_report(
        y,
        y_pred,
        target_names=le.classes_
    )
)


# STEP 14: Final Results

print("\nFinal Cluster Mapping:")
print(cluster_to_class)

print("\nTotal Colleges:", len(df))

print("\nCluster Distribution:")
print(df['Cluster'].value_counts().sort_index())

# Save the final dataset
df.to_csv('US_Colleges_Clustered.csv', index=False)

print("\nClustered dataset saved successfully!")
