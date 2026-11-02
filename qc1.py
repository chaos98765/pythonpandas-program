import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
#Dataset
x = np.array([1,2,3,4,5,6]).reshape(-1,1)
y = np.array([10,20,30,40,50,60])
#create an train model
model = LinearRegression()
model.fit(x,y)
#predict values
y_pred = model.predict(x)
#calculate evaluation mertrics
mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
rase = np.sqrt(mse)
r2 = r2_score(y, y_pred)
#Display results
print("Actual Values:", y)
print("Predicted Values:", y_pred.round(2))

print("\nMAE :", round(mae, 2))
print("MSE :", round(mse, 2))
print("RMSE :", round(rase, 2))
print("R2 Score :", round(r2, 2))
#Graph: Actual vs Predicted
plt.scatter(x, y, color='blue', label='Actual Values')
plt.plot(x, y_pred, color='red', label='Predicted Values')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression:Actual vs Predicted Values")
plt.legend()
plt.grid(True)
plt.show()
