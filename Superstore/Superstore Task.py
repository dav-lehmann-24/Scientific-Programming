import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the dataset
df = pd.read_csv('Superstore Task.csv', na_values='N/A')
print("First 10 rows of the dataset: ")
print(df.head(10))
print("---------------------------------------------------------------------------------------------------------------")


# Display statistics of the dataset
print("\nStatistics of this dataset: ")
print(df.describe())
print("---------------------------------------------------------------------------------------------------------------")


# Check for missing values
miss_value = df.isnull().sum()
print("Missing values in the columns: ")
print(miss_value)
print("---------------------------------------------------------------------------------------------------------------")


# Change the datetime format
#df['order_date'] = pd.to_datetime(df['order_date'])
#df['ship_date'] = pd.to_datetime(df['ship_date'])
#df['order_date'] = df['order_date'].dt.strftime('%m.%d.%Y')
#df['ship_date'] = df['ship_date'].dt.strftime('%m.%d.%Y')
#df.to_csv('Superstore Task.csv', index=False)

#print("The datetime format has been changed to DD.MM.YYYY: ")
#print(df.head(10))
#print("---------------------------------------------------------------------------------------------------------------")


# Check if there is a column 'Revenue'
if 'Revenue' not in df.columns:
    df['Revenue'] = df['quantity'] * df['sales']

df.to_csv('Superstore Task.csv', index=False)
print(df.head(10))
print("---------------------------------------------------------------------------------------------------------------")


# Total generated revenue
total_revenue = df['Revenue'].sum()
print("Total revenue: " + str((round(total_revenue, 2))) + "€ \n")

# Top 5 products by total revenue
top_5_revenues = df.nlargest(5, 'Revenue')
result = top_5_revenues[['order_id', 'Revenue']]
print("Top 5 revenues: \n" + str(result) + "\n")

# Customer with the most orders
customer_order = df['customer'].value_counts().idxmax()
print("The customer with the most orders is: " + str(customer_order))
print("---------------------------------------------------------------------------------------------------------------")


# Group by 'Product' and calculate total quantity sold for each product
total_quantity_per_product = df.groupby('product_name')['quantity'].sum()
print("Total quantity per product: \n" + str(total_quantity_per_product) + "\n")

# Group data by order date and calculate daily revenue
daily_revenue = df.groupby('order_date')['Revenue'].sum()
print("Daily revenue trends: \n " + str(daily_revenue))
print("---------------------------------------------------------------------------------------------------------------")


# Plot a bar chart showing the top 5 products by revenue
product_revenue = df.groupby('product_name')['Revenue'].sum()
top_5_products = product_revenue.nlargest(5)
plt.figure(figsize=(10, 6))
top_5_products.plot(kind='bar')
plt.title('Top 5 products by revenue')
plt.xlabel('Product Name')
plt.ylabel('Revenue in €')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Create a line graph to visualize daily revenue trends
plt.figure(figsize=(12, 6))
plt.plot(daily_revenue.index, daily_revenue.values, linestyle='-', marker='o')
plt.title('Daily revenue trends')
plt.xlabel('Order Date')
plt.ylabel('Revenue in €')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
print("---------------------------------------------------------------------------------------------------------------")


# Column to calculate a 7-day moving average for daily revenue.
daily_revenue = df.groupby('order_date')['Revenue'].sum().reset_index()
daily_revenue['7-day moving average'] = daily_revenue['Revenue'].rolling(window=7).mean()
print("Daily revenue with seven day moving average: \n " + str(daily_revenue))

# Identify the day with the highest revenue and the product that contributed the most.
daily_revenue = df.groupby('order_date')['Revenue'].sum()
max_revenue_day = daily_revenue.idxmax()
max_revenue_amount = daily_revenue.max()
print("Day with the highest revenue: " + max_revenue_day)
highest_revenue_day_data = df[df['order_date'] == max_revenue_day]
top_product = highest_revenue_day_data.groupby('product_name')['Revenue'].sum().idxmax()
top_product_revenue = highest_revenue_day_data.groupby('product_name')['Revenue'].sum().max()
print("Product that contributed the most: " + top_product)