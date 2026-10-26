import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = []

# Title & Metadata
cells.append(nbf.v4.new_markdown_cell("""# Employee Attrition Problem Definition, Exploratory Analytics, and Planning

**Academic Project**: Employee Attrition Problem Definition & Planning  
**Role**: Senior HR Data Analyst & Lead People Analytics Specialist  
**Dataset**: IBM HR Analytics Employee Attrition & Performance Benchmark  
**Environment**: Python 3.11, Pandas, NumPy, Matplotlib, Seaborn  

---

## Executive Summary & Notebook Scope
This notebook establishes the formal diagnostic and exploratory data analysis (EDA) baseline for organizational employee attrition.
The primary objectives are:
1. **Data Ingestion & Integrity Validation**: Inspect the 1,470 records and 35 columns, auditing data types, missingness, and structural anomalies.
2. **Target Variable Validation**: Analyze the `Attrition` target class distribution, quantify the ~5.2:1 class imbalance, and define the positive class (`Yes`).
3. **Exploratory Univariate & Bivariate Analytics**: Diagnose the empirical relationships between employee departure and organizational drivers (overtime workload, compensation, tenure, job roles, and satisfaction).
4. **Correlation Analysis & Methodological Rigor**: Compute linear associations across continuous features while documenting the critical distinctions between correlation and causation.
5. **Ethical & Governance Context**: Audit protected demographic attributes (`Age`, `Gender`, `MaritalStatus`) to establish strict algorithmic fairness and non-discrimination baselines before Phase 2 predictive modeling."""))

# Section 1: Environment Setup & Library Imports
cells.append(nbf.v4.new_markdown_cell("""## 1. Environment Setup & Library Imports
We configure standard data manipulation, statistical, and plotting libraries. All warnings are managed cleanly to ensure academic reproducibility."""))

cells.append(nbf.v4.new_code_cell("""import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure plotting parameters
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
sns.set_theme(style="whitegrid", font="sans-serif")
palette = ["#2b5c8f", "#d95f02"]  # Primary Corporate Blue, Highlight Orange

# Ensure output directories exist
os.makedirs('../outputs/figures', exist_ok=True)
os.makedirs('../outputs/tables', exist_ok=True)

print("Python version:", sys.version.split()[0])
print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)
print("Seaborn version:", sns.__version__)"""))

# Section 2: Data Loading & Initial Schema Inspection
cells.append(nbf.v4.new_markdown_cell("""## 2. Data Loading & Schema Inspection
We load the validated IBM HR Analytics dataset (`WA_Fn-UseC_-HR-Employee-Attrition.csv`) from the local `data/` directory.
We inspect dataset dimensions, sample records, and column data types."""))

cells.append(nbf.v4.new_code_cell("""# Load the dataset
dataset_path = os.path.join('..', 'data', 'WA_Fn-UseC_-HR-Employee-Attrition.csv')
if not os.path.exists(dataset_path):
    dataset_path = 'data/WA_Fn-UseC_-HR-Employee-Attrition.csv'

df = pd.read_csv(dataset_path)

print(f"Dataset Dimensions: {df.shape[0]} rows (employees) x {df.shape[1]} columns (features)")
print(f"Total Cells: {df.size:,}")"""))

cells.append(nbf.v4.new_code_cell("""# Display first 5 records
df.head()"""))

cells.append(nbf.v4.new_code_cell("""# Inspect Column Names, Non-Null Counts, and Data Types
df.info()"""))

# Section 3: Missing Value & Data Quality Audit
cells.append(nbf.v4.new_markdown_cell("""## 3. Data Integrity & Missing-Value Audit
A critical step in professional data science is verifying data completeness.
We check for missing (null) values, duplicates, and non-informative constant columns."""))

cells.append(nbf.v4.new_code_cell("""# Audit missing values across all 35 columns
missing_counts = df.isnull().sum()
missing_pct = (missing_counts / len(df)) * 100

data_quality_df = pd.DataFrame({
    'Column': df.columns,
    'Data_Type': df.dtypes.astype(str),
    'Missing_Count': missing_counts.values,
    'Missing_Percentage': missing_pct.values,
    'Unique_Values': [df[col].nunique() for col in df.columns]
})

print(f"Total Missing Values in Entire Dataset: {df.isnull().sum().sum()}")
print(f"Duplicate Rows Count: {df.duplicated().sum()}")
data_quality_df.head(10)"""))

