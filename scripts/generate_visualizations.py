"""
Diabetes Risk Prediction - Visualization Generator
==================================================
Creates publication-ready charts using matplotlib and seaborn
Output: PNG files at 300 DPI for GitHub documentation
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec
import warnings
warnings.filterwarnings('ignore')

# Configuration
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 100
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10

# Output directory
output_dir = r"C:\Users\Mujtaba\Desktop\diabetes-risk-analysis\visualizations"

# Load dataset
print("Loading dataset...")
df = pd.read_csv(r'D:\Datasets\extracted\diabetes_risk_prediction_dataset.csv')
print(f"✓ Loaded: {df.shape[0]:,} records, {df.shape[1]} features\n")

# ============================================================================
# VISUALIZATION 1: Risk Distribution Overview
# ============================================================================
print("Creating: 01_risk_distribution.png")
fig = plt.figure(figsize=(14, 5))
gs = GridSpec(1, 3, figure=fig, width_ratios=[1, 1, 1.2])

# Bar chart
ax1 = fig.add_subplot(gs[0, 0])
risk_counts = df['Diabetes_Risk'].value_counts().sort_index(key=lambda x: x.map({'Low': 0, 'Moderate': 1, 'High': 2}))
colors = ['#27ae60', '#f39c12', '#e74c3c']
bars = ax1.bar(risk_counts.index, risk_counts.values, color=colors, edgecolor='black', alpha=0.85, linewidth=1.5)
ax1.set_title('Diabetes Risk Distribution\n(Count)', fontsize=12, fontweight='bold', pad=10)
ax1.set_ylabel('Number of Patients', fontsize=11, fontweight='bold')
ax1.set_xlabel('Risk Category', fontsize=11, fontweight='bold')
ax1.grid(axis='y', alpha=0.3)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height):,}',
            ha='center', va='bottom', fontweight='bold', fontsize=10)

# Percentage bar chart
ax2 = fig.add_subplot(gs[0, 1])
risk_pct = (df['Diabetes_Risk'].value_counts(normalize=True) * 100).sort_index(key=lambda x: x.map({'Low': 0, 'Moderate': 1, 'High': 2}))
bars = ax2.bar(risk_pct.index, risk_pct.values, color=colors, edgecolor='black', alpha=0.85, linewidth=1.5)
ax2.set_title('Diabetes Risk Distribution\n(Percentage)', fontsize=12, fontweight='bold', pad=10)
ax2.set_ylabel('Percentage (%)', fontsize=11, fontweight='bold')
ax2.set_xlabel('Risk Category', fontsize=11, fontweight='bold')
ax2.set_ylim(0, 80)
ax2.grid(axis='y', alpha=0.3)

# Add value labels
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.1f}%',
            ha='center', va='bottom', fontweight='bold', fontsize=10)

# Pie chart
ax3 = fig.add_subplot(gs[0, 2])
explode = (0.05, 0.05, 0.1)
wedges, texts, autotexts = ax3.pie(risk_counts.values, labels=risk_counts.index, autopct='%1.1f%%',
                                     colors=colors, explode=explode, startangle=90,
                                     textprops={'fontsize': 11, 'fontweight': 'bold'})
ax3.set_title('Risk Distribution\n(Pie Chart)', fontsize=12, fontweight='bold', pad=10)

# Make percentage text white on dark backgrounds
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_fontweight('bold')

plt.tight_layout()
plt.savefig(f'{output_dir}/01_risk_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: 01_risk_distribution.png\n")

# ============================================================================
# VISUALIZATION 2: Key Health Metrics Dashboard
# ============================================================================
print("Creating: 02_health_metrics_dashboard.png")
fig = plt.figure(figsize=(16, 10))
gs = GridSpec(3, 3, figure=fig, hspace=0.35, wspace=0.3)

# BMI Distribution
ax1 = fig.add_subplot(gs[0, 0])
bmi_data = pd.to_numeric(df['BMI'], errors='coerce').dropna()
ax1.hist(bmi_data, bins=40, color='#9b59b6', edgecolor='black', alpha=0.8)
ax1.axvline(bmi_data.mean(), color='red', linestyle='--', linewidth=2.5, label=f'Mean: {bmi_data.mean():.1f}')
ax1.set_title('BMI Distribution', fontsize=11, fontweight='bold')
ax1.set_xlabel('BMI (kg/m²)', fontsize=10)
ax1.set_ylabel('Frequency', fontsize=10)
ax1.legend()
ax1.grid(alpha=0.3)

# Blood Glucose
ax2 = fig.add_subplot(gs[0, 1])
glucose_data = pd.to_numeric(df['Blood_Glucose'], errors='coerce').dropna()
ax2.hist(glucose_data, bins=40, color='#e74c3c', edgecolor='black', alpha=0.8)
ax2.axvline(glucose_data.mean(), color='darkred', linestyle='--', linewidth=2.5, label=f'Mean: {glucose_data.mean():.1f}')
ax2.axvline(126, color='orange', linestyle=':', linewidth=2, label='Diabetic threshold')
ax2.set_title('Blood Glucose Distribution', fontsize=11, fontweight='bold')
ax2.set_xlabel('Fasting Glucose (mg/dL)', fontsize=10)
ax2.set_ylabel('Frequency', fontsize=10)
ax2.legend(fontsize=9)
ax2.grid(alpha=0.3)

# HbA1c
ax3 = fig.add_subplot(gs[0, 2])
hba1c_data = pd.to_numeric(df['HbA1c'], errors='coerce').dropna()
ax3.hist(hba1c_data, bins=30, color='#f39c12', edgecolor='black', alpha=0.8)
ax3.axvline(hba1c_data.mean(), color='darkorange', linestyle='--', linewidth=2.5, label=f'Mean: {hba1c_data.mean():.1f}%')
ax3.axvline(6.5, color='red', linestyle=':', linewidth=2, label='Diagnostic threshold')
ax3.set_title('HbA1c Distribution', fontsize=11, fontweight='bold')
ax3.set_xlabel('HbA1c (%)', fontsize=10)
ax3.set_ylabel('Frequency', fontsize=10)
ax3.legend(fontsize=9)
ax3.grid(alpha=0.3)

# BMI Categories
ax4 = fig.add_subplot(gs[1, 0])
def categorize_bmi(x):
    if pd.isna(x):
        return 'Unknown'
    x = float(x)
    if x < 18.5: return 'Underweight'
    elif x < 25: return 'Normal'
    elif x < 30: return 'Overweight'
    else: return 'Obese'

bmi_cats = df['BMI'].apply(categorize_bmi).value_counts()
bmi_order = ['Underweight', 'Normal', 'Overweight', 'Obese', 'Unknown']
bmi_cats = bmi_cats.reindex([x for x in bmi_order if x in bmi_cats.index])
colors_bmi = ['#27ae60', '#3498db', '#f39c12', '#e74c3c', '#95a5a6']
ax4.barh(bmi_cats.index, bmi_cats.values, color=colors_bmi[:len(bmi_cats)], edgecolor='black', alpha=0.8)
ax4.set_title('BMI Categories', fontsize=11, fontweight='bold')
ax4.set_xlabel('Count', fontsize=10)
for i, v in enumerate(bmi_cats.values):
    ax4.text(v, i, f' {int(v):,}', va='center', fontweight='bold')
ax4.grid(axis='x', alpha=0.3)

# Blood Pressure
ax5 = fig.add_subplot(gs[1, 1])
systolic = pd.to_numeric(df['Blood_Pressure_Systolic'], errors='coerce').dropna()
diastolic = pd.to_numeric(df['Blood_Pressure_Diastolic'], errors='coerce').dropna()
ax5.scatter(systolic, diastolic, alpha=0.3, s=20, color='#e74c3c')
ax5.axhline(90, color='red', linestyle='--', linewidth=1.5, alpha=0.5, label='Stage 2 (90 mmHg)')
ax5.axvline(140, color='red', linestyle='--', linewidth=1.5, alpha=0.5)
ax5.set_title('Blood Pressure Scatter', fontsize=11, fontweight='bold')
ax5.set_xlabel('Systolic (mmHg)', fontsize=10)
ax5.set_ylabel('Diastolic (mmHg)', fontsize=10)
ax5.grid(alpha=0.3)
ax5.legend(fontsize=9)

# Total Cholesterol
ax6 = fig.add_subplot(gs[1, 2])
chol_data = pd.to_numeric(df['Total_Cholesterol'], errors='coerce').dropna()
ax6.hist(chol_data, bins=30, color='#1abc9c', edgecolor='black', alpha=0.8)
ax6.axvline(chol_data.mean(), color='darkcyan', linestyle='--', linewidth=2.5, label=f'Mean: {chol_data.mean():.1f}')
ax6.set_title('Total Cholesterol Distribution', fontsize=11, fontweight='bold')
ax6.set_xlabel('Total Cholesterol (mg/dL)', fontsize=10)
ax6.set_ylabel('Frequency', fontsize=10)
ax6.legend()
ax6.grid(alpha=0.3)

# Age Distribution
ax7 = fig.add_subplot(gs[2, 0])
age_data = pd.to_numeric(df['Age'], errors='coerce').dropna()
ax7.hist(age_data, bins=30, color='#3498db', edgecolor='black', alpha=0.8)
ax7.axvline(age_data.mean(), color='darkblue', linestyle='--', linewidth=2.5, label=f'Mean: {age_data.mean():.1f}')
ax7.set_title('Age Distribution', fontsize=11, fontweight='bold')
ax7.set_xlabel('Age (years)', fontsize=10)
ax7.set_ylabel('Frequency', fontsize=10)
ax7.legend()
ax7.grid(alpha=0.3)

# Heart Rate
ax8 = fig.add_subplot(gs[2, 1])
hr_data = pd.to_numeric(df['Heart_Rate'], errors='coerce').dropna()
ax8.hist(hr_data, bins=25, color='#e67e22', edgecolor='black', alpha=0.8)
ax8.axvline(hr_data.mean(), color='darkorange', linestyle='--', linewidth=2.5, label=f'Mean: {hr_data.mean():.1f}')
ax8.set_title('Heart Rate Distribution', fontsize=11, fontweight='bold')
ax8.set_xlabel('Heart Rate (bpm)', fontsize=10)
ax8.set_ylabel('Frequency', fontsize=10)
ax8.legend()
ax8.grid(alpha=0.3)

# Waist Circumference
ax9 = fig.add_subplot(gs[2, 2])
waist_data = pd.to_numeric(df['Waist_Circumference_cm'], errors='coerce').dropna()
ax9.hist(waist_data, bins=30, color='#8e44ad', edgecolor='black', alpha=0.8)
ax9.axvline(waist_data.mean(), color='darkviolet', linestyle='--', linewidth=2.5, label=f'Mean: {waist_data.mean():.1f}')
ax9.set_title('Waist Circumference Distribution', fontsize=11, fontweight='bold')
ax9.set_xlabel('Waist Circumference (cm)', fontsize=10)
ax9.set_ylabel('Frequency', fontsize=10)
ax9.legend()
ax9.grid(alpha=0.3)

fig.suptitle('Health Metrics Statistical Overview', fontsize=14, fontweight='bold', y=0.995)
plt.savefig(f'{output_dir}/02_health_metrics_dashboard.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: 02_health_metrics_dashboard.png\n")

# ============================================================================
# VISUALIZATION 3: Risk by Demographics
# ============================================================================
print("Creating: 03_risk_by_demographics.png")
fig = plt.figure(figsize=(16, 10))
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.3)

# Risk by Gender
ax1 = fig.add_subplot(gs[0, 0])
gender_risk = pd.crosstab(df['Gender'], df['Diabetes_Risk'], normalize='index') * 100
gender_risk = gender_risk[['Low', 'Moderate', 'High']]
gender_risk.plot(kind='bar', ax=ax1, color=['#27ae60', '#f39c12', '#e74c3c'],
                 edgecolor='black', alpha=0.8, width=0.7)
ax1.set_title('Diabetes Risk by Gender', fontsize=11, fontweight='bold')
ax1.set_ylabel('Percentage (%)', fontsize=10)
ax1.set_xlabel('Gender', fontsize=10)
ax1.legend(title='Risk Level', loc='upper right', fontsize=9)
ax1.grid(axis='y', alpha=0.3)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')

# Risk by Residence
ax2 = fig.add_subplot(gs[0, 1])
residence_risk = pd.crosstab(df['Residence_Type'], df['Diabetes_Risk'], normalize='index') * 100
residence_risk = residence_risk[['Low', 'Moderate', 'High']]
residence_risk.plot(kind='bar', ax=ax2, color=['#27ae60', '#f39c12', '#e74c3c'],
                    edgecolor='black', alpha=0.8, width=0.7)
ax2.set_title('Diabetes Risk by Residence', fontsize=11, fontweight='bold')
ax2.set_ylabel('Percentage (%)', fontsize=10)
ax2.set_xlabel('Residence Type', fontsize=10)
ax2.legend(title='Risk Level', loc='upper right', fontsize=9)
ax2.grid(axis='y', alpha=0.3)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')

# Top Countries Risk
ax3 = fig.add_subplot(gs[0, 2])
top_countries = df['Country'].value_counts().head(10).index
country_risk = df[df['Country'].isin(top_countries)]['Diabetes_Risk'].value_counts()
ax3.barh(country_risk.index, country_risk.values, color=['#27ae60', '#f39c12', '#e74c3c'],
         edgecolor='black', alpha=0.8)
ax3.set_title('Risk Distribution in\nTop 10 Countries', fontsize=11, fontweight='bold')
ax3.set_xlabel('Count', fontsize=10)
ax3.grid(axis='x', alpha=0.3)
for i, v in enumerate(country_risk.values):
    ax3.text(v, i, f' {int(v):,}', va='center', fontweight='bold', fontsize=9)

# Age Group Risk
ax4 = fig.add_subplot(gs[1, 0])
age_clean = pd.to_numeric(df['Age'], errors='coerce')
age_groups = pd.cut(age_clean, bins=[0, 30, 40, 50, 60, 100], labels=['18-30', '31-40', '41-50', '51-60', '60+'])
age_risk = pd.crosstab(age_groups, df['Diabetes_Risk'], normalize='index') * 100
age_risk = age_risk[['Low', 'Moderate', 'High']]
age_risk.plot(kind='bar', ax=ax4, color=['#27ae60', '#f39c12', '#e74c3c'],
              edgecolor='black', alpha=0.8, width=0.7)
ax4.set_title('Diabetes Risk by Age Group', fontsize=11, fontweight='bold')
ax4.set_ylabel('Percentage (%)', fontsize=10)
ax4.set_xlabel('Age Group', fontsize=10)
ax4.legend(title='Risk Level', loc='upper left', fontsize=9)
ax4.grid(axis='y', alpha=0.3)
ax4.set_xticklabels(ax4.get_xticklabels(), rotation=45, ha='right')

# BMI vs Risk
ax5 = fig.add_subplot(gs[1, 1])
bmi_clean = pd.to_numeric(df['BMI'], errors='coerce')
risk_numeric = df['Diabetes_Risk'].map({'Low': 1, 'Moderate': 2, 'High': 3})
ax5.scatter(bmi_clean, risk_numeric, alpha=0.2, s=15, color='#9b59b6')
ax5.set_title('BMI vs Diabetes Risk', fontsize=11, fontweight='bold')
ax5.set_xlabel('BMI (kg/m²)', fontsize=10)
ax5.set_ylabel('Risk Level', fontsize=10)
ax5.set_yticks([1, 2, 3])
ax5.set_yticklabels(['Low', 'Moderate', 'High'])
ax5.grid(alpha=0.3)

# Glucose vs Risk
ax6 = fig.add_subplot(gs[1, 2])
glucose_clean = pd.to_numeric(df['Blood_Glucose'], errors='coerce')
ax6.scatter(glucose_clean, risk_numeric, alpha=0.2, s=15, color='#e74c3c')
ax6.set_title('Blood Glucose vs Risk', fontsize=11, fontweight='bold')
ax6.set_xlabel('Fasting Glucose (mg/dL)', fontsize=10)
ax6.set_ylabel('Risk Level', fontsize=10)
ax6.set_yticks([1, 2, 3])
ax6.set_yticklabels(['Low', 'Moderate', 'High'])
ax6.grid(alpha=0.3)

fig.suptitle('Diabetes Risk by Demographics & Clinical Metrics', fontsize=14, fontweight='bold', y=0.995)
plt.savefig(f'{output_dir}/03_risk_by_demographics.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: 03_risk_by_demographics.png\n")

# ============================================================================
# VISUALIZATION 4: Lifestyle Factors Analysis
# ============================================================================
print("Creating: 04_lifestyle_factors.png")
fig = plt.figure(figsize=(16, 10))
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.3)

# Smoking Status
ax1 = fig.add_subplot(gs[0, 0])
smoking = df['Smoking_Status'].value_counts()
colors_smoke = ['#95a5a6', '#e74c3c', '#f39c12']
ax1.bar(smoking.index, smoking.values, color=colors_smoke, edgecolor='black', alpha=0.8)
ax1.set_title('Smoking Status Distribution', fontsize=11, fontweight='bold')
ax1.set_ylabel('Number of Patients', fontsize=10)
for i, v in enumerate(smoking.values):
    ax1.text(i, v, f'{int(v):,}\n({v/len(df)*100:.1f}%)', ha='center', va='bottom', fontweight='bold', fontsize=9)
ax1.grid(axis='y', alpha=0.3)
ax1.tick_params(axis='x', rotation=45)

# Alcohol Consumption
ax2 = fig.add_subplot(gs[0, 1])
alcohol = df['Alcohol_Consumption'].value_counts()
colors_alcohol = ['#3498db', '#f39c12', '#e74c3c']
ax2.pie(alcohol.values, labels=alcohol.index, autopct='%1.1f%%', colors=colors_alcohol,
        explode=(0.05, 0.05, 0.1), textprops={'fontsize': 10, 'fontweight': 'bold'})
ax2.set_title('Alcohol Consumption', fontsize=11, fontweight='bold')

# Physical Activity
ax3 = fig.add_subplot(gs[0, 2])
activity = df['Physical_Activity_Level'].value_counts()
colors_activity = ['#e74c3c', '#f39c12', '#27ae60']
ax3.bar(activity.index, activity.values, color=colors_activity, edgecolor='black', alpha=0.8)
ax3.set_title('Physical Activity Level', fontsize=11, fontweight='bold')
ax3.set_ylabel('Number of Patients', fontsize=10)
for i, v in enumerate(activity.values):
    ax3.text(i, v, f'{int(v):,}\n({v/len(df)*100:.1f}%)', ha='center', va='bottom', fontweight='bold', fontsize=9)
ax3.grid(axis='y', alpha=0.3)
ax3.tick_params(axis='x', rotation=45)

# Exercise Hours
ax4 = fig.add_subplot(gs[1, 0])
exercise = pd.to_numeric(df['Exercise_Hours_Per_Week'], errors='coerce').dropna()
ax4.hist(exercise, bins=25, color='#3498db', edgecolor='black', alpha=0.8)
ax4.axvline(exercise.mean(), color='darkblue', linestyle='--', linewidth=2.5, label=f'Mean: {exercise.mean():.1f}h')
ax4.axvline(2.5, color='red', linestyle=':', linewidth=2, label='WHO minimum')
ax4.set_title('Exercise Hours Per Week', fontsize=11, fontweight='bold')
ax4.set_xlabel('Hours', fontsize=10)
ax4.set_ylabel('Frequency', fontsize=10)
ax4.legend(fontsize=9)
ax4.grid(alpha=0.3)

# Sleep Hours
ax5 = fig.add_subplot(gs[1, 1])
sleep = pd.to_numeric(df['Sleep_Hours'], errors='coerce').dropna()
ax5.hist(sleep, bins=20, color='#34495e', edgecolor='black', alpha=0.8)
ax5.axvline(sleep.mean(), color='black', linestyle='--', linewidth=2.5, label=f'Mean: {sleep.mean():.1f}h')
ax5.axvline(7, color='green', linestyle=':', linewidth=2, label='Recommended: 7-9h')
ax5.set_title('Sleep Hours Distribution', fontsize=11, fontweight='bold')
ax5.set_xlabel('Hours', fontsize=10)
ax5.set_ylabel('Frequency', fontsize=10)
ax5.legend(fontsize=9)
ax5.grid(alpha=0.3)

# Stress Level
ax6 = fig.add_subplot(gs[1, 2])
stress = pd.to_numeric(df['Stress_Level'], errors='coerce').dropna()
stress_cats = pd.cut(stress, bins=[0, 3, 6, 10], labels=['Low (0-3)', 'Moderate (4-6)', 'High (7-10)'])
stress_dist = stress_cats.value_counts()
colors_stress = ['#27ae60', '#f39c12', '#e74c3c']
ax6.bar(stress_dist.index, stress_dist.values, color=colors_stress, edgecolor='black', alpha=0.8)
ax6.set_title('Stress Level Distribution', fontsize=11, fontweight='bold')
ax6.set_ylabel('Number of Patients', fontsize=10)
for i, v in enumerate(stress_dist.values):
    ax6.text(i, v, f'{int(v):,}\n({v/len(df)*100:.1f}%)', ha='center', va='bottom', fontweight='bold', fontsize=9)
ax6.grid(axis='y', alpha=0.3)
ax6.tick_params(axis='x', rotation=15)

fig.suptitle('Lifestyle Factors & Behavioral Risk Assessment', fontsize=14, fontweight='bold', y=0.995)
plt.savefig(f'{output_dir}/04_lifestyle_factors.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: 04_lifestyle_factors.png\n")

# ============================================================================
# VISUALIZATION 5: Comorbidities & Medical Conditions
# ============================================================================
print("Creating: 05_comorbidities.png")
fig = plt.figure(figsize=(16, 8))
gs = GridSpec(2, 2, figure=fig, hspace=0.35, wspace=0.3)

# Comorbidity Prevalence
ax1 = fig.add_subplot(gs[0, :])
conditions = ['Hypertension', 'Heart_Disease', 'Fatty_Liver', 'PCOS', 'Family_History_Diabetes']
prevalence = {cond: (df[cond] == 'Yes').sum() for cond in conditions}
prevalence = dict(sorted(prevalence.items(), key=lambda x: x[1], reverse=True))
ax1.barh(list(prevalence.keys()), list(prevalence.values()), color='#e74c3c', edgecolor='black', alpha=0.8)
ax1.set_title('Medical Conditions Prevalence', fontsize=12, fontweight='bold')
ax1.set_xlabel('Number of Patients', fontsize=10)
for i, (cond, count) in enumerate(prevalence.items()):
    pct = count / len(df) * 100
    ax1.text(count, i, f' {int(count):,} ({pct:.1f}%)', va='center', fontweight='bold', fontsize=10)
ax1.grid(axis='x', alpha=0.3)

# Risk Rate by Condition
ax2 = fig.add_subplot(gs[1, 0])
risk_by_cond = {}
for cond in conditions:
    has_cond = df[df[cond] == 'Yes']
    if len(has_cond) > 0:
        high_risk_pct = (has_cond['Diabetes_Risk'] == 'High').sum() / len(has_cond) * 100
        risk_by_cond[cond] = high_risk_pct

risk_by_cond = dict(sorted(risk_by_cond.items(), key=lambda x: x[1], reverse=True))
ax2.barh(list(risk_by_cond.keys()), list(risk_by_cond.values()), color='#9b59b6', edgecolor='black', alpha=0.8)
ax2.set_title('High-Risk Rate Among Those\nWith Each Condition', fontsize=11, fontweight='bold')
ax2.set_xlabel('High-Risk Percentage (%)', fontsize=10)
ax2.set_xlim(0, 100)
for i, (cond, pct) in enumerate(risk_by_cond.items()):
    ax2.text(pct, i, f' {pct:.1f}%', va='center', fontweight='bold', fontsize=9)
ax2.grid(axis='x', alpha=0.3)

# Comorbidity Count Distribution
ax3 = fig.add_subplot(gs[1, 1])
comorbidity_count = (df[conditions] == 'Yes').sum(axis=1)
comorbidity_dist = comorbidity_count.value_counts().sort_index()
ax3.bar(comorbidity_dist.index, comorbidity_dist.values, color='#1abc9c', edgecolor='black', alpha=0.8, width=0.6)
ax3.set_title('Number of Comorbidities Per Patient', fontsize=11, fontweight='bold')
ax3.set_xlabel('Number of Conditions', fontsize=10)
ax3.set_ylabel('Number of Patients', fontsize=10)
for i, v in enumerate(comorbidity_dist.values):
    ax3.text(i, v, f'{int(v):,}', ha='center', va='bottom', fontweight='bold', fontsize=9)
ax3.grid(axis='y', alpha=0.3)

fig.suptitle('Comorbidities & Medical Conditions Analysis', fontsize=14, fontweight='bold', y=0.995)
plt.savefig(f'{output_dir}/05_comorbidities.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: 05_comorbidities.png\n")

# ============================================================================
# VISUALIZATION 6: Correlation Heatmap
# ============================================================================
print("Creating: 06_correlation_heatmap.png")
fig, ax = plt.subplots(figsize=(14, 10))

# Select numeric columns for correlation
numeric_cols = ['Age', 'BMI', 'Blood_Glucose', 'HbA1c', 'Insulin_Level',
                'Blood_Pressure_Systolic', 'Total_Cholesterol', 'HDL', 'LDL',
                'Exercise_Hours_Per_Week', 'Sleep_Hours', 'Stress_Level', 'Heart_Rate']

# Create correlation matrix
corr_data = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
correlation_matrix = corr_data.corr()

# Create heatmap
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='RdBu_r', center=0,
            cbar_kws={'label': 'Correlation'}, ax=ax, vmin=-1, vmax=1,
            square=True, linewidths=0.5, linecolor='gray', annot_kws={'fontsize': 9})

ax.set_title('Correlation Matrix: Health Metrics & Lifestyle Factors', fontsize=13, fontweight='bold', pad=20)
plt.xticks(rotation=45, ha='right', fontsize=9)
plt.yticks(rotation=0, fontsize=9)
plt.tight_layout()
plt.savefig(f'{output_dir}/06_correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: 06_correlation_heatmap.png\n")

# ============================================================================
# VISUALIZATION 7: Diet Quality & Health Outcomes
# ============================================================================
print("Creating: 07_lifestyle_health_outcomes.png")
fig = plt.figure(figsize=(16, 8))
gs = GridSpec(2, 2, figure=fig, hspace=0.3, wspace=0.3)

# Diet Quality vs Risk
ax1 = fig.add_subplot(gs[0, 0])
diet_risk = pd.crosstab(df['Diet_Quality'], df['Diabetes_Risk'], normalize='index') * 100
diet_risk = diet_risk[['Low', 'Moderate', 'High']]
diet_risk.plot(kind='bar', ax=ax1, color=['#27ae60', '#f39c12', '#e74c3c'],
               edgecolor='black', alpha=0.8, width=0.7)
ax1.set_title('Diabetes Risk by Diet Quality', fontsize=11, fontweight='bold')
ax1.set_ylabel('Percentage (%)', fontsize=10)
ax1.set_xlabel('Diet Quality', fontsize=10)
ax1.legend(title='Risk Level', fontsize=9)
ax1.grid(axis='y', alpha=0.3)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')

# Sugar Intake vs Risk
ax2 = fig.add_subplot(gs[0, 1])
sugar_risk = pd.crosstab(df['Sugar_Intake_Level'], df['Diabetes_Risk'], normalize='index') * 100
sugar_risk = sugar_risk[['Low', 'Moderate', 'High']]
sugar_risk.plot(kind='bar', ax=ax2, color=['#27ae60', '#f39c12', '#e74c3c'],
                edgecolor='black', alpha=0.8, width=0.7)
ax2.set_title('Diabetes Risk by Sugar Intake', fontsize=11, fontweight='bold')
ax2.set_ylabel('Percentage (%)', fontsize=10)
ax2.set_xlabel('Sugar Intake Level', fontsize=10)
ax2.legend(title='Risk Level', fontsize=9)
ax2.grid(axis='y', alpha=0.3)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')

# Work Type Distribution
ax3 = fig.add_subplot(gs[1, 0])
work_dist = df['Work_Type'].value_counts()
colors_work = plt.cm.Set3(range(len(work_dist)))
ax3.pie(work_dist.values, labels=work_dist.index, autopct='%1.1f%%', colors=colors_work,
        textprops={'fontsize': 9, 'fontweight': 'bold'})
ax3.set_title('Work Type Distribution', fontsize=11, fontweight='bold')

# Daily Water Intake
ax4 = fig.add_subplot(gs[1, 1])
water = pd.to_numeric(df['Daily_Water_Intake_L'], errors='coerce').dropna()
ax4.hist(water, bins=25, color='#3498db', edgecolor='black', alpha=0.8)
ax4.axvline(water.mean(), color='darkblue', linestyle='--', linewidth=2.5, label=f'Mean: {water.mean():.1f}L')
ax4.set_title('Daily Water Intake Distribution', fontsize=11, fontweight='bold')
ax4.set_xlabel('Liters', fontsize=10)
ax4.set_ylabel('Frequency', fontsize=10)
ax4.legend()
ax4.grid(alpha=0.3)

fig.suptitle('Lifestyle Factors & Health Outcomes', fontsize=14, fontweight='bold', y=0.995)
plt.savefig(f'{output_dir}/07_lifestyle_health_outcomes.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: 07_lifestyle_health_outcomes.png\n")

# ============================================================================
# SUMMARY
# ============================================================================
print("="*60)
print("✅ ALL VISUALIZATIONS GENERATED SUCCESSFULLY")
print("="*60)
print(f"\n📊 Generated 7 publication-ready charts:\n")
print("1. 01_risk_distribution.png")
print("2. 02_health_metrics_dashboard.png")
print("3. 03_risk_by_demographics.png")
print("4. 04_lifestyle_factors.png")
print("5. 05_comorbidities.png")
print("6. 06_correlation_heatmap.png")
print("7. 07_lifestyle_health_outcomes.png")
print(f"\n📁 Location: {output_dir}")
print("\n✨ All files saved at 300 DPI for GitHub & publications")
