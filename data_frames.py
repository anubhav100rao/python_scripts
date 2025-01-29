import pandas as pd

data = {
    'name': ['John', 'Anna', 'Peter', 'Linda'],
    'location': ['New York', 'Paris', 'Berlin', 'London'],
    'age': [24, 13, 53, 33],
    'gender': ['M', 'F', 'M', 'F'],
    'married': [True, False, True, False]
}

df = pd.DataFrame(data)

# print(df)
# print(df.loc[0])
# print(df.iloc[0, 0])
# print(df['name'][0])

# for key, value in df.items():
#     print(f"key: {key}, value: {value}")

print(df.index)
