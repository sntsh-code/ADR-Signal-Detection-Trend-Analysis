import pandas as pd

# Load File Data
file_path = r"C:\Users\USER\Documents\DATA ANALYST\PROJECTS\Resume Projects\Project 1 ADR Signal Detection & Trend Analysis\cleaned_data\FAERS_2025_clean.csv"
df = pd.read_csv(file_path)

# Checking Database
print(df.columns)

# Count the frequency of each ADR

adr_frequency = df['pt'].value_counts().reset_index()
adr_frequency.columns = ['ADR', 'Frequency']

# Show top 10 ADR Frequency
print(adr_frequency.head(10))

# Saving File 
adr_frequency.to_csv(r"C:\Users\USER\Documents\DATA ANALYST\PROJECTS\Resume Projects\Project 1 ADR Signal Detection & Trend Analysis\adr_reports_per_year.csv", index=False)
print("Saved Successfuly")