# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Upload the dataset in Google Colab

# Load the dataset (replace with your actual CSV filename)
df = pd.read_csv('FuelConsumption.csv')

# Display the first five rows
print("First five rows:")
print(df.head())

# Check for null values
print("\nNull values in each column:")
print(df.isnull().sum())

# Handle missing values
df = df.dropna()

print("\nNull values after handling:")
print(df.isnull().sum())

# Check dataset details
print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nDataset information:")
df.info()

print("\nStatistical summary:")
print(df.describe(include='all'))

# Group by Fuel Type and calculate mean values
grouped_df = df.groupby('Fuel Type').mean(numeric_only=True)

print("\nMean values grouped by Fuel Type:")
print(grouped_df)

# Reset the index and update the dataframe
grouped_df = grouped_df.reset_index()

print("\nDataFrame after resetting index:")
print(grouped_df.head())

# Create a bar plot with annotations
plt.figure(figsize=(10, 6))

ax = sns.barplot(
    data=grouped_df,
    x='Fuel Type',
    y='CO2 Emissions(g/km)',
    errorbar=None
)

# Add title and labels
ax.set_title('Average CO2 Emissions by Fuel Type', fontsize=14)
ax.set_xlabel('Fuel Type', fontsize=12)
ax.set_ylabel('Average CO2 Emissions (g/km)', fontsize=12)

# Annotate the bars with their values
for container in ax.containers:
    ax.bar_label(container, fmt='%.2f', padding=3)

# Improve the plot layout
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot
plt.show()
