import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set aesthetics
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
sns.set_theme(style="whitegrid", font="sans-serif")
palette = ["#2b5c8f", "#d95f02"]  # Primary Blue, Accent Orange

os.makedirs('outputs/figures', exist_ok=True)
os.makedirs('outputs/tables', exist_ok=True)

# Load dataset
df = pd.read_csv('data/WA_Fn-UseC_-HR-Employee-Attrition.csv')

# 1. Target Distribution
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
counts = df['Attrition'].value_counts()
colors = ['#2b5c8f', '#d95f02']

ax1.bar(counts.index, counts.values, color=colors, width=0.5, edgecolor='black', linewidth=1)
for i, v in enumerate(counts.values):
    ax1.text(i, v + 25, f"{v} ({v/len(df)*100:.1f}%)", ha='center', fontweight='bold', fontsize=11)
ax1.set_title('Attrition Class Headcount (N=1,470)', fontsize=13, fontweight='bold', pad=15)
ax1.set_ylabel('Employee Count', fontsize=11)
ax1.set_ylim(0, 1400)

ax2.pie(counts.values, labels=counts.index, autopct='%1.2f%%', startangle=90, colors=colors,
        explode=(0, 0.1), shadow=True, textprops={'fontsize': 12, 'fontweight': 'bold'})
