import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("FuelConsumption.csv")

# ---------------------------------------
# 1. CHECK NULL VALUES
# ---------------------------------------

print("Null values:")
print(data.isnull().sum())

# Handle null values
data = data.dropna()

print("\nAfter handling null values:")
print(data.isnull().sum())


# ---------------------------------------
# 2. DETAILS OF DATASET
# ---------------------------------------

print("\nDataset Information:")
data.info()

print("\nShape of dataset:")
print(data.shape)

print("\nData types:")
print(data.dtypes)

print("\nStatistical summary:")
print(data.describe())


# ---------------------------------------
# 3. BOXPLOT FOR ALL QUANTITATIVE FEATURES
# ---------------------------------------

numeric_columns = data.select_dtypes(include="number").columns

for column in numeric_columns:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=data[column])
    plt.title(f"Boxplot of {column}")
    plt.xlabel(column)
    plt.show()


# ---------------------------------------
# 4. CO2 EMISSIONS BY FUEL TYPE
#    BOXPLOT
# ---------------------------------------

plt.figure(figsize=(8, 5))

sns.boxplot(
    x="Fuel Type",
    y="CO2 Emissions(g/km)",
    data=data,
    palette="Set2"
)

plt.title("CO2 Emissions by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("CO2 Emissions (g/km)")
plt.show()


# ---------------------------------------
# 5. CO2 EMISSIONS BY VEHICLE CLASS
#    BOXPLOT
# ---------------------------------------

plt.figure(figsize=(12, 6))

sns.boxplot(
    x="Vehicle Class",
    y="CO2 Emissions(g/km)",
    data=data,
    palette="Set3"
)

plt.title("CO2 Emissions by Vehicle Class")
plt.xlabel("Vehicle Class")
plt.ylabel("CO2 Emissions (g/km)")
plt.xticks(rotation=45)
plt.show()


# ---------------------------------------
# 6. CO2 EMISSIONS BY FUEL TYPE
#    VIOLIN PLOT
# ---------------------------------------

plt.figure(figsize=(8, 5))

sns.violinplot(
    x="Fuel Type",
    y="CO2 Emissions(g/km)",
    data=data,
    palette="Set2"
)

plt.title("CO2 Emissions Distribution by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("CO2 Emissions (g/km)")
plt.show()


# ---------------------------------------
# 7. CO2 EMISSIONS BY VEHICLE CLASS
#    VIOLIN PLOT
# ---------------------------------------

plt.figure(figsize=(12, 6))

sns.violinplot(
    x="Vehicle Class",
    y="CO2 Emissions(g/km)",
    data=data,
    palette="Set3"
)

plt.title("CO2 Emissions Distribution by Vehicle Class")
plt.xlabel("Vehicle Class")
plt.ylabel("CO2 Emissions (g/km)")
plt.xticks(rotation=45)
plt.show()


# ---------------------------------------
# 8. DENSITY PLOTS FOR ALL QUANTITATIVE
#    FEATURES
# ---------------------------------------

for column in numeric_columns:

    plt.figure(figsize=(8, 4))

    sns.kdeplot(
        data=data,
        x=column,
        fill=True
    )

    plt.title(f"Density Plot of {column}")
    plt.xlabel(column)
    plt.ylabel("Density")
    plt.show()


# ---------------------------------------
# 9. HISTOGRAMS FOR ALL QUANTITATIVE
#    FEATURES
# ---------------------------------------

for column in numeric_columns:

    plt.figure(figsize=(8, 4))

    sns.histplot(
        data=data,
        x=column,
        bins=20,
        kde=False
    )

    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()


# ---------------------------------------
# 10. DISTPLOTS FOR DISTRIBUTION
#     AND SKEWNESS
# ---------------------------------------

for column in numeric_columns:

    plt.figure(figsize=(8, 4))

    sns.histplot(
        data=data,
        x=column,
        kde=True,
        bins=20
    )

    plt.title(f"Distribution and Skewness of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()