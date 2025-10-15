ADR Signal Detection & Trend Analysis

This project is based on the original FAERS (FDA Adverse Event Reporting System) dataset, a real-world source of adverse drug reaction (ADR) reports submitted to the FDA. The dataset has been curated and cleaned to support educational and analytical purposes, enabling signal detection, trend analysis, and data-driven insights in pharmacovigilance.

Dataset Structure

raw/ → Original FAERS files containing unprocessed reports with missing values, duplicates, and inconsistent formats.

cleaned/ → Structured and preprocessed datasets after cleaning, deduplication, and formatting for analysis.

sample/ → Subset of data (~200 rows) for quick testing, demo visualizations, and SQL/Python queries.

Files & Description
File	Description
patients.csv	Patient demographics (age, sex, weight, country).
drugs.csv	Drug information (drug name, dosage, route).
adverse_events.csv	Individual ADR records including reaction details and severity.
case_reports.csv	Case-level information linking patients, drugs, and reactions.
outcomes.csv	Reported outcomes for ADRs (recovered, serious, fatal).
Data Cleaning Performed

Removed null and duplicate records.

Standardized date formats to YYYY-MM-DD.

Corrected inconsistent drug and reaction names.

Added calculated fields such as total_cases per drug and serious_percentage.

Ensured referential integrity between tables for accurate joins.

Analysis & Use Cases

This dataset is ideal for:

ADR Signal Detection: Identifying drugs associated with high frequencies of specific adverse events.

Trend Analysis: Observing ADR trends over time, by drug, or by patient demographics.

Pharmacovigilance Reporting: Generating insights for regulatory compliance and patient safety.

Portfolio Projects: SQL, Python, and Power BI dashboards for practical learning.

⚠️ Disclaimer

This dataset is a real-world dataset derived from the FDA Adverse Event Reporting System (FAERS), publicly available on the FDA website. While processed for analysis, it contains actual adverse event reports submitted to the FDA.
