import pandas as pd

df = pd.read_csv("data/swiggy.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Replace '--' with NaN
df.replace('--', pd.NA, inplace=True)

# Clean cost column (remove ₹ and spaces)
df['cost'] = df['cost'].str.replace('₹','', regex=False)
df['cost'] = df['cost'].str.strip()

# Convert cost to numeric
df['cost'] = pd.to_numeric(df['cost'], errors='coerce')

# Convert rating
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# Fill missing values
df['rating'].fillna(df['rating'].mean(), inplace=True)
df['cost'].fillna(df['cost'].median(), inplace=True)

df['city'].fillna("Unknown", inplace=True)
df['cuisine'].fillna("Unknown", inplace=True)

# Reset index
df.reset_index(drop=True, inplace=True)

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("Cleaning completed")
print(df.shape)
