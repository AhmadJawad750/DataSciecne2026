import pandas as pd

data = {
    'Name': ['Ali', 'Sara', 'Ahmed'],
    'Marks': [80, 90, 85]
}

df = pd.DataFrame(data)

print("Full Data:")
print(df)

print("\nTop 2 Students:")
print(df.head(2))

print("\nData Info:")
print(df.info())