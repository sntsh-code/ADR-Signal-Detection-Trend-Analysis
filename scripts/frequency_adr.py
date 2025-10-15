import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to your cleaned FAERS file
file_path = r"C:\Users\USER\Documents\DATA ANALYST\PROJECTS\Resume Projects\Project 1 ADR Signal Detection & Trend Analysis\cleaned_data\FAERS_2025_clean.csv"

# Step 1: Read CSV correctly
df = pd.read_csv(file_path, encoding='utf-8-sig', low_memory=False)

# Step 2: Clean column names
df.columns = df.columns.str.strip()

# Step 3: Check if 'outc_cod' column exists
if 'outc_cod' not in df.columns:
    print("Column 'outc_cod' not found. Available columns:")
    print(df.columns)
    exit()

# Step 4: Count frequency of each outcome code
outc_counts = df['outc_cod'].value_counts(dropna=False)
outc_percent = (outc_counts / outc_counts.sum()) * 100

# Step 5: Combine counts and percentages
outc_summary = pd.DataFrame({
    'Count': outc_counts,
    'Percentage': outc_percent
})

# Plot bar chart for outcome percentages
plt.figure(figsize=(10,6))
sns.barplot(x=outc_summary.index, y=outc_summary['Percentage'], palette='coolwarm')
plt.title('ADR Outcome Distribution (%)', fontsize=16)
plt.xlabel('Outcome Code', fontsize=12)
plt.ylabel('Percentage (%)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# Step 6: Display results
print("\nOutcome Code Summary:")
print(outc_summary)

# Step 7: Optional - save results to CSV
output_path = r"C:\Users\USER\Documents\DATA ANALYST\PROJECTS\Resume Projects\Project 1 ADR Signal Detection & Trend Analysis\outc_code_summary.csv"
outc_summary.to_csv(output_path)
print(f"\nOutcome code summary saved to {output_path}")
