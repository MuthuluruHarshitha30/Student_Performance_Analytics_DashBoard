import pandas as pd

df = pd.read_csv("Data/cleaned_students.csv")

print("Total Students:", len(df))

print("Average Total Score:", round(df["Total_Score"].mean(),2))

print("Average Attendance:", round(df["Attendance (%)"].mean(),2))

print("Average Study Hours:", round(df["Study_Hours_per_Week"].mean(),2))

print("\nGrade Distribution:")
print(df["Grade"].value_counts())