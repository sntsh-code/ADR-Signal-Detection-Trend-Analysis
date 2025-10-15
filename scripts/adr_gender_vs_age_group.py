# Importing Important Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned FAERS dataset
file_path = r"C:\Users\USER\Documents\DATA ANALYST\PROJECTS\Resume Projects\Project 1 ADR Signal Detection & Trend Analysis\cleaned_data\FAERS_2025_clean.csv"
df = pd.read_csv(file_path)

# Verifying Column Values 
print(df['sex'].unique())
print(df['age_grp'].unique())

# ADR distribution by gender
gender_dist = df['sex'].value_counts(normalize = True).round(3) * 100
print("Adr Distribution by Gender (%):")
print(gender_dist)

# ADR distribution by age
age_dist = df['age_grp'].value_counts(normalize = True).round(3) * 100
print("Adr Distribution by Age (%):")
print(age_dist)

# Cross Analysis- Age group vs. Gender
cross_table = pd.crosstab(df['age_grp'], df['sex'], normalize='index').round(3) * 100
print("ADR Distribution by Age Group and Gender (%):")
print(cross_table)

# Visualization
# Gender-wise ADRs
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='sex', palette='pastel')
plt.title('ADR Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('ADR Count')
plt.show()

# Age group-wise ADRs
plt.figure(figsize=(8,4))
sns.countplot(data=df, x='age_grp', palette='Set2', order=df['age_grp'].value_counts().index)
plt.title('ADR Distribution by Age Group')
plt.xlabel('Age Group')
plt.ylabel('ADR Count')
plt.show()

# Cross: Gender vs Age Group
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='age_grp', hue='sex', palette='coolwarm')
plt.title('ADR Distribution by Age Group and Gender')
plt.xlabel('Age Group')
plt.ylabel('ADR Count')
plt.show()

# Saving Summary Tables
summary = pd.DataFrame({
    'Gender_Distribution_%': gender_dist,
})
summary.to_csv('gender_distribution_summary.csv')

cross_table.to_csv('age_gender_distribution_summary.csv')



