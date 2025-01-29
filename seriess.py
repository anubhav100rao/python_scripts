import pandas as pd

numbers = pd.Series([
    {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5
    },
    {
        "apple": 1,
        "banana": 2,
        "cherry": 3,
        "date": 4,
        "elderberry": 5
    },
    {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5
    }
], index=["numbers", "fruits", "letters"])

print(numbers)

for key, value in numbers.items():
    print(f"key: {key}, value: {value}")

print(numbers.loc['numbers'])
print(numbers.iloc[0])
