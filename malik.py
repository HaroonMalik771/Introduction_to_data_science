import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
House_data = {
    'House Area in Marla': [5, 6, 7, 5, 10, 8],
    'No. of Rooms': [4, 5, 4, 5, 6, 6],
    'Price in Millions of PKR': [15, 17, 18, 15, 8, 16]
}

data_frame= pd.DataFrame(House_data)


y  = data_frame['Price in Millions of PKR']

linear_reg = LinearRegression()
linear_reg.fit(data_frame[['House Area in Marla']], y)
data_frame['Linear Regression'] = linear_reg.predict(data_frame[['House Area in Marla']])

coefficients = np.polyfit(data_frame['House Area in Marla'], y, 2)   # 3 is the degree of the polynomial
poly = np.poly1d(coefficients)
data_frame['Polynomial Regression'] = poly(data_frame['House Area in Marla'])


multi_reg = LinearRegression()
multi_reg.fit(data_frame[['House Area in Marla', 'No. of Rooms']], y)
data_frame['Multiple Regression'] = multi_reg.predict(data_frame[['House Area in Marla', 'No. of Rooms']])
print(data_frame)

