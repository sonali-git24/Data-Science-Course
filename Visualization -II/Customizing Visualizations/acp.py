import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------
data = pd.read_csv("FeulConsumption.csv")

# --------------------------------------------------
# 2. Check Null Values
# --------------------------------------------------
print("Null values in each column:")
print(data.isnull().sum())

# Handle null values
data = data.dropna()

print("\nNull values after handling:")
print(data.isnull().sum())

# --------------------------------------------------
# 3. Check Dataset Details
# --------------------------------------------------
print("\nDataset Information:")
data.info()

print("\nShape of dataset:")
print(data.shape)

print("\nData Types:")
print(data.dtypes)

print("\nFirst 5 rows:")
print(data.head())

# --------------------------------------------------
# 4. Count Plot - Fuel Type
# --------------------------------------------------
plt.figure(figsize=(8, 5))

sns.countplot(
    x="Fuel Type",
    data=data
)

plt.title("Number of Vehicles by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Number of Vehicles")
plt.xticks(rotation=45)
plt.show()

# --------------------------------------------------
# 5. Try Different Seaborn Themes
# --------------------------------------------------

themes = ["white", "dark", "whitegrid", "darkgrid", "ticks"]

for theme in themes:
    sns.set_theme(style=theme)

    plt.figure(figsize=(8, 5))

    sns.countplot(
        x="Fuel Type",
        data=data
    )

    plt.title(f"Fuel Type Count Plot - {theme}")
    plt.xlabel("Fuel Type")
    plt.ylabel("Number of Vehicles")
    plt.xticks(rotation=45)

    plt.show()

# --------------------------------------------------
# 6. White Theme + Remove Spines
# --------------------------------------------------

sns.set_theme(style="white")

plt.figure(figsize=(8, 5))

sns.countplot(
    x="Fuel Type",
    data=data
)

sns.despine()

plt.title("Fuel Type Count Plot")
plt.xlabel("Fuel Type")
plt.ylabel("Number of Vehicles")
plt.xticks(rotation=45)

plt.show()

# --------------------------------------------------
# 7. Set Palette
# --------------------------------------------------

sns.set_theme(style="white")

plt.figure(figsize=(8, 5))

sns.countplot(
    x="Fuel Type",
    data=data,
    palette="Set2"
)

sns.despine()

plt.title("Fuel Type Count Plot - Set2 Palette")
plt.xlabel("Fuel Type")
plt.ylabel("Number of Vehicles")
plt.xticks(rotation=45)

plt.show()

# --------------------------------------------------
# 8. Set Color of Bars
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.countplot(
    x="Fuel Type",
    data=data,
    color="steelblue"
)

sns.despine()

plt.title("Fuel Type Count Plot")
plt.xlabel("Fuel Type")
plt.ylabel("Number of Vehicles")
plt.xticks(rotation=45)

plt.show()

# --------------------------------------------------
# 9. Try Different Figure Scales
# --------------------------------------------------

scales = ["paper", "notebook", "talk", "poster"]

for scale in scales:

    sns.set_context(scale)

    plt.figure(figsize=(8, 5))

    sns.countplot(
        x="Fuel Type",
        data=data
    )

    plt.title(f"Fuel Type Count Plot - {scale}")
    plt.xlabel("Fuel Type")
    plt.ylabel("Number of Vehicles")
    plt.xticks(rotation=45)

    plt.show()

# --------------------------------------------------
# 10. Poster Scale + Font Size 0.8
# --------------------------------------------------

sns.set_context("poster", font_scale=0.8)

plt.figure(figsize=(8, 5))

sns.countplot(
    x="Fuel Type",
    data=data
)

sns.despine()

plt.title("Fuel Type Count Plot")
plt.xlabel("Fuel Type")
plt.ylabel("Number of Vehicles")
plt.xticks(rotation=45)

plt.show()