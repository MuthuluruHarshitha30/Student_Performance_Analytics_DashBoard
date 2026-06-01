import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Data/cleaned_students.csv")

columns = [
    "Attendance (%)",
    "Study_Hours_per_Week",
    "Stress_Level (1-10)",
    "Sleep_Hours_per_Night",
    "Total_Score"
]

corr = df[columns].corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True)

plt.title("Correlation Heatmap")
plt.savefig("Charts/correlation_heatmap.png")
plt.show()