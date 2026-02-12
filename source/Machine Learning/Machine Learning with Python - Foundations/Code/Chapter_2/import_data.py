import pandas as pd

members = ["Brazil","Russia", "India", "China", "South Africa"]
brics1 = pd.Series(members)
print(brics1, type(brics1), brics1[0])

members = {
    "country": ["Brazil","Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "gdp": [2750, 1658, 3202, 15270, 370],
    "literacy": [.944, .997, .721, .964, .943],
    "expectancy": [76.8, 72.7, 68.8, 76.4, 63.6],
    "population": [210.87, 143.96, 1367.09, 1415.05, 57.4]
}
brics2 = pd.DataFrame(members)
print(brics2, type(brics2))

members = [
    ["Brazil", "Brasilia", 2750, 0.944, 76.8, 210.87],
    ["Russia", "Moscow", 1658, 0.997, 72.7, 143.96],
    ["India", "New Delhi", 3202, 0.721, 68.8, 1367.09],
    ["China", "Beijing", 15270, 0.964, 76.4, 1415.05],
    ["South Africa", "Pretoria", 370, 0.943, 63.6, 57.4]]
labels = ["Country", "Capital", "Gdp", "Literacy", "Expectancy", "Population"]
brics3 = pd.DataFrame(members, columns=labels)
print(brics3)

print("-------------------------- CSV -------------------------------------")
brics_csv = pd.read_csv("brics.csv")
print(brics_csv, "\n0", type(brics_csv))

print("------------------------- Excel ------------------------------------")
brics_excel = pd.read_excel("brics.xlsx")
brics_excel_sheet2 = pd.read_excel("brics.xlsx", sheet_name="Summits")
print(brics_excel, "\n", brics_excel_sheet2)

