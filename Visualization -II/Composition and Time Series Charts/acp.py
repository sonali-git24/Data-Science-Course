import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------
# 1. LOAD DATASET
# -----------------------------------------

data = pd.read_csv("FuelConsumption.csv")

print(data.head())


# -----------------------------------------
# 2. CHECK NULL VALUES
# -----------------------------------------

print("\nNull values in each column:")
print(data.isnull().sum())


# Handle null values
data = data.dropna()

print("\nNull values after handling:")
print(data.isnull().sum())


# -----------------------------------------
# 3. CHECK DETAILS OF DATASET
# -----------------------------------------

print("\nDataset Information:")
data.info()

print("\nShape of dataset:")
print(data.shape)

print("\nData types:")
print(data.dtypes)

print("\nStatistical summary:")
print(data.describe())


# -----------------------------------------
# 4. PIE CHART FOR FUEL TYPE
# -----------------------------------------

fuel_counts = data["Fuel Type"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    fuel_counts.values,
    labels=fuel_counts.index,
    autopct="%1.1f%%"
)

plt.title("Distribution of Vehicles by Fuel Type")

plt.show()


# -----------------------------------------
# 5. CUSTOMIZE PIE CHART USING WEDGE PROPS
# -----------------------------------------

plt.figure(figsize=(7, 7))

plt.pie(
    fuel_counts.values,
    labels=fuel_counts.index,
    autopct="%1.1f%%",
    wedgeprops={
        "edgecolor": "black",
        "linewidth": 2
    },
    startangle=90
)

plt.title("Distribution of Vehicles by Fuel Type")

plt.show()


# -----------------------------------------
# 6. PIE CHART FOR VEHICLE CLASS
# -----------------------------------------

vehicle_class_counts = data["Vehicle Class"].value_counts()

plt.figure(figsize=(9, 9))

plt.pie(
    vehicle_class_counts.values,
    labels=vehicle_class_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Distribution of Vehicles by Vehicle Class")

plt.show()


# -----------------------------------------
# 7. LINE PLOT OF ALL CO2 EMISSIONS
# -----------------------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    data["CO2 Emissions(g/km)"],
    marker="o",
    linewidth=1
)

plt.xlabel("Vehicle Index")
plt.ylabel("CO2 Emissions (g/km)")
plt.title("CO2 Emissions of Vehicles")

plt.grid(True)

plt.show()