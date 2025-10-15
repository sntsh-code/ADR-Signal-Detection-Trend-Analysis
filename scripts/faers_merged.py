import pandas as pd
import os

# Base paths
base_path = r"C:\Users\USER\Documents\DATA ANALYST\PROJECTS\Resume Projects\Project 1 ADR Signal Detection & Trend Analysis"
raw_path = os.path.join(base_path, "raw_data")
clean_path = os.path.join(base_path, "cleaned_data")

# Read with low_memory=False to avoid dtype warnings
demo = pd.read_csv(f"{raw_path}\\DEMO25Q2.TXT", sep='$', encoding='latin1', low_memory=False)
drug = pd.read_csv(f"{raw_path}\\DRUG25Q2.TXT", sep='$', encoding='latin1', low_memory=False)
indication = pd.read_csv(f"{raw_path}\\INDI25Q2.TXT", sep='$', encoding='latin1', low_memory=False)
outcome = pd.read_csv(f"{raw_path}\\OUTC25Q2.TXT", sep='$', encoding='latin1', low_memory=False)
reaction = pd.read_csv(f"{raw_path}\\REAC25Q2.TXT", sep='$', encoding='latin1', low_memory=False)
source = pd.read_csv(f"{raw_path}\\RPSR25Q2.TXT", sep='$', encoding='latin1', low_memory=False)
therapy = pd.read_csv(f"{raw_path}\\THER25Q2.TXT", sep='$', encoding='latin1', low_memory=False)

# Normalize column names
for df in [demo, drug, indication, outcome, reaction, source, therapy]:
    df.columns = df.columns.str.lower()

# --- 🔹 Step 1: Merge only 1:1 tables first ---
merged = demo.merge(outcome, on='caseid', how='left')
merged = merged.merge(source, on='caseid', how='left')

# --- 🔹 Step 2: For multi-entry tables, aggregate before merge ---
def safe_join(base_df, add_df, key, text_cols):
    """
    Aggregates multi-rows (many drugs/reactions per case) into single text fields.
    """
    grouped = add_df.groupby(key)[text_cols].agg(lambda x: '; '.join(x.dropna().astype(str).unique())).reset_index()
    return base_df.merge(grouped, on=key, how='left')

# Combine multiple records safely
merged = safe_join(merged, drug, 'caseid', ['drugname'])
merged = safe_join(merged, reaction, 'caseid', ['pt'])
merged = safe_join(merged, indication, 'caseid', ['indi_pt'])
merged = safe_join(merged, therapy, 'caseid', ['start_dt', 'end_dt'])

# --- 🔹 Step 3: Save cleaned merged dataset ---
os.makedirs(clean_path, exist_ok=True)
merged.to_csv(f"{clean_path}\\FAERS_2025_cleaned.csv", index=False, encoding='utf-8-sig')

print(f"✅ Cleaned dataset saved successfully: {clean_path}\\FAERS_2025_cleaned.csv")
print(f"✅ Final shape: {merged.shape}")

            