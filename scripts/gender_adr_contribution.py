import pandas as pd

# File path to your cleaned FAERS CSV
file_path = r"C:\Users\USER\Documents\DATA ANALYST\PROJECTS\Resume Projects\Project 1 ADR Signal Detection & Trend Analysis\cleaned_data\FAERS_2025_clean.csv"

# Step 1: Read CSV safely
try:
    df = pd.read_csv(file_path, sep='$', encoding='latin1', low_memory=False)
except Exception as e:
    print("Error reading CSV:", e)
    exit()

# Step 2: Clean column names (remove extra spaces)
df.columns = df.columns.str.strip()

# Step 3: Check if 'sex' column exists (FAERS usually uses uppercase)
if 'sex' not in df.columns:
    print("Column 'sex' not found in dataset. Available columns:")
    print(df.columns)
    exit()

# Step 4: Count reports by gender
gender_counts = df['sex'].value_counts(dropna=False)

# Step 5: Calculate percentages
gender_percent = (gender_counts / gender_counts.sum()) * 100

# Step 6: Display results
print("Gender Counts:\n", gender_counts)
print("\nGender Percentage:\n", gender_percent)

# Step 7: Optional - save results to CSV
output_path = r"C:\Users\USER\Documents\DATA ANALYST\PROJECTS\Resume Projects\Project 1 ADR Signal Detection & Trend Analysis\data_analysis\gender_adr_contribution.csv"
gender_summary = pd.DataFrame({'Count': gender_counts, 'Percentage': gender_percent})
gender_summary.to_csv(output_path)
print(f"\nGender contribution saved to {output_path}")
