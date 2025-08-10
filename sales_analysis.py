import pandas as pd
import matplotlib.pyplot as plt

# Load the daily sales data from the CSV file
sales_daily = pd.read_csv('salesdaily.csv')

# --- Data Preparation ---

# Convert the 'datum' column from text to datetime objects for proper time-series analysis
sales_daily['datum'] = pd.to_datetime(sales_daily['datum'], format='%m/%d/%Y')

# Define the list of product category columns
product_cols = ['M01AB', 'M01AE', 'N02BA', 'N02BE', 'N05B', 'N05C', 'R03', 'R06']

# Create a 'Total Sales' column by summing up the sales of all product categories for each day
sales_daily['Total Sales'] = sales_daily[product_cols].sum(axis=1)

# --- Visualizations ---

# 1. Time-Series Analysis: Daily Sales Trend
# Create a new figure for the plot with a specified size
plt.figure(figsize=(12, 6))
# Plot the 'Total Sales' against the 'datum'
plt.plot(sales_daily['datum'], sales_daily['Total Sales'], label='Total Daily Sales')
# Add a title and labels for the axes
plt.title('Total Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales')
# Add a legend to identify the plotted line
plt.legend()
# Add a grid for better readability
plt.grid(True)
# Save the plot as a PNG image
plt.savefig('daily_sales_trend.png')

# 2. Sales by Weekday
# Group the data by 'Weekday Name', sum the 'Total Sales' for each day, and sort the results
weekday_sales = sales_daily.groupby('Weekday Name')['Total Sales'].sum().sort_values(ascending=False)
# Create a new figure for the plot
plt.figure(figsize=(10, 6))
# Create a bar chart of the weekday sales
weekday_sales.plot(kind='bar')
# Add a title and labels
plt.title('Total Sales by Weekday')
plt.xlabel('Weekday')
plt.ylabel('Total Sales')
# Rotate the x-axis labels for better visibility
plt.xticks(rotation=45)
# Save the plot
plt.savefig('weekday_sales.png')

# 3. Sales by Product Category
# Sum the sales for each product category across all days and sort them
product_sales = sales_daily[product_cols].sum().sort_values(ascending=False)
# Create a new figure
plt.figure(figsize=(10, 6))
# Create a bar chart of the product sales
product_sales.plot(kind='bar')
# Add a title and labels
plt.title('Total Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
# Rotate the x-axis labels
plt.xticks(rotation=45)
# Save the plot
plt.savefig('product_sales.png')

# 4. Monthly Sales Performance
# Set the 'datum' column as the index and resample the data by month ('M'), summing the sales for each month
monthly_sales = sales_daily.set_index('datum').resample('M')['Total Sales'].sum()
# Create a new figure
plt.figure(figsize=(12, 6))
# Create a bar chart of the monthly sales
monthly_sales.plot(kind='bar')
# Add a title and labels
plt.title('Total Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Total Sales')
# Rotate the x-axis labels
plt.xticks(rotation=90)
# Save the plot
plt.savefig('monthly_sales.png')

# --- KPI Calculation ---

# Calculate the total sales by summing the 'Total Sales' column
total_sales_kpi = sales_daily['Total Sales'].sum()
# Print the total sales KPI using an f-string for formatting
print(f'Total Sales: {total_sales_kpi}')
