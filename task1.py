import pandas as pd

file_path = 'A.csv'
df = pd.read_csv(file_path)

print(df.head())

print(df.info())

print(df.describe())