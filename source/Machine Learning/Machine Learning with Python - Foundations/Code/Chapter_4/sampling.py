'''
Sampling without replacement: They don't remain in the pool of people we can select
Sampling with replacement: Remain in the pool of people we can select
Stratified sampling: It first strates the data, then it samples
'''

import pandas as pd
from sklearn.model_selection import train_test_split

vehicles = pd.read_csv('vehicles.csv')
print(vehicles)

'''
We have to separate are data.
First we are going to separate the dependant from the independant variables,
by creating a dataframe only with the co2emissions.
    In this case, our dependant variable is co2emissions
Second, we are going to create a dataframe with all the other columns.
    To do this we are going to create first a list with all the columns
    of the dataset. Then we are going to erase the co2emissions column
    from the list.
    After doing this we can create a dataframe with the remaining columns
    on the list.
'''
response = 'co2emissions'
y = vehicles[[response]]
print(y.head())

predictors = list(vehicles.columns)
#print(predictors)
predictors.remove(response)
#print(predictors)
x = vehicles[predictors]
print(x.head())

'''
Simple Random Sampling:
We create 4 datasets, 2 for training and 2 for testing.
    For default train_test_split destines 25% of the data to the test set,
    we can change this modifiying the test size or the train size
'''
x_train, y_train, x_test, y_test = train_test_split(x,y)
print('\nSimple Random Sampling 25 % (Rows, Columns)')
print(f'X train set: {x_train.shape}')
print(f'X test set: {x_test.shape}')
print(f'Y train set: {y_train.shape}')
print(f'Y test set: {y_test.shape}')

x_train, y_train, x_test, y_test = train_test_split(x, y, test_size=0.4)
print('\nSimple Random Sampling 40 % (Rows, Columns)')
print(f'X train set: {x_train.shape}')
print(f'X test set: {x_test.shape}')
print(f'Y train set: {y_train.shape}')
print(f'Y test set: {y_test.shape}')

'''
Stratified Random Sampling
'''
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.01, random_state=1234)
print('\nStratified Random Sampling 1 % (Rows, Columns)')
print(f'X train set: {x_train.shape}')
print(f'X test set: {x_test.shape}')
print(f'Y train set: {y_train.shape}')
print(f'Y test set: {y_test.shape}')

print('\nNormalized distribution on the origninal X set')
print(x['drive'].value_counts(normalize= True))

print('\nNormalized distribution on the X_Test set')
print(x_test['drive'].value_counts(normalize= True))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.01, random_state=1234, stratify=x['drive'])
print('\nNormalized distribution on the X_Test set after stratifiying the set')
print(x_test['drive'].value_counts(normalize= True))