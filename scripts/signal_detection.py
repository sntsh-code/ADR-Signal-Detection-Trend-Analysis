import pandas as pd
import numpy as np

# -------------------- STEP 1: LOAD DATA --------------------
file_path = r"C:\Users\USER\Documents\DATA ANALYST\PROJECTS\Resume Projects\Project 1 ADR Signal Detection & Trend Analysis\cleaned_data\FAERS_2025_clean.csv"
df = pd.read_csv(file_path)
df.columns = df.columns.str.lower()

# -------------------- STEP 2: PREPARE COUNTS --------------------
N = len(df)
drug_total = df['drugname'].value_counts().to_dict()
event_total = df['pt'].value_counts().to_dict()

drug_event_pairs = df.groupby(['drugname', 'pt']).size().reset_index(name='a')

# -------------------- STEP 3: BUILD CONTINGENCY TABLE --------------------
contingency_list = []

for _, row in drug_event_pairs.iterrows():
    drug = row['drugname']
    reaction = row['pt']
    a = row['a']
    b = drug_total[drug] - a
    c = event_total[reaction] - a
    d = N - (a + b + c)
    contingency_list.append([drug, reaction, a, b, c, d])

contingency_df = pd.DataFrame(contingency_list, columns=['Drug', 'Reaction', 'a', 'b', 'c', 'd'])

# -------------------- STEP 4: CALCULATE SIGNAL METRICS --------------------
# Proportional Reporting Ratio (PRR)
contingency_df['PRR'] = (contingency_df['a'] / (contingency_df['a'] + contingency_df['b'])) / \
                        (contingency_df['c'] / (contingency_df['c'] + contingency_df['d']))

# Reporting Odds Ratio (ROR)
contingency_df['ROR'] = (contingency_df['a'] * contingency_df['d']) / (contingency_df['b'] * contingency_df['c'])

# Chi-square
contingency_df['Chi_square'] = ((contingency_df['a'] * contingency_df['d'] - contingency_df['b'] * contingency_df['c'])**2 * N) / \
                               ((contingency_df['a'] + contingency_df['b']) * (contingency_df['c'] + contingency_df['d']) * \
                                (contingency_df['a'] + contingency_df['c']) * (contingency_df['b'] + contingency_df['d']))

# Information Component (IC)
contingency_df['IC'] = np.log2((contingency_df['a'] * N) / ((contingency_df['a'] + contingency_df['b']) * (contingency_df['a'] + contingency_df['c'])))

# -------------------- STEP 5: CLEAN + FLAG SIGNALS --------------------
# Remove invalid or infinite values
contingency_df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Filter for meaningful data (Evans criteria)
contingency_df = contingency_df[(contingency_df['a'] >= 3) & (contingency_df['Chi_square'] >= 4)]

# Add a column flagging potential signals
contingency_df['Potential_Signal'] = np.where(contingency_df['ROR'] > 2, 'Potential Signal', 'No Signal')

# Sort strongest signals first
contingency_df_sorted = contingency_df.sort_values(by='ROR', ascending=False)

# # -------------------- STEP 6: SAVE RESULTS --------------------

contingency_df_sorted.to_csv(r"C:\Users\USER\Documents\DATA ANALYST\PROJECTS\Resume Projects\Project 1 ADR Signal Detection & Trend Analysis\adr_signal_results.csv", index=False)
print("Signal detection completed successfully.")
print(f"Results saved")
print("\nTop 10 Disproportionate Signals (ROR > 2 highlighted):")
print(contingency_df_sorted[['Drug', 'Reaction', 'a', 'PRR', 'ROR', 'Chi_square', 'IC', 'Potential_Signal']].head(10))
