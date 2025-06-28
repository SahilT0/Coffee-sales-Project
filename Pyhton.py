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


# Checking for outliers
print(cleaned_data['money'].value_counts().sort_index())
print(cleaned_data['money'].describe())
# Money value 18.12 has 10 counts
print(cleaned_data[cleaned_data['money'] == 18.12])

# removing these 10 rows
cleaned_data = cleaned_data[cleaned_data['money'] != 18.12]
print(cleaned_data.shape)


# Visualization part

# 1. Sales by Coffee Type
sns.boxplot(x='coffee_name', y='money', data=cleaned_data)
plt.title('Price Distribution per Coffee Type')
plt.show()

# 2. Sales by Hour
cleaned_data.groupby('hours')['money'].sum().plot(kind='line', marker='o', title='Sales Trend by Hour of Day')
plt.xlabel('Hour')
plt.ylabel('Total Sales')
plt.grid()
plt.show()

# 3. Payment Mode
plt.pie(cleaned_data['cash_type'].value_counts(), colors=sns.color_palette('pastel'), autopct="%1.1f%%", labels=['Card', 'Cash'])
plt.title("Payment type distribution")
plt.show()

# 4. Sales by Day of the Week
sns.barplot(x='day', y='money', data=cleaned_data, palette='viridis')
plt.title("Total Sales by Day of the Week")
plt.ylabel("Sales")
plt.show()

# 5.Customer Frequency
sns.scatterplot(x='customer_frequency', y='money', data=cleaned_data)
plt.title('Customer Frequency vs Sales Amount')
plt.xlabel('Customer Frequency')
plt.ylabel('Sales')
plt.show()

# 6. Monthly Sales Trend
cleaned_data.groupby('month')['money'].sum().plot(kind='line', marker='+', title='Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()


# Data Preprocessing Part

print(cleaned_data.head(10))

# Adding new feature is_weekend
weekend_days = ['Saturday', 'Sunday']
cleaned_data['is_weekend'] = cleaned_data['day'].apply(lambda x: 1 if x in weekend_days else 0)
print(cleaned_data[['day', 'is_weekend']].head(20))

# Encoding Categorical column
data = pd.get_dummies(cleaned_data, columns=['cash_type', 'coffee_name', 'month', 'day'], drop_first=False)
print(data.shape)
print(data.head(3))


# Features and Target
X = data.drop(columns=['money'])
y = data['money']

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)



























