import pandas as pd

washers = pd.read_csv("washers.csv")
washers.info() # General info
print(washers.head()) # Shows the first five instances to give you context

print(washers[["BrandName"]].describe()) # Categorical data
print(washers[["Volume"]].describe()) # Numerical data
print(washers[["BrandName"]].value_counts()) # Gives you the count
print(washers[["BrandName"]].value_counts(normalize= True)) # Gives you the percentage of each option
print(washers[["Volume"]].mean()) # Specific agreggations on numerical values. Such as mean in this case
print(washers.groupby('BrandName')[['Volume']].mean()) # Washer mean volumes by brand
print(washers.groupby('BrandName')[['Volume']].mean().sort_values(by= 'Volume')) # Washer mean volumes by brand sorted


print(washers.groupby("BrandName")[['Volume']].agg(['median','mean','min','max', 'count']))