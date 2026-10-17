
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV dataset
df = pd.read_csv("students.csv")

# Display the first five rows
print("\n--- First Five Rows ---")
print(df.head())

# Display dataset shape
print("\n--- Dataset Shape ---")
print("Rows and columns:", df.shape)

# Display dataset information
print("\n--- Dataset Information ---")
df.info()

# Display summary statistics
print("\n--- Summary Statistics ---")
print(df.describe())

# Find highest and lowest marks
print("\n--- Marks Analysis ---")
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
print("Average Marks:", df["Marks"].mean())

# Find the top student
top_student = df.loc[df["Marks"].idxmax(), "Name"]
print("Top Student:", top_student)

# Set a consistent chart style
sns.set_theme(style="whitegrid")

# Create and save the bar chart
plt.figure(figsize=(9, 5))
sns.barplot(data=df, x="Name", y="Marks")
plt.title("Student Marks Analysis")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("student_marks.png")
plt.show()
plt.close()

# Create and save the histogram
plt.figure(figsize=(9, 5))
sns.histplot(data=df, x="Marks", bins=5, kde=True)
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("marks_distribution.png")
plt.show()
plt.close()

print("\nAnalysis completed successfully!")
print("Charts saved as PNG files.")