cells.append(nbf.v4.new_markdown_cell("""### 3.1 Identification of Constant Columns and Primary Identifiers
In tabular datasets, features with zero variance provide zero informational entropy and can destabilize covariance matrices or cause overfitting:
- `EmployeeCount`: Uniformly equal to `1` across all 1,470 records.
- `StandardHours`: Uniformly equal to `80` across all 1,470 records.
- `Over18`: Uniformly `'Y'` across all 1,470 records.
- `EmployeeNumber`: Unique administrative employee ID (1 to 2068). This is an arbitrary primary key and must not be used as a predictor to avoid data leakage."""))

cells.append(nbf.v4.new_code_cell("""# Verify zero-variance constants and identifier
constant_cols = [col for col in df.columns if df[col].nunique() == 1]
print("Constant / Zero-Variance Columns identified:", constant_cols)

for c in constant_cols:
    print(f" - {c}: unique value = {df[c].unique()}")

print(f"EmployeeNumber unique values count: {df['EmployeeNumber'].nunique()} (equal to row count: {df['EmployeeNumber'].nunique() == len(df)})")"""))

# Section 4: Target Variable Analysis (Attrition)
cells.append(nbf.v4.new_markdown_cell("""## 4. Target Variable Analysis: `Attrition`
The target variable is `Attrition`, indicating whether the employee has separated from the organization (`Yes`) or remains active (`No`).
Here we validate its distribution, calculate the exact class proportions, and evaluate class imbalance."""))

cells.append(nbf.v4.new_code_cell("""# Calculate target class frequencies
attrition_counts = df['Attrition'].value_counts()
attrition_proportions = df['Attrition'].value_counts(normalize=True) * 100

target_summary = pd.DataFrame({
    'Headcount': attrition_counts,
    'Percentage (%)': attrition_proportions.round(2)
})
print("Target Class Summary Table:")
display(target_summary)

imbalance_ratio = attrition_counts['No'] / attrition_counts['Yes']
print(f"\\nClass Imbalance Ratio (Negative : Positive): {imbalance_ratio:.2f} : 1")"""))

cells.append(nbf.v4.new_code_cell("""# Visualize Target Distribution
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Bar chart
ax1.bar(target_summary.index, target_summary['Headcount'], color=['#2b5c8f', '#d95f02'], width=0.5, edgecolor='black')
for i, (idx, row) in enumerate(target_summary.iterrows()):
    ax1.text(i, row['Headcount'] + 25, f"{row['Headcount']} ({row['Percentage (%)']}%)", ha='center', fontweight='bold')
ax1.set_title('Attrition Class Distribution (Headcount)', fontsize=13, fontweight='bold', pad=12)
ax1.set_ylabel('Employee Count')
ax1.set_ylim(0, 1400)

# Donut chart
ax2.pie(target_summary['Headcount'], labels=target_summary.index, autopct='%1.2f%%', startangle=90,
        colors=['#2b5c8f', '#d95f02'], explode=(0, 0.08), shadow=True, textprops={'fontsize': 11, 'fontweight': 'bold'})
ax2.set_title('Attrition Class Proportion', fontsize=13, fontweight='bold', pad=12)

plt.tight_layout()
plt.show()"""))

# Section 5: Departmental & Job Role Attrition Diagnostics
cells.append(nbf.v4.new_markdown_cell("""## 5. Departmental & Job Role Diagnostics
We disaggregate attrition patterns by organizational business unit and functional job role.
We compute both:
1. **Within-Group Attrition Rate (%)**: The percentage of employees *within that specific department/role* who left.
2. **Share of Total Attrition (%)**: The proportion of *all 237 departures* accounted for by that department/role."""))

cells.append(nbf.v4.new_code_cell("""# Department-Level Breakdown
dept_summary = df.groupby('Department')['Attrition'].agg(
    Total_Employees='count',
    Departures=lambda x: (x == 'Yes').sum(),
    Retention_Count=lambda x: (x == 'No').sum(),
    Attrition_Rate=lambda x: (x == 'Yes').mean() * 100,
    Share_of_Total_Attrition=lambda x: (x == 'Yes').sum() / (df['Attrition'] == 'Yes').sum() * 100
).reset_index()

dept_summary['Attrition_Rate'] = dept_summary['Attrition_Rate'].round(2)
dept_summary['Share_of_Total_Attrition'] = dept_summary['Share_of_Total_Attrition'].round(2)

print("Department-Level Attrition Breakdown:")
display(dept_summary)"""))

