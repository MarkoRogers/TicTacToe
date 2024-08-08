import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the data manually based on the provided image
data = {
    "Row ID": [1, 2, 3, 4, 5],
    "Order ID": [
        "CA-2016-152156", "CA-2016-152156", "CA-2016-138688", "US-2015-108966", "US-2015-108966"
    ],
    "Order Date": [
        "08.11.2016", "08.11.2016", "12.06.2016", "11.10.2015", "11.10.2015"
    ],
    "Ship Date": [
        "11.11.2016", "11.11.2016", "16.06.2016", "18.10.2015", "18.10.2015"
    ],
    "Delivery Duration": [3, 3, 4, 7, 7],
    "Category": ["Furniture", "Furniture", "Office Supplies", "Furniture", "Office Supplies"],
    "Sales": [261.96, 731.94, 14.62, 957.5775, 22.368],
    "Profit": [41.9136, 219.582, 6.8714, -383.031, 2.5164],
    "Customer Name": ["Claire Gute", "Claire Gute", "Darrin Van Huff", "Sean O'Donnell", "Sean O'Donnell"],
    "Discount": [0, 0, 0, 0.45, 0.2]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Sales by Category
plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Sales', data=df, ci=None)
plt.title('Sales by Category')
plt.ylabel('Sales')
plt.xlabel('Category')
plt.show()

# Profit by Customer
plt.figure(figsize=(10, 6))
sns.barplot(x='Customer Name', y='Profit', data=df, ci=None)
plt.title('Profit by Customer')
plt.ylabel('Profit')
plt.xlabel('Customer Name')
plt.show()

# Discount vs Sales
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Discount', y='Sales', data=df)
plt.title('Discount vs Sales')
plt.ylabel('Sales')
plt.xlabel('Discount')
plt.show()
