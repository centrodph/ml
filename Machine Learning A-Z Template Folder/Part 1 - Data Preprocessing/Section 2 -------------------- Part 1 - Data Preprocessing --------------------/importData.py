import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import data set
dataset = pd.read_csv('Data.csv')

# take all the columns (independent variables) except the last one
X = dataset.iloc[:, :-1].values

# 3 is the index dependent variables
y = dataset.iloc[:, 3].values


# replace missing variables
from sklearn.preprocessing import LabelEncoder
imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
# fit the right columns 1 it's included, 3 is excluded => we sent 1 and 2
imputer = imputer.fit(X[:, 1:3])

#replace missing values with imputer
X[:, 1:3] = imputer.transform(X[:, 1:3])


# categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_X = LabelEncoder()
X[:, 0] = labelEncoder_X.fit_transform(X[:, 0])
oneHotEncoder = OneHotEncoder(categorical_features = [0])