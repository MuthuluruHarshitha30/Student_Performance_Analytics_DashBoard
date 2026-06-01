import pandas as pd

df = pd.read_csv("Data/Students Performance Dataset.csv")

print(df.head())
print("\nColumns:")
print(df.columns.to_list())

print("\nShape:")
print(df.shape)