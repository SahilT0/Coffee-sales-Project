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

# Creating a copy of original Data
sales = coffee_sales.copy()

# Data Structure
print(sales.info())

# Summarizing Data
print(sales.describe())

# Converting Datatype
sales['date'] = pd.to_datetime(sales['date'])
sales['datetime'] = pd.to_datetime(sales['datetime'])

# Missing values
print(sales.isnull().sum())
# card has 89 missing value which is of the cash user

# Handle missing value
sales['card'] = sales['card'].fillna("Cash_User")

print(sales.head(10))

# Adding column Month, Day, Hour
sales['month'] = sales['date'].dt.strftime('%Y-%m')
sales['day'] = sales['date'].dt.day_name()
sales['hours'] = sales['datetime'].dt.hour

print(sales.head(15))
print(sales.info())

# Card value count
card_count = sales['card'].value_counts()
print(card_count)

# New column Customer_Frequency
sales['customer_frequency'] = sales['card'].map(card_count)

print(sales.head(25))
# cash user showing the frequency of 89 , now making them as 0
filtered_sales = sales[sales['card'] != 'Cash_User']
card_count = filtered_sales['card'].value_counts()
sales['customer_frequency'] = sales['card'].map(card_count)
sales['customer_frequency'] = sales['customer_frequency'].fillna(0).astype(int)

# Drop unneeded columns for ML modeling
cleaned_data = sales.drop(columns=['date', 'datetime', 'card'])
print(cleaned_data.head())

# Save Cleaned data to new CSV
cleaned_data.to_csv('C:/Users/SAHIL/Unified Mentor/Project (Data Analyst)/Coffee sales/cleaned_coffee_sales.csv', index=False)

# Data Cleaning Done


