import pandas as pd

# Load File

file_path = r"C:\Users\USER\Documents\DATA ANALYST\PROJECTS\Resume Projects\Project 1 ADR Signal Detection & Trend Analysis\cleaned_data\FAERS_2025_clean.csv"
df = pd.read_csv(file_path)

#Checking Column
print(df.columns)

# Count the Country Occurrance
adr_occurrence = df['occr_country'].value_counts().reset_index()
adr_occurrence.columns = ['ADR', 'Occurance']

# Top 10 Country with ADR
print(adr_occurrence.head(10))

# Saving File
adr_occurrence.to_csv(r"C:\Users\USER\Documents\DATA ANALYST\PROJECTS\Resume Projects\Project 1 ADR Signal Detection & Trend Analysis\top_adr_by_countries.csv", index=False)
print("Saved Successfuly")