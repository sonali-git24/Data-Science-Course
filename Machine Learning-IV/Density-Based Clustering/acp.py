
# STEP 1: Download Dataset from Google Drive
import gdown
file_id = '1ag2MiU_ywub_0u8grlJZPTLovlSfWoLK'
url = f'https://drive.google.com/uc?id={file_id}'

gdown.download(url, 'customers.csv', quiet=False)


# STEP 2: Import Necessary Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

import warnings
warnings.filterwarnings('ignore')


# STEP 3: Load Dataset

df = pd.read_csv('customers.csv')

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


# STEP 5: Handling Missing Values

# Fill numerical columns with median values
for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].median())

# Fill categorical columns with mode values
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing Values After Treatment:")
print(df.isnull().sum())


# STEP 6: Data Preprocessing

# Select numerical columns
numeric_df = df.select_dtypes(include=np.number).copy()

# Remove ID columns if present
id_columns = [
    col for col in numeric_df.columns
    if 'id' in col.lower()
]

numeric_df = numeric_df.drop(columns=id_columns)

# Remove constant columns
numeric_df = numeric_df.loc[
    :, numeric_df.nunique() > 1
]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(numeric_df)

print("\nPreprocessing Completed!")
print("Features Used:")
print(numeric_df.columns.tolist())


# STEP 7: Implement DBSCAN Clustering

dbscan = DBSCAN(
    eps=0.5,
    min_samples=5
)

df['Cluster'] = dbscan.fit_predict(X_scaled)

print("\nDataset with Cluster Labels:")
print(df.head())


# STEP 8: Find Unique Clusters

unique_clusters = np.unique(df['Cluster'])

print("\nUnique Clusters:")
print(unique_clusters)

print("\nTotal Number of Clusters:",
      len(unique_clusters) - (1 if -1 in unique_clusters else 0))

print("\nNumber of Noise Points:",
      (df['Cluster'] == -1).sum())

print("\nNumber of Customers in Each Cluster:")
print(df['Cluster'].value_counts().sort_index())


# STEP 9: Select Features for Visualization

# Use common Mall Customers dataset columns if available
lower_columns = {
    col.lower(): col for col in numeric_df.columns
}

if ('annual income (k$)' in lower_columns and
    'spending score (1-100)' in lower_columns):

    x_col = lower_columns['annual income (k$)']
    y_col = lower_columns['spending score (1-100)']

else:
    x_col = numeric_df.columns[0]
    y_col = numeric_df.columns[1]

print("\nX-axis:", x_col)
print("Y-axis:", y_col)


# STEP 10: Visualize the Clusters

plt.figure(figsize=(10, 6))

sns.scatterplot(
    x=df[x_col],
    y=df[y_col],
    hue=df['Cluster'],
    palette='viridis',
    s=80
)

plt.title('DBSCAN Customer Clustering')
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.legend(title='Cluster')
plt.show()


# STEP 11: Save the Clustered Dataset

df.to_csv('customer_dbscan_clusters.csv', index=False)

print("\nClustered dataset saved successfully!")
