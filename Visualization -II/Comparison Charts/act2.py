import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('FuelConsumption.csv')

data.head()

data.isnull().any()

df_grouped = data.groupby('VEHICLECLASS').mean()

df_grouped.head()

# numerical x
x = np.arange(0, len(df_grouped.index))
# plot bars
plt.bar(x, df_grouped['FUELCONSUMPTION_CITY'], bottom=df_grouped['FUELCONSUMPTION_HWY'], 
        color = '#1D2F6F')
plt.bar(x, df_grouped['FUELCONSUMPTION_HWY'], color = '#8390FA')
plt.bar(x, df_grouped['FUELCONSUMPTION_COMB'], bottom=df_grouped['FUELCONSUMPTION_COMB'], 
        color = '#6EAF46')
plt.ylabel('Fuel Consumption')
plt.xticks(x, df_grouped.index, rotation=90)
plt.legend(['City','Highway','Combined'])
plt.title('Average Fuel Consumption for Different Vehicle Type')
plt.show()