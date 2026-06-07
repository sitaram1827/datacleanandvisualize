import os
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. LOAD DATASET (Universal Setup)
# ==========================================
file_name = 'raw_data.csv' 

if not os.path.exists(file_name):
    raise FileNotFoundError(f"Could not find '{file_name}'. Please ensure it's in the same folder as this script.")

df = pd.read_csv(file_name)

print("==========================================")
print("   ORIGINAL DATASET PREVIEW (FIRST 5 ROWS) ")
print("==========================================")
print(df.head())
print(f"Total Rows: {len(df)} | Total Columns: {len(df.columns)}\n")

# ==========================================
# 2. CLEAN & PROCESS DATA
# ==========================================
# Check missing values
print("--- Missing Values Found Per Column ---")
print(df.isnull().sum())

# Handle missing values (Fills numeric with median, text with 'Unknown')
for col in df.columns:
    if df[col].dtype in ['int64', 'float64']:
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna('Unknown')

# Remove duplicate rows
duplicate_count = df.duplicated().sum()
df = df.drop_duplicates()
print(f"\nDuplicate Rows Removed: {duplicate_count}")

# ==========================================
# 3. CLEANED DATASET PREVIEW & EXPORT
# ==========================================
print("\n==========================================")
print("   CLEANED DATASET PREVIEW (FIRST 5 ROWS) ")
print("==========================================")
print(df.head())
print(f"Final Rows remaining: {len(df)}")
print("==========================================\n")

# Export to a brand new CSV
cleaned_file_name = 'cleaned_data.csv'
df.to_csv(cleaned_file_name, index=False)
print(f"Success! Cleaned dataset exported locally as: '{cleaned_file_name}'\n")

# ==========================================
# 4. DUAL-AXIS SIDE-BY-SIDE VISUALIZATION
# ==========================================
# Dynamically select columns for plotting
x_axis_col = df.columns[0] 
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

if len(numeric_cols) < 2:
    raise ValueError("The dataset needs at least two numeric columns to generate a dual-axis chart.")

# Select the first two available numeric columns for comparison
col1, col2 = numeric_cols[0], numeric_cols[1]

# Set up the figure and the first axis (ax1)
fig, ax1 = plt.subplots(figsize=(12, 6))

# Width of bars and offsets
width = 0.35
x_indexes = range(len(df[x_axis_col]))

# Plot first metric on Left Y-Axis (ax1)
bar1 = ax1.bar([x - width/2 for x in x_indexes], df[col1], width=width, color='royalblue', label=col1)
ax1.set_xlabel(x_axis_col, fontweight='bold', labelpad=10)
ax1.set_ylabel(col1, color='royalblue', fontweight='bold')
ax1.tick_params(axis='y', labelcolor='royalblue')
ax1.set_xticks(x_indexes)
ax1.set_xticklabels(df[x_axis_col], rotation=45)

# Create the second axis (ax2) sharing the same x-axis
ax2 = ax1.twinx()

# Plot second metric on Right Y-Axis (ax2)
bar2 = ax2.bar([x + width/2 for x in x_indexes], df[col2], width=width, color='darkorange', label=col2)
ax2.set_ylabel(col2, color='darkorange', fontweight='bold')
ax2.tick_params(axis='y', labelcolor='darkorange')

# Combined Legend for both axes
bars = [bar1, bar2]
labels = [b.get_label() for b in bars]
ax1.legend(bars, labels, loc='upper left')

# Layout and Title adjustments
plt.title(f"Comparison of {col1} vs {col2} by {x_axis_col}", fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()

# Render plot
plt.show()