import pandas as pd
import matplotlib.pyplot as plt
vehicles = pd.read_csv('vehicles.csv')
print(vehicles.head())

#Comparision
vehicles.plot(kind="scatter", x='citympg', y='co2emissions')
plt.show()

#Relationship
vehicles['co2emissions'].plot(kind='hist')
plt.show()

#Distribution
print(vehicles.pivot(columns='drive', values='co2emissions'))
print(vehicles.pivot(columns='drive', values='co2emissions').plot(kind= 'box', figsize=(10,6)))
plt.show()

#Composition
print(vehicles.groupby('year')['drive'].value_counts())
print(vehicles.groupby('year')['drive'].value_counts().unstack())
vehicles.groupby('year')['drive'].value_counts().unstack().plot(kind='bar', stacked=True, figsize=(10,6))
plt.show()