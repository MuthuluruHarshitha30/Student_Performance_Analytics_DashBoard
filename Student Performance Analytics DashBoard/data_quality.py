import pandas as pd

df = pd.read_csv("Data/Students Performance Dataset.csv")

print("Missing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

