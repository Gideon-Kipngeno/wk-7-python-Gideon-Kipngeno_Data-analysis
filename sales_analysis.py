# Importing necessary libraries
import pandas as pd  # Used for loading, cleaning, and analyzing tabular data
import matplotlib.pyplot as plt  # Used for creating basic visualizations like line, bar, and histogram plots
import seaborn as sns  # Adds styling and advanced plotting capabilities (especially for scatter plots)

# -------------------------------
# Task 1: Load and Explore the Dataset
# -------------------------------

try:
    # Load the CSV file using ISO-8859-1 encoding to avoid UnicodeDecodeError
    df = pd.read_csv('sales_data_sample.csv', encoding='ISO-8859-1') 
    
    # Show the first 5 rows to preview the dataset
    print(df.head())
    
    # Display column names, data types, and non-null counts
    print(df.info())
    
    # Show how many missing values exist in each column
    print(df.isnull().sum())
    
    # Drop any rows that contain missing values to ensure clean analysis
    df.dropna(inplace=True)

# Handle errors gracefully if the file is missing or unreadable
except FileNotFoundError:
    print("File not found. Make sure the path is correct.")
except UnicodeDecodeError:
    print("Encoding error. Try using 'ISO-8859-1' or 'cp1252'.")

# -------------------------------
# Task 2: Basic Data Analysis
# -------------------------------

# Print summary statistics (mean, std, min, max, etc.) for all numeric columns
print("\nDescriptive Statistics:")
print(df.describe())

# Group the data by 'DEALSIZE' (categorical column: Small, Medium, Large)
# Then calculate the average 'SALES' for each group
print("\nAverage Sales by Deal Size:")
grouped = df.groupby('DEALSIZE')['SALES'].mean()
print(grouped)

# -------------------------------
# Task 3: Data Visualization
# -------------------------------

# Convert the 'ORDERDATE' column to datetime format
# 'errors="coerce"' replaces invalid dates with NaT (Not a Time)
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')

# Sort the dataset by date so the line chart appears in chronological order
df.sort_values('ORDERDATE', inplace=True)

# Line Chart: Sales Over Time
plt.figure(figsize=(10, 5))  # Set the size of the plot
plt.plot(df['ORDERDATE'], df['SALES'], color='blue')  # Plot sales against order date
plt.title('Sales Over Time')  # Add a title to the chart
plt.xlabel('Order Date')  # Label the x-axis
plt.ylabel('Sales Amount')  # Label the y-axis
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Prevent label overlap
plt.show()  # Display the chart

# Bar Chart: Average Sales by Product Line
plt.figure(figsize=(8, 5))  # Set plot size
df.groupby('PRODUCTLINE')['SALES'].mean().plot(kind='bar', color='green')  # Group and plot
plt.title('Average Sales by Product Line')  # Chart title
plt.ylabel('Sales Amount')  # Y-axis label
plt.xticks(rotation=45)  # Rotate x-axis labels
plt.tight_layout()
plt.show()

# Histogram: Distribution of Unit Prices
plt.figure(figsize=(8, 5))
df['PRICEEACH'].plot(kind='hist', bins=20, color='purple')  # Plot histogram with 20 bins
plt.title('Unit Price Distribution')  # Chart title
plt.xlabel('Price Each')  # X-axis label
plt.tight_layout()
plt.show()

# Scatter Plot: Quantity Ordered vs Sales Amount
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='QUANTITYORDERED', y='SALES', hue='COUNTRY')  # Color points by country
plt.title('Quantity Ordered vs Sales Amount')  # Chart title
plt.xlabel('Quantity Ordered')  # X-axis label
plt.ylabel('Sales Amount')  # Y-axis label
plt.tight_layout()
plt.show()
