import pandas as pd

df = pd.read_csv("Data/Students Performance Dataset.csv")

# Fill missing Parent Education values
df["Parent_Education_Level"] = df["Parent_Education_Level"].fillna("Unknown")

print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("Data/cleaned_students.csv", index=False)

print("Data cleaned successfully!")


