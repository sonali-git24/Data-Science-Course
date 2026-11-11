
# =====================================================
# K-MEANS CLUSTERING ON LIVE SELLING DATASET
# =====================================================

# 1. Import necessary libraries

import gdown
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

import warnings
warnings.filterwarnings('ignore')


# 2. Import the dataset from Google Drive

file_id = "1hHdZ6YeYzSHRjescvLxaeZyp4sTo7lUp"
url = f"https://drive.google.com/uc?id={file_id}"

gdown.download(url, "Live.csv", quiet=False)

df = pd.read_csv("Live.csv")


# 3. Data Exploration

print("\nFIRST FIVE ROWS:")
print(df.head())

print("\nDATASET SHAPE:")
print(df.shape)

print("\nCOLUMN NAMES:")
print(df.columns)

print("\nDATASET INFORMATION:")
df.info()

print("\nSTATISTICAL DESCRIPTION:")
print(df.describe())

print("\nMISSING VALUES:")
print(df.isnull().sum())


# 4. Visualize missing values

plt.figure(figsize=(10, 5))
sns.heatmap(df.isnull(), cbar=False)
plt.title("Missing Values")
plt.show()


# 5. Handle missing values

for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include='object').columns:
    if df[col].isnull().any() and not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])


# 6. Remove duplicate records

df.drop_duplicates(inplace=True)

print("\nDATASET AFTER CLEANING:")
print(df.shape)


# 7. Data Preprocessing

# Remove ID, date, time and URL columns
drop_cols = [
    col for col in df.columns
    if any(word in col.lower()
           for word in ['id', 'date', 'time', 'url'])
]

data = df.drop(columns=drop_cols, errors='ignore')

# Select numerical features
numeric_data = data.select_dtypes(include=np.number)

# Select categorical features with limited unique values
categorical_data = data.select_dtypes(include='object')

categorical_data = categorical_data[
    [col for col in categorical_data.columns
     if categorical_data[col].nunique() <= 20]
]

# Convert categorical values into numerical values
categorical_data = pd.get_dummies(
    categorical_data,
    drop_first=True,
    dtype=int
)

# Combine numerical and categorical features
X = pd.concat([numeric_data, categorical_data], axis=1)

# Remove constant columns
X = X.loc[:, X.nunique() > 1]

print("\nFEATURES SELECTED:")
print(X.columns)

if X.shape[1] == 0:
    raise ValueError("No suitable features found for clustering.")

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# 8. Apply Elbow Method

wcss = []

for i in range(1, 11):

    kmeans = KMeans(
        n_clusters=i,
        init='k-means++',
        random_state=42,
        n_init=10
    )

    kmeans.fit(X_scaled)

    wcss.append(kmeans.inertia_)

# Plot Elbow Graph
plt.figure(figsize=(8, 5))

plt.plot(range(1, 11), wcss, marker='o')

plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.xticks(range(1, 11))
plt.grid()

plt.show()


# 9. Compare different K-Means models

results = []

for k in range(2, 11):

    kmeans = KMeans(
        n_clusters=k,
        init='k-means++',
        random_state=42,
        n_init=10
    )

    labels = kmeans.fit_predict(X_scaled)

    score = silhouette_score(X_scaled, labels)

    results.append({
        'Number of Clusters': k,
        'WCSS': kmeans.inertia_,
        'Silhouette Score': score
    })


# Display model comparison
results_df = pd.DataFrame(results)

print("\nMODEL COMPARISON:")
print(results_df.to_string(index=False))


# 10. Visualize Silhouette Scores

plt.figure(figsize=(8, 5))

sns.barplot(
    data=results_df,
    x='Number of Clusters',
    y='Silhouette Score'
)

plt.title("Comparison of Different K-Means Models")
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Score")

plt.show()


# 11. Find the best model

best_model = results_df.loc[
    results_df['Silhouette Score'].idxmax()
]

optimal_k = int(best_model['Number of Clusters'])

print("\nBEST NUMBER OF CLUSTERS:", optimal_k)

print("BEST SILHOUETTE SCORE:",
      best_model['Silhouette Score'])


# 12. Apply final K-Means model

final_kmeans = KMeans(
    n_clusters=optimal_k,
    init='k-means++',
    random_state=42,
    n_init=10
)

df['Cluster'] = final_kmeans.fit_predict(X_scaled)

print("\nFINAL DATASET:")
print(df.head())


# 13. Count records in each cluster

print("\nNUMBER OF RECORDS IN EACH CLUSTER:")
print(df['Cluster'].value_counts())


# 14. Visualize clusters using PCA

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(9, 6))

sns.scatterplot(
    x=X_pca[:, 0],
    y=X_pca[:, 1],
    hue=df['Cluster'],
    palette='viridis',
    s=50
)

plt.title("K-Means Clustering Visualization")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.show()


# 15. Analyse each cluster

print("\nCLUSTER ANALYSIS:")

cluster_analysis = df.groupby('Cluster').mean(
    numeric_only=True
)

print(cluster_analysis)


# 16. Final Conclusion

print("\n========== FINAL CONCLUSION ==========")

print("K-Means clustering was successfully applied.")

print("Optimal number of clusters:", optimal_k)

print("Best Silhouette Score:",
      round(best_model['Silhouette Score'], 4))

print("The dataset was divided into",
      optimal_k, "different clusters.")

print("Clustering performance was evaluated using")
print("WCSS and Silhouette Score.")

print("Note: Silhouette Score is a clustering evaluation")
print("metric, not classification accuracy.")
