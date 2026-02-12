'''
Normalization
    Z-Score Normalization:
        Transform the data so that it has a mean of 0 and a standard deviation of 1.
    
    Min-Max Normalization:
        Transform the data from measured units to a new interval, which goes from lowerf to upperf

    Log Tranformation
        Transform the data by replacing the values of the original data with its logarithm
'''
import pandas as pd
import matplotlib.pyplot as mp
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

vehicles = pd.read_csv("vehicles.csv")
print(vehicles.head())

print(vehicles[['co2emissions']].describe())
vehicles[['co2emissions']].plot(kind = 'hist', bins=20, figsize=(10,6))
mp.show()

'''
Normalizing by MinMaxScaler
'''
# Transforms the data to a numpy array -> The next scope converts this to a Data Frame
print("\n\n    MinMax Scaler\n")
co2emissions_mm = MinMaxScaler().fit_transform(vehicles[['co2emissions']])
print(co2emissions_mm)
co2emissions_mm = pd.DataFrame(co2emissions_mm, columns= ['co2emissions']) #Converts the numpy array to a dataframe
print(co2emissions_mm)

print(co2emissions_mm.describe())
co2emissions_mm.plot(kind = 'hist', bins=20, figsize=(10,6))
mp.show()

'''
Normalizing by Z-Score
'''
print("\n \n    Z-Score\n")
co2emissions_zm = StandardScaler().fit_transform(vehicles[['co2emissions']])
co2emissions_zm = pd.DataFrame(co2emissions_zm,columns=['co2emission'])
print(co2emissions_zm.describe())
co2emissions_zm.plot(
    kind='hist',
    bins= 20,
    figsize= (10,6)
)
mp.show()
