import pandas as pd

# Load cleaned FAERS dataset
file_path = r"C:\Users\USER\Documents\DATA ANALYST\PROJECTS\Resume Projects\Project 1 ADR Signal Detection & Trend Analysis\cleaned_data\FAERS_2025_clean.csv"
df = pd.read_csv(file_path)

# Define serious outcome codes based on FDA standard
serious_codes = ['DE', 'LT', 'HO', 'DS', 'CA', 'RI', 'OT']

# Classify each record
df['SERIOUSNESS'] = df['outc_cod'].apply(lambda x: 'Serious' if x in serious_codes else 'Non-Serious')

# Count each category
serious_counts = df['SERIOUSNESS'].value_counts().reset_index()
serious_counts.columns = ['Seriousness', 'Count']

# Calculate ratio and percentages
serious = serious_counts.loc[serious_counts['Seriousness'] == 'Serious', 'Count'].values[0]
non_serious = serious_counts.loc[serious_counts['Seriousness'] == 'Non-Serious', 'Count'].values[0]
ratio = serious / non_serious
total = serious + non_serious
serious_pct = (serious / total) * 100
non_serious_pct = (non_serious / total) * 100

# Prepare summary dataframe
ratio_summary = pd.DataFrame({
    'Metric': ['Serious Reports', 'Non-Serious Reports', 'Serious:Non-Serious Ratio', 'Serious %', 'Non-Serious %'],
    'Value': [serious, non_serious, f"{ratio:.2f}:1", f"{serious_pct:.2f}%", f"{non_serious_pct:.2f}%"]
})

# Save to CSV
ratio_summary.to_csv(r"C:\Users\USER\Documents\DATA ANALYST\PROJECTS\Resume Projects\Project 1 ADR Signal Detection & Trend Analysis\cleaned_data\serious_ratio_summary.csv", index=False)

print("Serious vs Non-Serious ratio summary saved successfully!")
print(ratio_summary)

