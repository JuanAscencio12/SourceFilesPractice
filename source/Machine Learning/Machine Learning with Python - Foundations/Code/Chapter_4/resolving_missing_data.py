import pandas as pd

students = pd.read_excel("students.xlsx")
print(students)

# Deletes if the state row is null
mask = students['State'].isnull()
print(mask)

# Shows the rows where the State is null
print(students[mask])

# Removes all the rows where there is a missing value
print(students.dropna())

# Removes all the rows where the State and Zip is null
print(students.dropna(subset=['State', 'Zip'], how= 'all'))

# Removes all the columns where there is an empty cell
print(students.dropna(axis=1))

# Removes all the columns where the 50% 
# of the rows are missing
# (in this case 10, represents the 50% because
#   the dataset has 20 rows)
print(students.dropna(axis=1, thresh=10))

# You can fill the missing data as you wish
print(students.fillna({'Gender':'Female'}))
print(students.fillna({'Age':students['Age'].median()}))

mask = (students['City'] == 'Granger') & (students['State'] == 'IN')
print(students.loc[mask, :])
students.loc[mask, 'Zip'] == 46530