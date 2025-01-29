import pandas as pd
import numpy as np

data = {
    'Name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'Diana Prince', 'Evan Wright'],
    'Age': [28, 34, 45, 23, 31],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
    'Salary': [65000, 72000, 58000, 89000, 68000],
    'Join_Date': pd.date_range(start='2020-01-01', periods=5, freq='ME'),
    'Department': ['HR', 'Tech', 'Marketing', 'Tech', 'Finance']
}


df = pd.DataFrame(data)

# iterate over rows
for index, row in df.iterrows():
    print(row['Name'], row['Age'], row['City'],
          row['Salary'], row['Join_Date'], row['Department'])

# iterate over columns
for col, col_data in df.items():
    print(col, col_data)


# iterate over tuples

for row in df.itertuples():
    print(row, type(row))