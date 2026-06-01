import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Data/cleaned_students.csv")

# 1. Grade Distribution
plt.figure(figsize=(8, 5))
df["Grade"].value_counts().plot(kind="bar")
plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.savefig("Charts/grade_distribution.png")

# 2. Attendance vs Total Score
plt.figure(figsize=(8, 5))
plt.scatter(df["Attendance (%)"], df["Total_Score"])
plt.title("Attendance vs Total Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Total Score")
plt.savefig("Charts/attendance_vs_score.png")

# 3. Study Hours vs Total Score
plt.figure(figsize=(8, 5))
plt.scatter(df["Study_Hours_per_Week"], df["Total_Score"])
plt.title("Study Hours vs Total Score")
plt.xlabel("Study Hours per Week")
plt.ylabel("Total Score")
plt.savefig("Charts/study_hours_vs_score.png")

# 4. Stress Level vs Total Score
plt.figure(figsize=(8, 5))
plt.scatter(df["Stress_Level (1-10)"], df["Total_Score"])
plt.title("Stress Level vs Total Score")
plt.xlabel("Stress Level")
plt.ylabel("Total Score")
plt.savefig("Charts/stress_vs_score.png")

# 5. Sleep Hours vs Total Score
plt.figure(figsize=(8, 5))
plt.scatter(df["Sleep_Hours_per_Night"], df["Total_Score"])
plt.title("Sleep Hours vs Total Score")
plt.xlabel("Sleep Hours per Night")
plt.ylabel("Total Score")
plt.savefig("Charts/sleep_vs_score.png")

# Display all charts
plt.show()

print("All charts created and saved successfully!")