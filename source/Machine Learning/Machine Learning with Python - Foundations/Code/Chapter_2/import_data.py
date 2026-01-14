import pandas as pd

#Pandas Series
members = ["Brazil", "Rusia","India","China", "South Africa"]
brics1 = pd.Series(members)
print(brics1)
print(type(brics1))

#Pandas DataFrame
members = {
    "country": ["Brazil","Russia","India","China","South Africa"],
    "capital":["Brasilia","Moscow","New Delhi","Beijing","Pretoria"],
    "gdp": [2750, 1658, 3202, 15270, 370],
    "literacy":[.944, .997, .721, .964, .943],
    "expectancy": [76.8, 72.7, 68.8, 76.4, 63.6],
    "population": [210.87, 143.96, 1367.09, 1415.05, 57.4]
}
brics2 = pd.DataFrame(members)
print(brics2)
print(type(brics2))

members = [
    ["Brazil", "Brasilia", 2750, 0.944, 76.8, 210.87],
    ["Russia", "Moscow", 1658, 0.997, 72.7, 143.96],
    ["India", "New Delhi", 3202, 0.721, 68.8, 1367.09],
    ["China", "Beijing", 15270, 0.964, 76.4, 1415.05],
    ["South Africa", "Pretoria", 370, 0.943, 63.6, 57.4]
]
labels = ["country", "capital", "gdp", "literacy", "expectancy", "population"]
brics3 = pd.DataFrame(members, columns = labels)
print(brics3)
print(type(brics3))

#Importing CSV file
brics4 = pd.read_csv('brics.csv')
print(brics4)

#Importing EXCEL file
''' Error al ejecutar
brics5 = pd.read_excel("brics.xlsx")
print(brics5)
'''

#Importing EXCEL file with multiple sheets
''' Error al ejecutar
brics6 = pd.read_excel("brics.xlsx", sheet_name = "Summits")
print(brics6)
'''