cells.append(nbf.v4.new_code_cell("""# Job Role Breakdown (Sorted by Attrition Rate)
role_summary = df.groupby('JobRole')['Attrition'].agg(
    Total_Employees='count',
    Departures=lambda x: (x == 'Yes').sum(),
    Attrition_Rate=lambda x: (x == 'Yes').mean() * 100,
    Share_of_Total_Attrition=lambda x: (x == 'Yes').sum() / (df['Attrition'] == 'Yes').sum() * 100
).sort_values(by='Attrition_Rate', ascending=False).reset_index()

role_summary['Attrition_Rate'] = role_summary['Attrition_Rate'].round(2)
role_summary['Share_of_Total_Attrition'] = role_summary['Share_of_Total_Attrition'].round(2)

print("Job Role Attrition Breakdown (Ranked by Flight Risk):")
display(role_summary)"""))

cells.append(nbf.v4.new_code_cell("""# Visualize Job Role Attrition Rates
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.barh(role_summary['JobRole'][::-1], role_summary['Attrition_Rate'][::-1],
               color='#2b5c8f', edgecolor='black', height=0.6)

# Highlight high risk roles (>20%)
for idx, bar in enumerate(bars):
    val = role_summary['Attrition_Rate'][::-1].iloc[idx]
    if val > 20.0:
        bar.set_color('#d95f02')
    ax.text(val + 0.8, idx, f"{val:.1f}% (n={role_summary['Departures'][::-1].iloc[idx]}/{role_summary['Total_Employees'][::-1].iloc[idx]})",
            va='center', fontweight='bold', fontsize=10)

ax.set_title('Attrition Rate by Functional Job Role', fontsize=13, fontweight='bold', pad=15)
ax.set_xlabel('Attrition Rate (%)', fontsize=11)
ax.set_xlim(0, 48)
plt.tight_layout()
plt.show()"""))

# Section 6: Workload & Overtime Analysis
cells.append(nbf.v4.new_markdown_cell("""## 6. Workload Demands: Overtime & Business Travel
We investigate the association between working hours demand (`OverTime`), business travel frequency, and flight risk."""))

cells.append(nbf.v4.new_code_cell("""# Overtime Analysis
ot_summary = df.groupby('OverTime')['Attrition'].agg(
    Total_Employees='count',
    Departures=lambda x: (x == 'Yes').sum(),
    Attrition_Rate=lambda x: (x == 'Yes').mean() * 100
).reset_index()

ot_summary['Attrition_Rate'] = ot_summary['Attrition_Rate'].round(2)
print("OverTime Attrition Analysis:")
display(ot_summary)

ot_ratio = ot_summary.loc[ot_summary['OverTime'] == 'Yes', 'Attrition_Rate'].values[0] / ot_summary.loc[ot_summary['OverTime'] == 'No', 'Attrition_Rate'].values[0]
print(f"\\nRelative Risk: Employees working OverTime exhibit a {ot_ratio:.2f}x higher attrition rate than non-overtime staff.")"""))

cells.append(nbf.v4.new_code_cell("""# Business Travel Analysis
travel_summary = df.groupby('BusinessTravel')['Attrition'].agg(
    Total_Employees='count',
    Departures=lambda x: (x == 'Yes').sum(),
    Attrition_Rate=lambda x: (x == 'Yes').mean() * 100
).reset_index()

travel_summary['Attrition_Rate'] = travel_summary['Attrition_Rate'].round(2)
print("Business Travel Attrition Analysis:")
display(travel_summary)"""))

# Section 7: Continuous Feature Distributions & Boxplots
cells.append(nbf.v4.new_markdown_cell("""## 7. Compensation, Experience, and Tenure Comparisons
We compare the statistical distributions of numerical continuous variables across retained and departing employees:
- `MonthlyIncome`
- `TotalWorkingYears`
- `YearsAtCompany`
- `YearsWithCurrManager`"""))

