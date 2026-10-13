
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('gapminder(2007).csv')

data.head()

data.groupby('continent').size().plot(kind='pie', autopct='%.2f')

plt.pie(data.groupby('continent').size(), autopct='%.2f', 
        labels=['Africa','America','Asia','Europe','Oceania'],
        labeldistance=1.15, wedgeprops = { 'linewidth' : 2, 'edgecolor' : 'white' })