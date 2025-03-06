import pandas as pd

# Load dataset
df = pd.read_csv("cms readmission data race and ethnicity 2012 2020.csv")

# Show first few rows
print(df.head())
# Check basic dataset info
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Check summary statistics
print(df.describe())
# Drop rows with missing values (if any)
df_cleaned = df.dropna()

# Confirm missing values are gone
print(df_cleaned.isnull().sum())
# Rename columns for easier access
df_cleaned.columns = [col.lower().replace(" ", "_") for col in df_cleaned.columns]

# Print column names to confirm
print(df_cleaned.columns)
# Save cleaned data to a new CSV file
df_cleaned.to_csv("cleaned_data.csv", index=False)

print("Cleaned dataset saved as cleaned_data.csv")