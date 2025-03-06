import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("cleaned_data.csv")

# Set seaborn style
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 1️⃣ Histogram + KDE
sns.histplot(df['value'], kde=True, bins=30, ax=axes[0, 0], color="blue")
axes[0, 0].set_title("Distribution of Hospital Readmission Values")
axes[0, 0].set_xlabel("Readmission Value")
axes[0, 0].set_ylabel("Frequency")

# 2️⃣ Boxplot
sns.boxplot(x=df['value'], ax=axes[0, 1], color="skyblue")
axes[0, 1].set_title("Boxplot of Readmission Values")
axes[0, 1].set_xlabel("Readmission Value")

# 3️⃣ Violin Plot by Primary Race (if available)
if 'primary_race' in df.columns:
    sns.violinplot(x='primary_race', y='value', data=df, ax=axes[1, 0], palette="muted")
    axes[1, 0].set_title("Readmission Values by Race")
    axes[1, 0].set_xlabel("Race")
    axes[1, 0].set_ylabel("Readmission Value")
    axes[1, 0].tick_params(axis='x', rotation=45)

# 4️⃣ Trend Over Time (if year column exists)
if 'year' in df.columns:
    df_grouped = df.groupby("year")["value"].mean().reset_index()
    sns.lineplot(x='year', y='value', data=df_grouped, marker="o", ax=axes[1, 1], color="red")
    axes[1, 1].set_title("Average Readmission Value Over Time")
    axes[1, 1].set_xlabel("Year")
    axes[1, 1].set_ylabel("Average Readmission Value")

plt.tight_layout()
plt.show()