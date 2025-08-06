import pandas as pd

# ============================
# Data Cleaning Project
# ============================
# Author: Monica Nieto
# Objective: Demonstrate data cleaning and preprocessing skills on a sample dataset
# Tools: Python, Pandas
# ============================

# Simulated dataset with intentional errors for demonstration purposes
data = {
    'Name': ['Ana', 'Luis', None, 'Carlos', 'Luis'],
    'Age': [25, None, 30, 22, 22],
    'City': ['Helsinki', 'Espoo', 'Tampere', None, 'Espoo'],
    'Salary': ['3000', 'NaN', '2500', '4000', '4000']
}

df = pd.DataFrame(data)

print("=== Original Dataset ===")
print(df)

# ----------------------------
# Step 1: Remove duplicate rows
# ----------------------------
df = df.drop_duplicates()

# ----------------------------
# Step 2: Handle missing values
# Fill missing 'Age' values with the mean of the column
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill missing 'City' values with 'Unknown'
df['City'] = df['City'].fillna('Unknown')

# ----------------------------
# Step 3: Convert data types
# Ensure 'Salary' is numeric, coercing errors
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

# Fill any remaining missing 'Salary' values with the median
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

# ----------------------------
# Step 4: Verify cleaned dataset
# ----------------------------
print("\n=== Cleaned Dataset ===")
print(df)

