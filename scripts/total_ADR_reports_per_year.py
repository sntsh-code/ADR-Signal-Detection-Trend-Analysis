import pandas as pd

# Load cleaned FAERS file
file_path = r"C:\Users\USER\Documents\DATA ANALYST\PROJECTS\Resume Projects\Project 1 ADR Signal Detection & Trend Analysis\cleaned_data\FAERS_2025_clean.csv"
df = pd.read_csv(file_path)

# Check column names
print(df.columns)

# Look at the first few rows
print(df.head())

# Extract Year from Column 
df['YEAR'] = pd.to_datetime(df['init_fda_dt'], errors='coerce').dt.year

# Count of ADR per Year
year_adr_count = df.groupby('YEAR').size().reset_index(name='Total_ADR_Reports')

# Sort by year
year_adr_count = year_adr_count.sort_values('YEAR')

print(year_adr_count)

# Saving ADR Report
year_adr_count.to_csv(r"C:\Users\USER\Documents\DATA ANALYST\PROJECTS\Resume Projects\Project 1 ADR Signal Detection & Trend Analysis\adr_reports_per_year.csv", index=False)
print("Saved Successfully")
