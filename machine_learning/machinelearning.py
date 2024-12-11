from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import numpy as np

# Generate some sample data
y_true = np.array([1, 2, 3, 1])
y_pred = np.array([1, 2, 3, 6])

# Calculate the MAE
mae = mean_absolute_error(y_true, y_pred)
print("Mean Absolute Error:", mae)
