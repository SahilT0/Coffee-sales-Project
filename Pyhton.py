# Predicting Sales for Future Months

# Importing necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Reading CSV file
coffee_sales = pd.read_csv("C:/Users/SAHIL/Unified Mentor/Project (Data Analyst)/Coffee sales/index.csv")

# for showing all cols and rows in pycharm
# pd.set_option("display.max_columns",None)
# pd.set_option("display.max_rows",None)
print(coffee_sales)