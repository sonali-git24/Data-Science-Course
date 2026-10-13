
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('gapminder(2007).csv')

data.head()

# Checking null values
data.isnull().any()

#checking details of dataset
data.info()

# Countplot for feature Continent
# Setting different themes
sns.set_style('white')
sns.countplot(x=data['continent'])

sns.set_style('dark')
sns.countplot(x=data['continent'])

sns.set_style('whitegrid')
sns.countplot(x=data['continent'])

sns.set_style('darkgrid')
sns.countplot(x=data['continent'])

sns.set_style('ticks')
sns.countplot(x=data['continent'])

# Despining
sns.set_style('white')
sns.countplot(x=data['continent'])
sns.despine()

# Trying different palettes
sns.set_style('whitegrid')
sns.countplot(x=data['continent'], palette='winter')

sns.set_style('whitegrid')
sns.countplot(x=data['continent'], color='Purple')

# Scaling figures
sns.set_style('whitegrid')
sns.set_context("paper")
sns.countplot(x=data['continent'], color='Purple')

sns.set_style('whitegrid')
sns.set_context("notebook")
sns.countplot(x=data['continent'], color='Purple')

sns.set_style('whitegrid')
sns.set_context("talk")
sns.countplot(x=data['continent'], color='Purple')

sns.set_style('whitegrid')
sns.set_context("poster")
sns.countplot(x=data['continent'], color='Purple')
plt.xticks(rotation=45)

# Scaling font size of figure
sns.set_style('whitegrid')
sns.set_context("poster", font_scale=0.8)
sns.countplot(x=data['continent'], color='Purple')
plt.xticks(rotation=45)