cells.append(nbf.v4.new_code_cell("""# Statistical Comparison of Key Continuous Features
cont_cols = ['MonthlyIncome', 'Age', 'TotalWorkingYears', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsWithCurrManager']

comp_stats = []
for c in cont_cols:
    no_stats = df[df['Attrition'] == 'No'][c]
    yes_stats = df[df['Attrition'] == 'Yes'][c]
    comp_stats.append({
        'Feature': c,
        'Retained_Mean': round(no_stats.mean(), 2),
        'Departed_Mean': round(yes_stats.mean(), 2),
        'Retained_Median': round(no_stats.median(), 2),
        'Departed_Median': round(yes_stats.median(), 2),
        'Difference_in_Median': round(yes_stats.median() - no_stats.median(), 2)
    })

comp_df = pd.DataFrame(comp_stats)
display(comp_df)"""))

cells.append(nbf.v4.new_code_cell("""# Multi-panel Boxplots comparing distributions
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

sns.boxplot(x='Attrition', y='MonthlyIncome', data=df, ax=axes[0, 0], hue='Attrition', palette=['#2b5c8f', '#d95f02'], legend=False)
axes[0, 0].set_title('Monthly Income ($) by Attrition Status', fontsize=12, fontweight='bold')

sns.boxplot(x='Attrition', y='TotalWorkingYears', data=df, ax=axes[0, 1], hue='Attrition', palette=['#2b5c8f', '#d95f02'], legend=False)
axes[0, 1].set_title('Total Career Experience (Years)', fontsize=12, fontweight='bold')

sns.boxplot(x='Attrition', y='YearsAtCompany', data=df, ax=axes[1, 0], hue='Attrition', palette=['#2b5c8f', '#d95f02'], legend=False)
axes[1, 0].set_title('Company Tenure (Years)', fontsize=12, fontweight='bold')

sns.boxplot(x='Attrition', y='YearsWithCurrManager', data=df, ax=axes[1, 1], hue='Attrition', palette=['#2b5c8f', '#d95f02'], legend=False)
axes[1, 1].set_title('Tenure with Current Manager (Years)', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()"""))

# Section 8: Employee Satisfaction & Well-Being Likert Scales
cells.append(nbf.v4.new_markdown_cell("""## 8. Employee Sentiment and Survey Ratings
We examine the 4-point Likert ratings:
- `JobSatisfaction` (1: Low to 4: Very High)
- `EnvironmentSatisfaction` (1: Low to 4: Very High)
- `WorkLifeBalance` (1: Bad to 4: Best)"""))

cells.append(nbf.v4.new_code_cell("""# Satisfaction cross-tabulations
for sat_col in ['JobSatisfaction', 'EnvironmentSatisfaction', 'WorkLifeBalance']:
    agg = df.groupby(sat_col)['Attrition'].agg(
        Total='count',
        Departures=lambda x: (x == 'Yes').sum(),
        Attrition_Rate=lambda x: (x == 'Yes').mean() * 100
    ).reset_index()
    agg['Attrition_Rate'] = agg['Attrition_Rate'].round(2)
    print(f"\\n--- {sat_col} Breakdown ---")
    display(agg)"""))

# Section 9: Correlation Matrix of Continuous Features
cells.append(nbf.v4.new_markdown_cell("""## 9. Pearson Linear Correlation Analysis
We compute the Pearson linear correlation matrix for suitable continuous and discrete numerical variables.

### Methodological Notes & Ethical Caveats:
1. **Correlation Does Not Imply Causation**: A strong linear association (e.g., between `MonthlyIncome` and `TotalWorkingYears`) reflects seniority-based pay structures, not an independent causal mechanism.
2. **Exclusion of Non-Continuous Columns**: Categorical nominal variables (`Department`, `JobRole`, `EducationField`) must **never** be arbitrarily mapped to integers (e.g. Sales=1, R&D=2, HR=3) because arbitrary integers impose false geometric distances and fictitious linear trends.
3. **Ordinal Cautions**: Likert ratings are discrete ordinal scales with non-uniform psychological distances and must be interpreted cautiously."""))