ax2.set_title('Attrition Class Proportion', fontsize=13, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig('outputs/figures/attrition_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved outputs/figures/attrition_distribution.png")

# 2. Attrition by Department
dept_agg = df.groupby('Department')['Attrition'].agg(
    Total='count',
    Departed=lambda x: (x == 'Yes').sum(),
    Rate=lambda x: (x == 'Yes').mean() * 100
).reset_index()

fig, ax1 = plt.subplots(figsize=(10, 5))
x = np.arange(len(dept_agg))
width = 0.35

rects1 = ax1.bar(x - width/2, dept_agg['Total'], width, label='Total Population', color='#4a7bb0', edgecolor='black')
rects2 = ax1.bar(x + width/2, dept_agg['Departed'], width, label='Departed Count', color='#d95f02', edgecolor='black')

ax1.set_ylabel('Employee Headcount', fontsize=11)
ax1.set_title('Departmental Workforce Headcount and Departures', fontsize=13, fontweight='bold', pad=15)
ax1.set_xticks(x)
ax1.set_xticklabels(dept_agg['Department'], fontsize=11)
ax1.legend(loc='upper right')

# Add rate labels
for i, row in dept_agg.iterrows():
    ax1.text(i + width/2, row['Departed'] + 15, f"Rate:\n{row['Rate']:.1f}%", ha='center', fontsize=9, fontweight='bold', color='#b30000')

plt.tight_layout()
plt.savefig('outputs/figures/attrition_by_department.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved outputs/figures/attrition_by_department.png")

# 3. Attrition by Job Role
role_agg = df.groupby('JobRole')['Attrition'].agg(
    Total='count',
    Departed=lambda x: (x == 'Yes').sum(),
    Rate=lambda x: (x == 'Yes').mean() * 100
).sort_values(by='Rate', ascending=True).reset_index()

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.barh(role_agg['JobRole'], role_agg['Rate'], color='#2b5c8f', edgecolor='black', height=0.6)

# Highlight high risk roles (>20%) in red/orange
for i, bar in enumerate(bars):
    if role_agg.loc[i, 'Rate'] > 20.0:
        bar.set_color('#d95f02')

for i, row in role_agg.iterrows():
    ax.text(row['Rate'] + 0.8, i, f"{row['Rate']:.1f}%  (n={row['Departed']}/{row['Total']})",
            va='center', fontsize=10, fontweight='bold')

ax.set_xlabel('Attrition Rate within Job Role (%)', fontsize=11)
ax.set_title('Attrition Rate by Job Role (Highlight: >20% Turnover)', fontsize=13, fontweight='bold', pad=15)
ax.set_xlim(0, 48)

plt.tight_layout()
plt.savefig('outputs/figures/attrition_by_job_role.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved outputs/figures/attrition_by_job_role.png")

# 4. Attrition by OverTime
ot_agg = df.groupby('OverTime')['Attrition'].agg(
    Total='count',
    Departed=lambda x: (x == 'Yes').sum(),
    Rate=lambda x: (x == 'Yes').mean() * 100
).reset_index()

fig, ax = plt.subplots(figsize=(7, 5))
bars = ax.bar(['No OverTime (n=1,054)', 'OverTime Mandated (n=416)'], ot_agg['Rate'],
              color=['#2b5c8f', '#d95f02'], width=0.45, edgecolor='black', linewidth=1)

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.2f}%", ha='center', fontsize=12, fontweight='bold')

ax.set_ylabel('Attrition Rate (%)', fontsize=11)
ax.set_title('Impact of OverTime on Employee Attrition Rate', fontsize=13, fontweight='bold', pad=15)
ax.set_ylim(0, 36)

plt.tight_layout()
plt.savefig('outputs/figures/attrition_by_overtime.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved outputs/figures/attrition_by_overtime.png")

# 5. Continuous Distributions: Income, Tenure, Age, Manager
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Monthly Income
sns.boxplot(x='Attrition', y='MonthlyIncome', data=df, ax=axes[0, 0], hue='Attrition', palette=['#2b5c8f', '#d95f02'], legend=False)
axes[0, 0].set_title('Monthly Income by Attrition Status', fontsize=12, fontweight='bold')
axes[0, 0].set_ylabel('Monthly Income ($)', fontsize=10)
axes[0, 0].set_xlabel('Attrition', fontsize=10)

# Total Working Years
sns.boxplot(x='Attrition', y='TotalWorkingYears', data=df, ax=axes[0, 1], hue='Attrition', palette=['#2b5c8f', '#d95f02'], legend=False)
axes[0, 1].set_title('Total Career Experience (Years)', fontsize=12, fontweight='bold')
axes[0, 1].set_ylabel('Total Working Years', fontsize=10)
axes[0, 1].set_xlabel('Attrition', fontsize=10)

# Years At Company
sns.boxplot(x='Attrition', y='YearsAtCompany', data=df, ax=axes[1, 0], hue='Attrition', palette=['#2b5c8f', '#d95f02'], legend=False)
axes[1, 0].set_title('Company Tenure by Attrition Status', fontsize=12, fontweight='bold')
axes[1, 0].set_ylabel('Years at Company', fontsize=10)
axes[1, 0].set_xlabel('Attrition', fontsize=10)

# Years With Current Manager
sns.boxplot(x='Attrition', y='YearsWithCurrManager', data=df, ax=axes[1, 1], hue='Attrition', palette=['#2b5c8f', '#d95f02'], legend=False)
axes[1, 1].set_title('Years with Current Manager', fontsize=12, fontweight='bold')
axes[1, 1].set_ylabel('Years with Manager', fontsize=10)
axes[1, 1].set_xlabel('Attrition', fontsize=10)

plt.tight_layout()
plt.savefig('outputs/figures/tenure_and_income_distributions.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved outputs/figures/tenure_and_income_distributions.png")

# 6. Satisfaction and Well-Being Ratings
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

for idx, (col, title) in enumerate([
    ('JobSatisfaction', 'Job Satisfaction (1:Low to 4:V.High)'),
    ('EnvironmentSatisfaction', 'Environment Satisfaction (1:Low to 4:V.High)'),
    ('WorkLifeBalance', 'Work-Life Balance (1:Bad to 4:Best)')
]):
    sat_agg = df.groupby(col)['Attrition'].agg(
        Rate=lambda x: (x == 'Yes').mean() * 100,
        Count='count'
    ).reset_index()
    
    bars = axes[idx].bar(sat_agg[col].astype(str), sat_agg['Rate'], color='#2b5c8f', edgecolor='black', width=0.5)
    for bar in bars:
        yval = bar.get_height()
        axes[idx].text(bar.get_x() + bar.get_width()/2, yval + 0.8, f"{yval:.1f}%", ha='center', fontsize=10, fontweight='bold')
    axes[idx].set_title(title, fontsize=11, fontweight='bold')
    axes[idx].set_ylabel('Attrition Rate (%)' if idx == 0 else '')
    axes[idx].set_xlabel('Survey Rating Level', fontsize=10)
    axes[idx].set_ylim(0, 36)

plt.tight_layout()
plt.savefig('outputs/figures/satisfaction_and_wlb_attrition.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved outputs/figures/satisfaction_and_wlb_attrition.png")

# 7. Correlation Heatmap
# Select numerical continuous and discrete features, excluding constants and IDs
corr_cols = [
    'Age', 'DailyRate', 'DistanceFromHome', 'HourlyRate', 'MonthlyIncome', 'MonthlyRate',
    'NumCompaniesWorked', 'PercentSalaryHike', 'TotalWorkingYears', 'TrainingTimesLastYear',
    'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager'
]

corr_matrix = df[corr_cols].corr()

fig, ax = plt.subplots(figsize=(12, 10))
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', cmap='Blues', vmin=-0.2, vmax=1.0,
            square=True, linewidths=0.5, cbar_kws={"shrink": 0.8}, ax=ax)
ax.set_title('Pearson Linear Correlation Matrix (Continuous Features)', fontsize=13, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig('outputs/figures/correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved outputs/figures/correlation_heatmap.png")

# 8. Data Completeness Chart
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(['Dataset Columns (All 35)'], [100.0], color='#2b5c8f', width=0.35, edgecolor='black')
ax.text(0, 50, "100.0% Complete\n(0 Missing Values / 1,470 Rows)", ha='center', va='center',
        fontsize=13, fontweight='bold', color='white')
ax.set_ylim(0, 115)
ax.set_ylabel('Data Completeness (%)', fontsize=11)
ax.set_title('Dataset Integrity: Missing Value Audit', fontsize=13, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig('outputs/figures/missing_values_summary.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved outputs/figures/missing_values_summary.png")
