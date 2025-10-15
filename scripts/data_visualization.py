# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: Improve plot aesthetics
sns.set(style="whitegrid")

# Step 2: Load Your Data
file_path = r"C:\Users\USER\Documents\DATA ANALYST\PROJECTS\Resume Projects\Project 1 ADR Signal Detection & Trend Analysis\cleaned_data\FAERS_2025_clean.csv"
df = pd.read_csv(file_path)

# Step 3: Quick Look at Data
print(df.head())
print(df.info())

# ------------------------------------------
# Visualization 1: Bar Chart - ADR reports per Drug
drug_counts = df['drugname'].value_counts().head(10)  # top 10 drugs
plt.figure(figsize=(10,6))
sns.barplot(x=drug_counts.values, y=drug_counts.index, palette='viridis')
plt.title("Top 10 Drugs with Most ADR Reports")
plt.xlabel("Number of ADR Reports")
plt.ylabel("Drug Name")
plt.show()

# ------------------------------------------
# Visualization 2: Line Chart - ADR reports over Years
reports_per_year = df.groupby('event_dt')['rept_dt'].count()
plt.figure(figsize=(10,6))
sns.lineplot(x=reports_per_year.index, y=reports_per_year.values, marker='o')
plt.title("ADR Reports Over Years")
plt.xlabel("Year")
plt.ylabel("Number of ADR Reports")
plt.show()

# ------------------------------------------
# Visualization 3: Pie Chart - Serious vs Non-Serious Cases
serious_counts = df['outc_cod'].value_counts()  # Column should be 0/1 or Yes/No
plt.figure(figsize=(6,6))
plt.pie(serious_counts, labels=serious_counts.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff'])
plt.title("Serious vs Non-Serious ADR Cases")
plt.show()

# ------------------------------------------
# Visualization 4: Histogram - Age Distribution
plt.figure(figsize=(10,6))
sns.histplot(df['age'], bins=20, kde=True, color='skyblue')
plt.title("Age Distribution of Patients Reporting ADRs")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# ------------------------------------------
# Visualization 5: Heatmap - Drug vs Reaction Frequency
drug_reaction = pd.crosstab(df['drugname'], df['pt'])
top_drugs = drug_reaction.sum(axis=1).sort_values(ascending=False).head(10).index
top_reactions = drug_reaction.sum(axis=0).sort_values(ascending=False).head(10).index
plt.figure(figsize=(12,8))
sns.heatmap(drug_reaction.loc[top_drugs, top_reactions], annot=True, fmt="d", cmap="YlGnBu")
plt.title("Heatmap: Top Drugs vs Top Reactions")
plt.show()
