import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------------------------------
# LOAD DATASET
# ---------------------------------------------

data = pd.read_csv("FuelConsumption.csv")

print("First 5 rows:")
print(data.head())


# ---------------------------------------------
# 1. CHECK NULL VALUES
# ---------------------------------------------

print("\nNull values in each column:")
print(data.isnull().sum())

# Handle missing values
data = data.dropna()

print("\nNull values after handling:")
print(data.isnull().sum())


# ---------------------------------------------
# 2. CHECK DETAILS OF DATASET
# ---------------------------------------------

print("\nDataset Information:")
data.info()

print("\nShape:")
print(data.shape)

print("\nData Types:")
print(data.dtypes)

print("\nStatistical Summary:")
print(data.describe())


# ---------------------------------------------
# 3. MEAN VALUES GROUPED BY FUEL TYPE
# ---------------------------------------------

fuel_mean = data.groupby("Fuel Type").mean(numeric_only=True)

print("\nMean values grouped by Fuel Type:")
print(fuel_mean)


# ---------------------------------------------
# 4. RESET INDEX
# ---------------------------------------------

fuel_mean.reset_index(inplace=True)

print("\nAfter resetting index:")
print(fuel_mean)


# ---------------------------------------------
# 5. AVERAGE CO2 EMISSIONS BY FUEL TYPE
#    BAR PLOT
# ---------------------------------------------

plt.figure(figsize=(8, 5))

sns.barplot(
    x="Fuel Type",
    y="CO2 Emissions(g/km)",
    data=fuel_mean,
    palette="Set2"
)

plt.title("Average CO2 Emissions by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Average CO2 Emissions (g/km)")

plt.show()


# ---------------------------------------------
# 6. NUMBER OF ENTRIES FOR EACH FUEL TYPE
#    COUNT PLOT
# ---------------------------------------------

plt.figure(figsize=(8, 5))

sns.countplot(
    x="Fuel Type",
    data=data,
    palette="Set2"
)

plt.title("Number of Vehicles by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Number of Vehicles")

plt.show()


# ---------------------------------------------
# 7. NUMBER OF ENTRIES FOR EACH VEHICLE CLASS
#    COUNT PLOT
# ---------------------------------------------

plt.figure(figsize=(12, 6))

sns.countplot(
    x="Vehicle Class",
    data=data,
    palette="Set3"
)

plt.title("Number of Vehicles by Vehicle Class")
plt.xlabel("Vehicle Class")
plt.ylabel("Number of Vehicles")

plt.xticks(rotation=45)

plt.show()


# ---------------------------------------------
# 8. MEAN VALUES GROUPED BY VEHICLE CLASS
# ---------------------------------------------

vehicle_mean = data.groupby("Vehicle Class").mean(numeric_only=True)

print("\nMean values grouped by Vehicle Class:")
print(vehicle_mean)


# ---------------------------------------------
# 9. RESET INDEX
# ---------------------------------------------

vehicle_mean.reset_index(inplace=True)

print("\nVehicle Class mean DataFrame:")
print(vehicle_mean)


# ---------------------------------------------
# 10. AVERAGE CO2 EMISSIONS BY VEHICLE CLASS
#     BAR PLOT
# ---------------------------------------------

plt.figure(figsize=(12, 6))

sns.barplot(
    x="Vehicle Class",
    y="CO2 Emissions(g/km)",
    data=vehicle_mean,
    palette="viridis"
)

plt.title("Average CO2 Emissions by Vehicle Class")
plt.xlabel("Vehicle Class")
plt.ylabel("Average CO2 Emissions (g/km)")

plt.xticks(rotation=45)

plt.show()


# ---------------------------------------------
# 11. STACKED BAR PLOT
#     CITY, HIGHWAY AND COMBINED FUEL CONSUMPTION
# ---------------------------------------------

fuel_consumption = data.groupby("Vehicle Class")[
    [
        "Fuel Consumption City (L/100 km)",
        "Fuel Consumption Hwy (L/100 km)",
        "Fuel Consumption Comb (L/100 km)"
    ]
].mean()

print("\nAverage fuel consumption by Vehicle Class:")
print(fuel_consumption)


# Create stacked bar plot

fuel_consumption.plot(
    kind="bar",
    stacked=True,
    figsize=(14, 7)
)

plt.title("Average Fuel Consumption by Vehicle Class")
plt.xlabel("Vehicle Class")
plt.ylabel("Fuel Consumption (L/100 km)")

plt.xticks(rotation=45)

plt.legend(
    title="Fuel Consumption",
    labels=[
        "City",
        "Highway",
        "Combined"
    ]
)

plt.tight_layout()
plt.show()