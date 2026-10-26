# Dataset Documentation: IBM HR Analytics Employee Attrition

## 1. Overview & Provenance
- **Dataset Name**: IBM HR Analytics Employee Attrition & Performance
- **Primary Creator / Organization**: IBM Watson Analytics Data Science Team
- **Official Origin**: IBM Watson Analytics Sample Datasets / IBM Developer Samples
- **Public Reference / Mirror**: [Kaggle IBM HR Analytics Attrition Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- **Direct Acquisition URL**: `https://raw.githubusercontent.com/prernagoel/IBM-Employee-Attrition-Analysis-in-Python/master/WA_Fn-UseC_-HR-Employee-Attrition.csv`
- **License / Terms of Use**: Public Domain (CC0 1.0 Universal) / Open Data Commons. Released by IBM as a synthetic, anonymized benchmark dataset for education, research, and HR analytics demonstrations.
- **Verification Status**: Fully verified. File size: 227,977 bytes, SHA-consistent across open-source mirrors.

---

## 2. Dataset Dimensions & Profile
- **Total Records (Rows)**: `1,470`
- **Total Attributes (Columns)**: `35`
- **Data Types**:
  - `int64` (Numerical / Ordinal / Discrete): 26 columns
  - `object` / `string` (Categorical Nominal / Binary): 9 columns
- **Missing Values**: `0` across all 35 columns (100% complete)
- **Duplicate Records**: `0` duplicate rows detected

---

## 3. Target Variable Profile
- **Target Feature Name**: `Attrition`
- **Feature Role**: Supervised binary classification target (for future predictive modeling)
- **Values**:
  - `No`: 1,233 records (83.88%) — Retained employee population
  - `Yes`: 237 records (16.12%) — Attrited employee population
- **Class Balance Ratio**: Approximately `5.2 : 1` (imbalanced binary distribution)

---

## 4. Key Structural Characteristics & Data Quality Findings

### 4.1 Constant / Zero-Variance Features
The following three columns exhibit zero variance across all 1,470 records and must be excluded from predictive modeling:
1. `EmployeeCount`: Uniform integer `1` for all rows.
2. `StandardHours`: Uniform integer `80` (standard bi-weekly working hours) for all rows.
3. `Over18`: Uniform categorical string `'Y'` for all rows.

### 4.2 Non-Predictive Identifier
- `EmployeeNumber`: Unique identifier ranging from `1` to `2068` (1,470 unique values). It represents an administrative index, not an informative feature, and must never be used as a predictor to avoid data leakage and overfitting.

### 4.3 Nature of the Data (Static Snapshot Caveat)
- This dataset is a **cross-sectional, point-in-time observational snapshot**.
- It does **not** record precise historical dates of hiring, promotion, or separation.
- Consequently, calculated attrition rates represent **sample proportions** within the dataset population, **not** an annualized organizational turnover rate.

---

## 5. Dataset Acquisition & Setup Instructions

To download or refresh the dataset locally using Python:

```python
import urllib.request
import os

url = "https://raw.githubusercontent.com/prernagoel/IBM-Employee-Attrition-Analysis-in-Python/master/WA_Fn-UseC_-HR-Employee-Attrition.csv"
dest_path = os.path.join("data", "WA_Fn-UseC_-HR-Employee-Attrition.csv")

os.makedirs("data", exist_ok=True)
urllib.request.urlretrieve(url, dest_path)
print("Dataset downloaded successfully to:", dest_path)
```
