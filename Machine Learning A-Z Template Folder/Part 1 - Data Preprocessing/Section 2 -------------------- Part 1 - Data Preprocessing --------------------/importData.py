import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import data set
dataset = pd.read_csv('Data.csv')

# take all the columns (independent variables) except the last one
X = dataset.iloc[:, :-1].values

# 3 is the index dependent variables
y = dataset.iloc[:, 3].values