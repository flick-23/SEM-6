import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error

# Load the dataset and print it
boston = load_boston()
# Create dataframes out of the dataset
# data --> independent variables / x values
# target --> dependent variable / y value
# feature_names --> column names / features
df_x = pd.DataFrame(boston.data, columns=boston.feature_names)
df_y = pd.DataFrame(boston.target)

# Generate descriptive statistics such as mean, count, etc.
print(df_x.describe())

# Initialise the linear regression model
reg = linear_model.LinearRegression()

# Split the dataset into 67% training and 33% testing data
x_train, x_test, y_train, y_test = train_test_split(
    df_x, df_y, test_size=0.33, random_state=42)

# Train the model with the training data
reg.fit(x_train, y_train)

# Print the coefficients for each feature
print("\nCOEFFICIENTS", reg.coef_)

# Run the model on the test data and print the predictions
y_pred = reg.predict(x_test)
print("\nPREDICTIONS : ", y_pred)

# Print the actual / target values
print("\nACTUAL DATA : ", y_test)

# Calculate the error
# using np.mean
print("\nNP MEAN : ", np.mean(y_test - y_pred)**2)
# using mean_squared_errro from sklearn.metrics
print("\nMEAN SQUARED ERROR :", mean_squared_error(y_test, y_pred))
