
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 1. Create DataFrame
data = {
    'Month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Advertising Cost': [10000, 12000, 15000, 18000, 20000,
                         22000, 25000, 28000, 30000, 35000],
    'Sales': [50000, 56000, 65000, 72000, 80000,
              86000, 95000, 104000, 110000, 125000]
}

df = pd.DataFrame(data)

print("Historical Data:")
print(df)

# 2. Separate X and Y
X = df[['Advertising Cost']]
Y = df['Sales']

# 3. Split training and testing data
X_train = X.iloc[:8]
X_test = X.iloc[8:]

Y_train = Y.iloc[:8]
Y_test = Y.iloc[8:]

# 4. Train Linear Regression model
model = LinearRegression()
model.fit(X_train, Y_train)

# 5. Predict sales for advertising cost 32000
predicted_sales = model.predict(pd.DataFrame({
    'Advertising Cost': [32000]
}))

print("\nPredicted Sales:", predicted_sales[0])

# 6. Display coefficient and intercept
print("Regression Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)

# 7. Calculate R2 score
Y_pred = model.predict(X_test)

r2 = r2_score(Y_test, Y_pred)

print("R2 Score:", r2)

# 8. Plot historical data and regression line
plt.scatter(X, Y, color='blue', label='Actual Sales')

plt.plot(X, model.predict(X),
         color='red', label='Regression Line')

plt.xlabel('Advertising Cost')
plt.ylabel('Sales')

plt.title('Advertising Cost vs Sales - Linear Regression')

plt.legend()
plt.grid(True)
plt.show()
