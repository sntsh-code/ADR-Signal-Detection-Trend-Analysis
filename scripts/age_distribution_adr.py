import pandas as pd

file_path = r"C:\Users\USER\Documents\DATA ANALYST\PROJECTS\Resume Projects\Project 1 ADR Signal Detection & Trend Analysis\cleaned_data\FAERS_2025_clean.csv"

# Step 1: Read CSV with auto-detect for delimiter
with open(file_path, 'r', encoding='latin1') as f:
    first_line = f.readline()
    print("First line of CSV:", first_line)

# Step 2: Identify delimiter
# If it looks like commas separate columns, use sep=','

# Step 3: Read CSV correctly
df = pd.read_csv(file_path, sep=',', encoding='utf-8-sig', low_memory=False)

# Step 4: Clean column names
df.columns = df.columns.str.strip()

# Step 5: Check 'sex' column (FAERS uses lowercase sometimes)
if 'sex' not in df.columns:
    print("Column 'sex' not found. Available columns are:")
    print(df.columns)
    exit()

# Step 6: Count gender
gender_counts = df['sex'].value_counts(dropna=False)
gender_percent = (gender_counts / gender_counts.sum()) * 100

print("Gender Counts:\n", gender_counts)
print("\nGender Percentages:\n", gender_percent)


# Step 7: Optional - save results to CSV
output_path = r"C:\Users\USER\Documents\DATA ANALYST\PROJECTS\Resume Projects\Project 1 ADR Signal Detection & Trend Analysis\data_analysis\gender_adr_contribution.csv"
gender_summary = pd.DataFrame({'Count': gender_counts, 'Percentage': gender_percent})
gender_summary.to_csv(output_path)
print(f"\nGender contribution saved to {output_path}")