import pandas as pd
import matplotlib.pyplot as mp
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

'''
Charge and see data
'''
bikes = pd.read_csv('bikes.csv')
print("\nHead")
print(bikes.head())

print("\nDescription")
print(bikes.describe())

'''
Scatter to see the relation
'''
#bikes.plot(kind="scatter", x='temperature', y='rentals')
#mp.show()
#bikes.plot(kind="scatter", x='humidity', y='rentals')
#mp.show()
#bikes.plot(kind="scatter", x='windspeed', y='rentals')
#mp.show()

'''
Spliting data to prepare model
'''
response = 'rentals'
y = bikes['rentals']

predictors = list(bikes)
predictors.remove(response)
x = bikes[predictors]

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state= 1234)

'''
Train the model
'''
model = LinearRegression().fit(x_train, y_train)
print('\n\nThe model coefficients correspond to the orden in witch the independent variables are listed in the training data.')
print('This means that the equation for the fitted regression line can be written as:')
print('     y = 3800.68 + 80.35 * temperature - 4665.74 * humidity - 196.22 * windspeed')
print('With the linear regression equation, we can estimate ehat our model will predict given any weather condition.')
print('For example, given a temperature of 72°F ,22% humidity and windspeed of 5 milles per hour, our model would predict:')
print('     7,578 bikes ≈ 3800.68 + 80.35 * 72 - 4665.74 * .22 - 196.22 * 5')

print(f'\nEstimated intercept value for the model: {model.intercept_}')
print(f'\nEstimated coefficeintes for the regression line\n     (temperature / humidity / windspeed): {model.coef_}')

'''
Evaluate the model
'''
print(f'\nR squared value: {model.score(x_test, y_test)}')
y_pred = model.predict(x_test)
print(f'Mean absolute error: +-{mean_absolute_error(y_test, y_pred)} bikes')

'''
Common Supervised Machine Learning algorithms:
    Linear Regression: How many bikes are going to be rented 
    Logistic Regression: Is he going to buy that based o his social economic level
    Decision Tree: Is he going to pay his loan
    Neural Networks: Image detection or language translation (LLM, Deep Learning)

Ensambled learning:
    Random Forests: Several decisions trees in paralel
    Gradient Boosting Machines: Several decisions trees trained in sequential manner to try to correct the mistakes of the previous one

Common Unsupervised Learning algorithms:
    K-Means Clustering: Groups items into one of "k" clusters based on similarity
    Association Rules: Set of if-then statements that describe the co-occurrence of items within data
'''