import os
import pytest
import pandas as pd

DATASET_PATH = os.path.join('data', 'WA_Fn-UseC_-HR-Employee-Attrition.csv')
FEATURE_DICT_PATH = os.path.join('outputs', 'tables', 'feature_dictionary.csv')

def test_dataset_exists_and_loads():
    """Verify that the dataset file exists and loads cleanly into a Pandas DataFrame."""
    assert os.path.exists(DATASET_PATH), f"Dataset file not found at {DATASET_PATH}"
    df = pd.read_csv(DATASET_PATH)
    assert not df.empty, "Dataset loaded but is unexpectedly empty."

def test_dataset_dimensions():
    """Verify that the dataset possesses the canonical dimensions: 1,470 rows and 35 columns."""
    df = pd.read_csv(DATASET_PATH)
    assert df.shape == (1470, 35), f"Expected shape (1470, 35), but got {df.shape}"

def test_target_variable():
    """Verify that the target column 'Attrition' exists and matches verified benchmark counts."""
    df = pd.read_csv(DATASET_PATH)
    assert 'Attrition' in df.columns, "'Attrition' column missing from dataset."
    counts = df['Attrition'].value_counts().to_dict()
    assert counts.get('No') == 1233, f"Expected 1,233 'No' records, found {counts.get('No')}"
    assert counts.get('Yes') == 237, f"Expected 237 'Yes' records, found {counts.get('Yes')}"
    
    # Calculate sample attrition rate
    rate = (counts['Yes'] / len(df)) * 100
    assert abs(rate - 16.1224) < 0.01, f"Expected sample attrition rate ~16.12%, got {rate:.2f}%"

def test_no_missing_values():
    """Verify that the dataset has zero missing values across all columns."""
    df = pd.read_csv(DATASET_PATH)
    null_count = df.isnull().sum().sum()
    assert null_count == 0, f"Expected 0 missing values, found {null_count}"

def test_no_duplicate_rows():
    """Verify that the dataset contains zero duplicated observations."""
    df = pd.read_csv(DATASET_PATH)
    dup_count = df.duplicated().sum()
    assert dup_count == 0, f"Expected 0 duplicate rows, found {dup_count}"

def test_constant_columns_identified():
    """Verify that the three known zero-variance features are constant."""
    df = pd.read_csv(DATASET_PATH)
    assert df['EmployeeCount'].nunique() == 1 and df['EmployeeCount'].iloc[0] == 1
    assert df['StandardHours'].nunique() == 1 and df['StandardHours'].iloc[0] == 80
    assert df['Over18'].nunique() == 1 and df['Over18'].iloc[0] == 'Y'

def test_employee_number_uniqueness():
    """Verify that EmployeeNumber is a distinct administrative key."""
    df = pd.read_csv(DATASET_PATH)
    assert df['EmployeeNumber'].nunique() == len(df), "EmployeeNumber contains duplicate IDs"

def test_feature_dictionary_completeness():
    """Verify that the feature dictionary covers all 35 columns from the dataset."""
    assert os.path.exists(FEATURE_DICT_PATH), f"Feature dictionary missing at {FEATURE_DICT_PATH}"
    df_data = pd.read_csv(DATASET_PATH)
    df_dict = pd.read_csv(FEATURE_DICT_PATH)
    
    assert len(df_dict) == 35, f"Expected 35 features in dictionary, found {len(df_dict)}"
    data_cols = set(df_data.columns)
    dict_cols = set(df_dict['Feature'])
    assert data_cols == dict_cols, f"Mismatch between dataset and feature dictionary: {data_cols ^ dict_cols}"

def test_generated_figures_exist():
    """Verify that all core EDA visualization figures were generated."""
    expected_figures = [
        'attrition_distribution.png',
        'attrition_by_department.png',
        'attrition_by_job_role.png',
        'attrition_by_overtime.png',
        'tenure_and_income_distributions.png',
        'satisfaction_and_wlb_attrition.png',
        'correlation_heatmap.png',
        'missing_values_summary.png'
    ]
    for fig in expected_figures:
        path = os.path.join('outputs', 'figures', fig)
        assert os.path.exists(path), f"Figure missing: {path}"
        assert os.path.getsize(path) > 1000, f"Figure file suspiciously small: {path}"

def test_workflow_diagram_exists():
    """Verify that both Mermaid source and rendered PNG workflow diagrams exist."""
    mmd_path = os.path.join('diagrams', 'project_workflow.mmd')
    png_path = os.path.join('diagrams', 'project_workflow.png')
    assert os.path.exists(mmd_path), f"Mermaid workflow diagram missing: {mmd_path}"
    assert os.path.exists(png_path), f"Rendered workflow diagram missing: {png_path}"
    assert os.path.getsize(png_path) > 5000, f"Workflow PNG suspiciously small: {png_path}"

def test_pdf_reports_exist():
    """Verify that both executive PDF reports were compiled and are non-empty."""
    dataset_report = os.path.join('reports', 'dataset_report.pdf')
    ethics_report = os.path.join('reports', 'ethics_report.pdf')
    
    assert os.path.exists(dataset_report), f"Dataset report PDF missing: {dataset_report}"
    assert os.path.exists(ethics_report), f"Ethics report PDF missing: {ethics_report}"
    assert os.path.getsize(dataset_report) > 50000, f"Dataset report PDF suspiciously small: {os.path.getsize(dataset_report)} bytes"
    assert os.path.getsize(ethics_report) > 5000, f"Ethics report PDF suspiciously small: {os.path.getsize(ethics_report)} bytes"

def test_documentation_files_exist():
    """Verify that all mandatory documentation markdown files exist in docs/."""
    expected_docs = [
        'business_problem_statement.md',
        'stakeholder_analysis.md',
        'feature_dictionary.md',
        'business_kpis.md',
        'ethics_report.md',
        'project_roadmap.md'
    ]
    for doc in expected_docs:
        path = os.path.join('docs', doc)
        assert os.path.exists(path), f"Documentation file missing: {path}"
        assert os.path.getsize(path) > 500, f"Documentation file suspiciously small: {path}"
