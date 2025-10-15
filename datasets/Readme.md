*\
=============================================
ADR Signal Detection & Trend Analysis Dataset
=============================================

This dataset is a curated and cleaned version of FAERS (FDA Adverse Event Reporting System) data for educational and analytical purposes. It simulates real-world pharmacovigilance data to demonstrate ADR signal detection, trend analysis, and data-driven insights in drug safety.

-----------------
Dataset Structure
-----------------
raw/ → Original FAERS files containing unprocessed adverse event reports, including missing values, duplicates, and inconsistent formats.
cleaned/ → Preprocessed and structured datasets after cleaning, deduplication, and formatting for analysis.
sample/ → Subset of data (~200 rows) for quick testing, demo visualizations, and SQL/Python queries.

-------------------
Files & Description
-------------------
(not original tables names)
patients.csv → Patient demographics (age, sex, weight, country).
drugs.csv → Drug information (drug name, dosage, route).
adverse_events.csv → Individual ADR records with reaction details and severity.
case_reports.csv → Case-level information linking patients, drugs, and reactions.
outcomes.csv → Reported outcomes for ADRs (recovered, serious, fatal).

-----------------------
Data Cleaning Performed
-----------------------
Removed null and duplicate records.
Standardized date formats to YYYY-MM-DD.
Corrected inconsistent drug and reaction names.
Added calculated fields such as total_cases per drug and serious_percentage.
Ensured referential integrity between all tables for accurate join operations.

----------
Disclaimer
----------
This dataset is a real-world dataset derived from the FDA Adverse Event Reporting System (FAERS), publicly available on the FDA website. 
The data has been processed for analysis purposes but originates from actual adverse event reports submitted to the FDA.

========================================================================================================================================
