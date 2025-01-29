import pandas as pd

df = pd.read_csv(
    '/Users/anubhav100rao/development/python_scripts/employee_data.csv')


# print(df.iloc[:3, :3])

print(df[df['Age'] > 40])