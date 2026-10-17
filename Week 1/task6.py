
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dataset with missing values
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Hina", "Usman"],
    "Marks": [85, 92, None, 78, 95, 88],
    "Age": [20, 21, 19, None, 21, 22]
}

df = pd.DataFrame(data)

# Display the original dataset
print("--- Dataset Before Cleaning ---")
print(df)

# Display missing values count
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Plot marks before cleaning
sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 4))
sns.barplot(data=df, x="Name", y="Marks")
plt.title("Student Marks Before Cleaning")
plt.tight_layout()
plt.savefig("before_cleaning.png")
plt.show()
plt.close()

# Fill missing values with column averages
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Display cleaned dataset
print("\n--- Dataset After Cleaning ---")
print(df)

# Display missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Plot marks after cleaning
plt.figure(figsize=(8, 4))
sns.barplot(data=df, x="Name", y="Marks")
plt.title("Student Marks After Cleaning")
plt.tight_layout()
plt.savefig("after_cleaning.png")
plt.show()
plt.close()

print("\nData cleaning completed successfully!")
print("Charts saved as PNG files.")
