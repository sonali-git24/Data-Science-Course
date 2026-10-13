# Importing Libraries and dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('gapminder(2007).csv')

data.head()

data.info()

data.isnull().any()

labels = ['population','life_exp','gdp_cap']

# Plotting boxplots
for l in labels:
  sns.boxplot(y=data[l], palette='winter')
  plt.show()

sns.boxplot(y='gdp_cap', x='continent',data=data, palette='viridis')

sns.boxplot(y='life_exp', x='continent',data=data, palette='viridis')

# Plotting violin plots
sns.violinplot(y='gdp_cap', x='continent',data=data, palette='bright')

sns.violinplot(y='life_exp', x='continent',data=data, palette='bright')

#Plotting Density Plot
for l in labels:
  sns.kdeplot(data[l])
  plt.show()

# Plotting histogram
for l in labels:
  plt.hist(data[l])
  plt.xlabel(l)
  plt.show()

# Plotting Distplot
for l in labels:
  sns.distplot(data[l])
  plt.show()
  print("Skewness is :", data[l].skew())

