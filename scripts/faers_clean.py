import pandas as pd
import numpy as np
import os

# ======================================================
# 1️⃣ FILE SETUP
# ======================================================

file_path = r'C:\Users\USER\Documents\DATA ANALYST\PROJECTS\Resume Projects\Project 1 ADR Signal Detection & Trend Analysis\raw_data\FAERS_2025_merge.csv'

# Check file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"❌ File not found at: {file_path}")

# ======================================================
# 2️⃣ LOAD FILE SAFELY
# ======================================================

# Most FAERS exports are comma-separated and UTF-8 encoded with BOM
df = pd.read_csv(file_path, sep=',', encoding='utf-8-sig', low_memory=False)

print("✅ File loaded successfully!")
print("Initial shape:", df.shape)
print("Sample columns:", df.columns.tolist()[:10])

# ======================================================
# 3️⃣ STANDARDIZE COLUMN NAMES
# ======================================================

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
if df.columns[0].startswith('ï»¿'):
    df.columns = [col.replace('ï»¿', '') for col in df.columns]  # remove BOM artifacts

print("\n🧾 Cleaned column names:")
print(df.columns.tolist()[:10])

# ======================================================
# 4️⃣ REMOVE DUPLICATES
# ======================================================

dup_count = df.duplicated().sum()
if dup_count > 0:
    print(f"\n🔍 Found {dup_count} duplicate rows. Removing...")
    df = df.drop_duplicates()
else:
    print("\n✅ No duplicate rows found.")

# ======================================================
# 5️⃣ HANDLE MISSING VALUES
# ======================================================

missing_summary = df.isnull().sum()
print("\n🧩 Missing values (non-zero only):")
print(missing_summary[missing_summary > 0])

# Drop rows missing key identifiers if they exist
key_cols = [col for col in ['caseid', 'primaryid', 'isr'] if col in df.columns]
if key_cols:
    df = df.dropna(subset=key_cols)

# Fill numeric columns with median
num_cols = df.select_dtypes(include=[np.number]).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# Fill text columns with "Unknown"
obj_cols = df.select_dtypes(include=['object']).columns
df[obj_cols] = df[obj_cols].fillna('Unknown')

# ======================================================
# 6️⃣ STANDARDIZE DATE FORMATS (YYYY-MM-DD)
# ======================================================

date_cols = [col for col in df.columns if 'date' in col.lower() or 'dt' in col.lower()]
print("\n📅 Detected date columns:", date_cols)

def standardize_date(series):
    series = series.astype(str).str.strip().replace(['nan', 'NaT', 'None', ''], pd.NA)
    return pd.to_datetime(series, errors='coerce')

for col in date_cols:
    df[col] = standardize_date(df[col])
    df[col] = df[col].dt.strftime('%Y-%m-%d')

print("\n✅ All detected date columns standardized to YYYY-MM-DD.")

# ======================================================
# 7️⃣ FIX DATA TYPES & OUTLIERS (IF PRESENT)
# ======================================================

if 'age' in df.columns:
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df = df[df['age'].ge(0) | df['age'].isna()]

# ======================================================
# 8️⃣ FINAL SUMMARY
# ======================================================

print("\n✅ Data cleaning complete!")
print("Final shape:", df.shape)
print("Sample preview:")
print(df.head())

# ======================================================
# 9️⃣ SAVE CLEANED FILE
# ======================================================

cleaned_path = os.path.splitext(r'C:\Users\USER\Documents\DATA ANALYST\PROJECTS\Resume Projects\Project 1 ADR Signal Detection & Trend Analysis\cleaned_data')[0] + '_cleaned.csv'
df.to_csv(cleaned_path, index=False, encoding='utf-8-sig')

print(f"\n💾 Cleaned file saved successfully at:\n{cleaned_path}")