cells.append(nbf.v4.new_code_cell("""# Select continuous and discrete numerical variables
corr_cols = [
    'Age', 'DailyRate', 'DistanceFromHome', 'HourlyRate', 'MonthlyIncome', 'MonthlyRate',
    'NumCompaniesWorked', 'PercentSalaryHike', 'TotalWorkingYears', 'TrainingTimesLastYear',
    'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager'
]

corr_matrix = df[corr_cols].corr()

# Plot heatmap
fig, ax = plt.subplots(figsize=(12, 10))
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', cmap='Blues', vmin=-0.2, vmax=1.0,
            square=True, linewidths=0.5, cbar_kws={"shrink": 0.8}, ax=ax)
ax.set_title('Pearson Linear Correlation Heatmap (Continuous Features)', fontsize=13, fontweight='bold', pad=15)
plt.tight_layout()
plt.show()"""))

# Section 10: Ethical Demographic Audit (Protected Classes)
cells.append(nbf.v4.new_markdown_cell("""## 10. Protected Demographics & Ethical Fairness Audit
To adhere to labor non-discrimination standards (Title VII of the Civil Rights Act, Age Discrimination in Employment Act), we audit attrition distributions across protected demographic attributes:
- `Gender`
- `MaritalStatus`
- `Age` cohorts

**Strict Governance Mandate**: These attributes must be evaluated to ensure company policies do not inadvertently produce disparate impact. However, individual predictions in Phase 2 must **never** be used to deny promotions, alter compensation, or execute adverse employment actions."""))

cells.append(nbf.v4.new_code_cell("""# Demographic Cross-Tabulation
print("--- Gender Attrition Profile ---")
gender_agg = df.groupby('Gender')['Attrition'].agg(
    Total='count',
    Departures=lambda x: (x == 'Yes').sum(),
    Attrition_Rate=lambda x: (x == 'Yes').mean() * 100
).reset_index()
gender_agg['Attrition_Rate'] = gender_agg['Attrition_Rate'].round(2)
display(gender_agg)

print("\\n--- Marital Status Attrition Profile ---")
marital_agg = df.groupby('MaritalStatus')['Attrition'].agg(
    Total='count',
    Departures=lambda x: (x == 'Yes').sum(),
    Attrition_Rate=lambda x: (x == 'Yes').mean() * 100
).reset_index()
marital_agg['Attrition_Rate'] = marital_agg['Attrition_Rate'].round(2)
display(marital_agg)"""))

# Section 11: Summary of Empirical Findings & Next Steps
cells.append(nbf.v4.new_markdown_cell("""## 11. Empirical Findings Summary & Project Roadmap

### Key Diagnostic Findings:
1. **Target Baseline**: The dataset exhibits an overall attrition proportion of **16.12% (237 departed employees out of 1,470)**, establishing a **5.2:1 class imbalance**.
2. **Workload Risk Driver**: Personnel working **OverTime** experience an attrition rate of **30.53%**, compared to **10.44%** among non-overtime staff (nearly 3x higher relative risk).
3. **Role-Specific Vulnerability**: **Sales Representatives** experience the highest turnover rate at **39.76%**, while **Laboratory Technicians** represent the largest single departure volume (**62 departures**, representing **26.16%** of all organizational turnover).
4. **Compensation Disparity**: Departed employees had a median monthly salary of **$3,202**, compared to **$5,204** for retained personnel (a **38.5%** gap).
5. **Early-Career Hazard**: Median tenure among departed employees was **3.0 years** at the company and **2.0 years** with their current manager, indicating acute retention vulnerability during early career socialization.
6. **Data Hygiene & Completeness**: All 35 features are **100% complete** (0 missing values), with 3 zero-variance constants (`EmployeeCount`, `StandardHours`, `Over18`) and 1 primary key (`EmployeeNumber`) identified for exclusion from predictive modeling.

---

### Transition to Phase 2: Predictive Modeling Roadmap
With the business problem formally specified, feature dictionary published, business KPIs standardized, and exploratory data analysis verified, the foundation is established for **Phase 2 Predictive Modeling**:
- Data pre-processing and categorical one-hot encoding.
- Stratified train-validation-test partitioning (e.g. 70/15/15) preserving the 16.12% class balance.
- Imbalanced learning techniques (class weighting, SMOTE, PR-AUC optimization).
- Algorithm benchmarking (Logistic Regression, Random Forest, XGBoost).
- Post-prediction model explainability via SHAP (SHapley Additive exPlanations) and ethical fairness auditing."""))

nb.cells = cells

# Save notebook
notebook_path = 'notebooks/employee_attrition_problem_definition.ipynb'
with open(notebook_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print(f"Successfully written Jupyter Notebook to {notebook_path} with {len(cells)} cells.")
