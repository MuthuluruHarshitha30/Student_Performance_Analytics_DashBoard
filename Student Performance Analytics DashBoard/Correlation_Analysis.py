import pandas as pd

df = pd.read_csv("Data/cleaned_students.csv")

columns = [
    "Attendance (%)",
    "Study_Hours_per_Week",
    "Stress_Level (1-10)",
    "Sleep_Hours_per_Night",
    "Total_Score"
]

correlation = df[columns].corr()

print("Correlation Matrix:")
print(correlation)