import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("FuelConsumption.csv")

# 1. Check null values
print(data.isnull().sum())

# Handle null values
data = data.dropna()

# 2. Dataset details
print(data.info())
print(data.describe())
print(data.dtypes)

# 3. CO2 Emissions vs Combined MPG
sns.scatterplot(
    x="Fuel Consumption Comb. (mpg)",
    y="CO2 Emissions(g/km)",
    data=data
)
plt.title("CO2 Emissions vs Combined MPG")
plt.show()

# 4. CO2 vs MPG for different fuel types
sns.scatterplot(
    x="Fuel Consumption Comb. (mpg)",
    y="CO2 Emissions(g/km)",
    hue="Fuel Type",
    data=data
)
plt.title("CO2 Emissions vs MPG by Fuel Type")
plt.show()

# 5. CO2 vs MPG, fuel type + engine size
sns.scatterplot(
    x="Fuel Consumption Comb. (mpg)",
    y="CO2 Emissions(g/km)",
    hue="Fuel Type",
    size="Engine Size(L)",
    data=data
)
plt.title("CO2 vs MPG by Fuel Type and Engine Size")
plt.show()

# 6. Correlation between numerical features
correlation = data.corr(numeric_only=True)

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.show()

# 7. Individual plots for each fuel type
fuel_types = data["Fuel Type"].unique()

for fuel in fuel_types:
    fuel_data = data[data["Fuel Type"] == fuel]

    sns.scatterplot(
        x="Fuel Consumption Comb. (mpg)",
        y="CO2 Emissions(g/km)",
        data=fuel_data
    )

    plt.title(f"CO2 Emissions vs MPG - Fuel Type: {fuel}")
    plt.show()

# 8. Relationship between features with Fuel Type as hue
sns.pairplot(
    data,
    hue="Fuel Type",
    palette="Set2"
)

plt.show()