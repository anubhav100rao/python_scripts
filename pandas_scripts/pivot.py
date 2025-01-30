import pandas as pd
import numpy as np

# Create sample sales data
data = {
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'Product': ['Electronics', 'Furniture', 'Electronics', 'Furniture',
                'Electronics', 'Furniture', 'Electronics', 'Furniture'],
    'Sales': [1500, 2200, 1300, 2400, 1600, 2100, 1450, 2300],
    'Quantity': [15, 22, 13, 24, 16, 21, 14, 23],
    'Month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar', 'Apr', 'Apr'],
    'Customer_Rating': [4.5, 3.8, 4.2, 4.7, 4.1, 4.0, 4.6, 4.3]
}

df = pd.DataFrame(data)

pivot1 = pd.pivot_table(df,
                        values='Sales',
                        index='Region',
                        columns='Product',
                        aggfunc='mean')
print("\nBasic Pivot Table:")
print(pivot1)


pivot2 = pd.pivot_table(df,
                        values='Sales',
                        index='Region',
                        columns='Product',
                        aggfunc=['sum', 'mean'],
                        fill_value=0)
print("\nMultiple Aggregations:")
print(pivot2)

pivot3 = pd.pivot_table(df,
                        values=['Sales', 'Quantity'],
                        index=['Region', 'Product'],
                        aggfunc={'Sales': 'mean', 'Quantity': 'sum'})
print("\nMultiple Values:")
print(pivot3)


ct1 = pd.crosstab(index=df['Region'],
                  columns=df['Product'],
                  rownames=['Region'],
                  colnames=['Product Category'])
print("\nCross Tab - Frequency:")
print(ct1)
