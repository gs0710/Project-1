# Employee Attrition Analytics: Comprehensive Feature Dictionary

## 1. Overview and Feature Inventory
This feature dictionary documents all **35 actual columns** present in the IBM HR Analytics Employee Attrition dataset.
No fabricated or unverified columns are included. Each attribute is categorized according to its measurement scale, data type, business relevance, proposed modeling role, data quality concerns, and ethical/privacy considerations.

| Column Count | Total Records | Missing Values | Target Attribute | Positive Class |
| :---: | :---: | :---: | :---: | :---: |
| **35** | **1,470** | **0 (100% Complete)** | `Attrition` | `Yes` (237 records, 16.12%) |

---

## 2. Feature Classification Taxonomy
- **Target Variable (1)**: `Attrition` (Binary: Yes / No)
- **Constant / Zero-Variance Attributes (3)**: `EmployeeCount`, `StandardHours`, `Over18` *(Must be excluded from modeling)*
- **Administrative Identifiers (1)**: `EmployeeNumber` *(Non-predictive; exclude to prevent data leakage)*
- **Sensitive / Protected Demographics (3)**: `Age`, `Gender`, `MaritalStatus` *(Subject to strict ethical/bias auditing)*
- **Subjective Sentiment & Satisfaction Ratings (5)**: `EnvironmentSatisfaction`, `JobInvolvement`, `JobSatisfaction`, `RelationshipSatisfaction`, `WorkLifeBalance` *(Likert ordinal scales)*
- **Tenure & Career Mobility Metrics (5)**: `TotalWorkingYears`, `YearsAtCompany`, `YearsInCurrentRole`, `YearsSinceLastPromotion`, `YearsWithCurrManager`
- **Compensation & Equity Attributes (6)**: `DailyRate`, `HourlyRate`, `MonthlyIncome`, `MonthlyRate`, `PercentSalaryHike`, `StockOptionLevel`
- **Role & Organizational Placement (4)**: `Department`, `JobRole`, `JobLevel`, `EducationField`
- **Work Conditions & Demands (3)**: `BusinessTravel`, `DistanceFromHome`, `OverTime`
- **Professional Background & Training (4)**: `Education`, `NumCompaniesWorked`, `PerformanceRating`, `TrainingTimesLastYear`

---

## 3. Comprehensive Column-by-Column Feature Dictionary

### 1. `Age`
- **Business Meaning**: Chronological age of the employee in completed years
- **Data Type**: `int64`
- **Feature Type**: Numerical Discrete
- **Valid / Observed Values**: 18 to 60 (Min: 18, Max: 60, Mean: 36.92)
- **Units / Measurement Scale**: Years
- **Missing Value Count**: 0
- **Analytical Relevance**: Career lifecycle stage, generational stability, retirement proximity
- **Proposed Role in Future Modeling**: **Candidate Predictor (Demographic)**
- **Data Quality Concerns**: Right-skewed, bounded range (no minors or individuals >60)
- **Privacy & Ethical Considerations**: Protected attribute under Age Discrimination in Employment Act (ADEA). Model must be monitored for disparate impact against older workers.

### 2. `Attrition`
- **Business Meaning**: Termination status of the employee (whether employee has left the company)
- **Data Type**: `object`
- **Feature Type**: Target (Binary)
- **Valid / Observed Values**: "Yes" (237, 16.12%), "No" (1233, 83.88%)
- **Units / Measurement Scale**: Binary categorical flag
- **Missing Value Count**: 0
- **Analytical Relevance**: Primary outcome variable for organizational retention analytics
- **Proposed Role in Future Modeling**: **Target Variable (Positive class: "Yes")**
- **Data Quality Concerns**: Significant class imbalance (~5.2:1 ratio). Static snapshot without exact departure date or exit type (voluntary vs involuntary).
- **Privacy & Ethical Considerations**: Direct label of employee departure. Predictions must not be used to penalize employees.

### 3. `BusinessTravel`
- **Business Meaning**: Frequency of official company travel required for the role
- **Data Type**: `object`
- **Feature Type**: Categorical Nominal / Ordinal
- **Valid / Observed Values**: "Travel_Rarely" (1043), "Travel_Frequently" (277), "Non-Travel" (150)
- **Units / Measurement Scale**: Categorical levels
- **Missing Value Count**: 0
- **Analytical Relevance**: Workload stress, travel fatigue, travel-induced burnout
- **Proposed Role in Future Modeling**: **Candidate Predictor (Work Environment)**
- **Data Quality Concerns**: Natural ordinal hierarchy present (Non-Travel < Rarely < Frequently)
- **Privacy & Ethical Considerations**: Operational job condition; low ethical sensitivity.

### 4. `DailyRate`
- **Business Meaning**: Daily monetary compensation / internal billing rate
- **Data Type**: `int64`
- **Feature Type**: Numerical Continuous
- **Valid / Observed Values**: 102 to 1499 (Mean: 802.49, Median: 802)
- **Units / Measurement Scale**: USD ($) per day
- **Missing Value Count**: 0
- **Analytical Relevance**: Compensation adequacy and perceived equity
- **Proposed Role in Future Modeling**: **Candidate Predictor (Compensation)**
- **Data Quality Concerns**: High variance, uniform distribution indicative of synthetic generation
- **Privacy & Ethical Considerations**: Compensation confidentiality. In production, salary data must be access-controlled.

### 5. `Department`
- **Business Meaning**: Primary organizational business unit where employee is assigned
- **Data Type**: `object`
- **Feature Type**: Categorical Nominal
- **Valid / Observed Values**: "Research & Development" (961), "Sales" (446), "Human Resources" (63)
- **Units / Measurement Scale**: Categorical levels
- **Missing Value Count**: 0
- **Analytical Relevance**: Subculture differences, divisional workload, department leadership differences
- **Proposed Role in Future Modeling**: **Candidate Predictor (Organizational Context)**
- **Data Quality Concerns**: Small sample size for Human Resources (63 records, 4.3% of workforce)
- **Privacy & Ethical Considerations**: Risk of re-identification in very small subgroups.

### 6. `DistanceFromHome`
- **Business Meaning**: Distance from employee residential address to primary workplace
- **Data Type**: `int64`
- **Feature Type**: Numerical Discrete
- **Valid / Observed Values**: 1 to 29 (Mean: 9.19, Median: 7)
- **Units / Measurement Scale**: Miles / Kilometers
- **Missing Value Count**: 0
- **Analytical Relevance**: Commuting friction, transportation stress, demand for flexible/remote work
- **Proposed Role in Future Modeling**: **Candidate Predictor (Work-Life Context)**
- **Data Quality Concerns**: Does not record commute duration in minutes or hybrid/remote work arrangement days
- **Privacy & Ethical Considerations**: Proximate residential geolocation data requires privacy masking in enterprise systems.

### 7. `Education`
- **Business Meaning**: Highest educational attainment level achieved by employee
- **Data Type**: `int64`
- **Feature Type**: Categorical Ordinal
- **Valid / Observed Values**: 1: Below College (170), 2: College (282), 3: Bachelor (572), 4: Master (398), 5: Doctor (48)
- **Units / Measurement Scale**: Ordinal 5-point scale
- **Missing Value Count**: 0
- **Analytical Relevance**: Educational overqualification or mismatch with role requirements
- **Proposed Role in Future Modeling**: **Candidate Predictor (Qualifications)**
- **Data Quality Concerns**: Integer encoded; should be treated as ordinal rather than continuous interval scale
- **Privacy & Ethical Considerations**: Educational pedigree should not inadvertently reinforce systemic hiring biases.

### 8. `EducationField`
- **Business Meaning**: Academic discipline of highest educational qualification
- **Data Type**: `object`
- **Feature Type**: Categorical Nominal
- **Valid / Observed Values**: "Life Sciences" (606), "Medical" (464), "Marketing" (159), "Technical Degree" (132), "Other" (82), "Human Resources" (27)
- **Units / Measurement Scale**: Categorical levels
- **Missing Value Count**: 0
- **Analytical Relevance**: Alignment between academic specialization and assigned functional domain
- **Proposed Role in Future Modeling**: **Candidate Predictor (Qualifications)**
- **Data Quality Concerns**: Low sample size for Human Resources field (27)
- **Privacy & Ethical Considerations**: Low risk.

### 9. `EmployeeCount`
- **Business Meaning**: Standard headcount counter per row
- **Data Type**: `int64`
- **Feature Type**: Constant / Zero Variance
- **Valid / Observed Values**: 1 (Uniform across all 1470 rows)
- **Units / Measurement Scale**: Count integer
- **Missing Value Count**: 0
- **Analytical Relevance**: None (zero variance provides zero informational entropy)
- **Proposed Role in Future Modeling**: **Exclude from Analysis and Future Modeling**
- **Data Quality Concerns**: Redundant artifact of tabular export
- **Privacy & Ethical Considerations**: None.

### 10. `EmployeeNumber`
- **Business Meaning**: Unique corporate identifier assigned to each employee record
- **Data Type**: `int64`
- **Feature Type**: Identifier
- **Valid / Observed Values**: 1 to 2068 (1470 unique values)
- **Units / Measurement Scale**: Administrative ID
- **Missing Value Count**: 0
- **Analytical Relevance**: None (administrative key)
- **Proposed Role in Future Modeling**: **Exclude from Predictive Modeling (Record Identifier only)**
- **Data Quality Concerns**: Non-sequential gaps indicate historic deletions or pre-existing turnover
- **Privacy & Ethical Considerations**: High risk of direct identification. Must be pseudonymized or removed in reporting.

### 11. `EnvironmentSatisfaction`
- **Business Meaning**: Survey rating of satisfaction with physical and psychological work environment
- **Data Type**: `int64`
- **Feature Type**: Categorical Ordinal
- **Valid / Observed Values**: 1: Low (284), 2: Medium (287), 3: High (453), 4: Very High (446)
- **Units / Measurement Scale**: Likert 4-point scale
- **Missing Value Count**: 0
- **Analytical Relevance**: Workplace safety, team climate, facilities, culture satisfaction
- **Proposed Role in Future Modeling**: **Candidate Predictor (Engagement / Sentiment)**
- **Data Quality Concerns**: Self-reported survey data subject to social desirability bias or response latency
- **Privacy & Ethical Considerations**: Survey confidentiality must be maintained to prevent retaliation from managers.

### 12. `Gender`
- **Business Meaning**: Self-identified biological sex / gender identity of employee
- **Data Type**: `object`
- **Feature Type**: Categorical Binary (Demographic)
- **Valid / Observed Values**: "Male" (882, 60%), "Female" (588, 40%)
- **Units / Measurement Scale**: Binary categories
- **Missing Value Count**: 0
- **Analytical Relevance**: Demographic parity and equity auditing
- **Proposed Role in Future Modeling**: **Candidate Feature for Bias Auditing / Fairness Assessment (DO NOT use for disparate treatment)**
- **Data Quality Concerns**: Binary classification only; does not capture non-binary or diverse identities
- **Privacy & Ethical Considerations**: Protected attribute under Title VII of Civil Rights Act and global labor laws. High fairness sensitivity.

### 13. `HourlyRate`
- **Business Meaning**: Hourly wage rate in USD
- **Data Type**: `int64`
- **Feature Type**: Numerical Continuous
- **Valid / Observed Values**: 30 to 100 (Mean: 65.89, Median: 66)
- **Units / Measurement Scale**: USD ($) per hour
- **Missing Value Count**: 0
- **Analytical Relevance**: Compensation evaluation for hourly-based assignments
- **Proposed Role in Future Modeling**: **Candidate Predictor (Compensation)**
- **Data Quality Concerns**: Weak correlation with MonthlyIncome, reflecting synthetic distribution design
- **Privacy & Ethical Considerations**: Confidential compensation data.

### 14. `JobInvolvement`
- **Business Meaning**: Survey rating assessing degree of psychological identification with work
- **Data Type**: `int64`
- **Feature Type**: Categorical Ordinal
- **Valid / Observed Values**: 1: Low (83), 2: Medium (375), 3: High (868), 4: Very High (144)
- **Units / Measurement Scale**: Likert 4-point scale
- **Missing Value Count**: 0
- **Analytical Relevance**: Core psychological predictor of engagement and commitment
- **Proposed Role in Future Modeling**: **Candidate Predictor (Engagement / Sentiment)**
- **Data Quality Concerns**: Concentrated in category 3 (59% of respondents)
- **Privacy & Ethical Considerations**: Must not be used in performance appraisal or punitive evaluations.

### 15. `JobLevel`
- **Business Meaning**: Hierarchical organizational seniority grade
- **Data Type**: `int64`
- **Feature Type**: Categorical Ordinal
- **Valid / Observed Values**: 1 (543), 2 (534), 3 (218), 4 (106), 5 (69)
- **Units / Measurement Scale**: Ordinal 5-level scale
- **Missing Value Count**: 0
- **Analytical Relevance**: Seniority, career progression tier, organizational responsibility
- **Proposed Role in Future Modeling**: **Candidate Predictor (Organizational Context)**
- **Data Quality Concerns**: Pyramidal distribution; fewer records at level 4 and 5
- **Privacy & Ethical Considerations**: High correlation with compensation and age.

### 16. `JobRole`
- **Business Meaning**: Specific functional operational position held by employee
- **Data Type**: `object`
- **Feature Type**: Categorical Nominal
- **Valid / Observed Values**: Sales Executive (326), Research Scientist (292), Lab Tech (259), Manufacturing Director (145), Healthcare Rep (131), Manager (102), Sales Rep (83), Research Director (80), HR (52)
- **Units / Measurement Scale**: 9 distinct job roles
- **Missing Value Count**: 0
- **Analytical Relevance**: Differential role-specific turnover pressures, market demand, burnout rates
- **Proposed Role in Future Modeling**: **Candidate Predictor (Core Role)**
- **Data Quality Concerns**: High cardinality (9 classes); requires one-hot or target encoding in modeling
- **Privacy & Ethical Considerations**: Niche roles combined with department could enable individual re-identification.

### 17. `JobSatisfaction`
- **Business Meaning**: Self-reported satisfaction with job duties and conditions
- **Data Type**: `int64`
- **Feature Type**: Categorical Ordinal
- **Valid / Observed Values**: 1: Low (289), 2: Medium (280), 3: High (442), 4: Very High (459)
- **Units / Measurement Scale**: Likert 4-point scale
- **Missing Value Count**: 0
- **Analytical Relevance**: Established business predictor of voluntary resignation
- **Proposed Role in Future Modeling**: **Candidate Predictor (Engagement / Sentiment)**
- **Data Quality Concerns**: Snapshot metric; misses temporal trends or sudden sentiment drops
- **Privacy & Ethical Considerations**: Confidential sentiment; employees must trust responses cannot trigger adverse action.

### 18. `MaritalStatus`
- **Business Meaning**: Legal marital status of employee
- **Data Type**: `object`
- **Feature Type**: Categorical Nominal (Demographic)
- **Valid / Observed Values**: "Married" (673, 45.8%), "Single" (470, 32.0%), "Divorced" (327, 22.2%)
- **Units / Measurement Scale**: Categorical levels
- **Missing Value Count**: 0
- **Analytical Relevance**: Personal lifestyle demands and geographic mobility
- **Proposed Role in Future Modeling**: **Sensitive Demographic Feature (Requires strict fairness audit; exclude from automated action)**
- **Data Quality Concerns**: Does not account for domestic partnerships or dependents
- **Privacy & Ethical Considerations**: Highly sensitive personal status. Employment decisions cannot legally discriminate based on marital status.

### 19. `MonthlyIncome`
- **Business Meaning**: Gross monthly earnings in USD
- **Data Type**: `int64`
- **Feature Type**: Numerical Continuous
- **Valid / Observed Values**: 1009 to 19999 (Mean: 6502.93, Median: 4919)
- **Units / Measurement Scale**: USD ($) per month
- **Missing Value Count**: 0
- **Analytical Relevance**: Pay competitiveness, living wage adequacy, compensation equity
- **Proposed Role in Future Modeling**: **Candidate Predictor (Compensation)**
- **Data Quality Concerns**: Positively right-skewed; requires log-transformation or scaling for linear models
- **Privacy & Ethical Considerations**: Strictly confidential salary data. High internal sensitivity.

### 20. `MonthlyRate`
- **Business Meaning**: Allocated monthly billing or cost rate
- **Data Type**: `int64`
- **Feature Type**: Numerical Continuous
- **Valid / Observed Values**: 2094 to 26999 (Mean: 14313.10, Median: 14235.5)
- **Units / Measurement Scale**: USD ($) per month
- **Missing Value Count**: 0
- **Analytical Relevance**: Cost-accounting rate per employee
- **Proposed Role in Future Modeling**: **Candidate Predictor (Compensation)**
- **Data Quality Concerns**: Near-uniform distribution typical of synthetic data generation
- **Privacy & Ethical Considerations**: Financial data.

### 21. `NumCompaniesWorked`
- **Business Meaning**: Total number of prior distinct corporate employers
- **Data Type**: `int64`
- **Feature Type**: Numerical Discrete
- **Valid / Observed Values**: 0 to 9 (Mean: 2.69, Median: 2)
- **Units / Measurement Scale**: Count of prior employers
- **Missing Value Count**: 0
- **Analytical Relevance**: Job-hopping propensity, external marketability, tenure volatility
- **Proposed Role in Future Modeling**: **Candidate Predictor (Career History)**
- **Data Quality Concerns**: Value 0 indicates only current company worked; values up to 9 indicate high mobility
- **Privacy & Ethical Considerations**: Prior employment history must be evaluated without undue prejudice.

### 22. `Over18`
- **Business Meaning**: Legal adulthood verification flag
- **Data Type**: `object`
- **Feature Type**: Constant / Zero Variance
- **Valid / Observed Values**: "Y" (Uniform across all 1470 rows)
- **Units / Measurement Scale**: Binary flag
- **Missing Value Count**: 0
- **Analytical Relevance**: None (zero variance)
- **Proposed Role in Future Modeling**: **Exclude from Analysis and Future Modeling**
- **Data Quality Concerns**: Redundant constant column
- **Privacy & Ethical Considerations**: None.

### 23. `OverTime`
- **Business Meaning**: Whether the employee routinely works overtime hours beyond standard shift
- **Data Type**: `object`
- **Feature Type**: Categorical Binary
- **Valid / Observed Values**: "No" (1054, 71.7%), "Yes" (416, 28.3%)
- **Units / Measurement Scale**: Binary flag
- **Missing Value Count**: 0
- **Analytical Relevance**: Work overload, chronic exhaustion, burnout, work-life conflict
- **Proposed Role in Future Modeling**: **Candidate Predictor (Workload / Demands)**
- **Data Quality Concerns**: Binary indicator does not record quantitative overtime hours worked per week
- **Privacy & Ethical Considerations**: Overtime mandates can impact labor standard compliance and employee well-being.

### 24. `PercentSalaryHike`
- **Business Meaning**: Percentage increase in annual compensation awarded at latest performance cycle
- **Data Type**: `int64`
- **Feature Type**: Numerical Discrete
- **Valid / Observed Values**: 11% to 25% (Mean: 15.21%, Median: 14%)
- **Units / Measurement Scale**: Percentage (%)
- **Missing Value Count**: 0
- **Analytical Relevance**: Reward perception, merit recognition, incentive motivation
- **Proposed Role in Future Modeling**: **Candidate Predictor (Compensation / Recognition)**
- **Data Quality Concerns**: Bounded between 11% and 25%; does not include zero or sub-10% raises
- **Privacy & Ethical Considerations**: Perceptions of pay inequity affect morale.

### 25. `PerformanceRating`
- **Business Meaning**: Annual supervisory performance assessment rating
- **Data Type**: `int64`
- **Feature Type**: Categorical Ordinal
- **Valid / Observed Values**: 3: Excellent (1244, 84.6%), 4: Outstanding (226, 15.4%)
- **Units / Measurement Scale**: Ordinal rating
- **Missing Value Count**: 0
- **Analytical Relevance**: Correlation between high performance and retention or flight risk
- **Proposed Role in Future Modeling**: **Candidate Predictor (Performance)**
- **Data Quality Concerns**: Extreme rating leniency: only ratings 3 and 4 exist; ratings 1 (Low) and 2 (Good) are missing
- **Privacy & Ethical Considerations**: Supervisory performance ratings are subjective and prone to appraisal biases.

### 26. `RelationshipSatisfaction`
- **Business Meaning**: Self-reported satisfaction with workplace interpersonal relationships
- **Data Type**: `int64`
- **Feature Type**: Categorical Ordinal
- **Valid / Observed Values**: 1: Low (276), 2: Medium (303), 3: High (459), 4: Very High (432)
- **Units / Measurement Scale**: Likert 4-point scale
- **Missing Value Count**: 0
- **Analytical Relevance**: Collegiality, team psychological safety, peer cohesion
- **Proposed Role in Future Modeling**: **Candidate Predictor (Interpersonal Climate)**
- **Data Quality Concerns**: Subjective survey rating
- **Privacy & Ethical Considerations**: Confidential survey data.

### 27. `StandardHours`
- **Business Meaning**: Standard bi-weekly working hours expected for standard employment contract
- **Data Type**: `int64`
- **Feature Type**: Constant / Zero Variance
- **Valid / Observed Values**: 80 (Uniform across all 1470 rows)
- **Units / Measurement Scale**: Hours per pay period
- **Missing Value Count**: 0
- **Analytical Relevance**: None (zero variance)
- **Proposed Role in Future Modeling**: **Exclude from Analysis and Future Modeling**
- **Data Quality Concerns**: Redundant constant column
- **Privacy & Ethical Considerations**: None.

### 28. `StockOptionLevel`
- **Business Meaning**: Tier level of equity stock options awarded to employee
- **Data Type**: `int64`
- **Feature Type**: Categorical Ordinal
- **Valid / Observed Values**: 0 (631), 1 (596), 2 (158), 3 (85)
- **Units / Measurement Scale**: Ordinal tier (0 to 3)
- **Missing Value Count**: 0
- **Analytical Relevance**: Long-term financial incentive, equity golden handcuffs, executive retention
- **Proposed Role in Future Modeling**: **Candidate Predictor (Compensation)**
- **Data Quality Concerns**: Significant zero-inflation (42.9% receive zero options)
- **Privacy & Ethical Considerations**: Executive / management compensation privilege transparency.

### 29. `TotalWorkingYears`
- **Business Meaning**: Cumulative total professional career experience across all organizations
- **Data Type**: `int64`
- **Feature Type**: Numerical Discrete
- **Valid / Observed Values**: 0 to 40 (Mean: 11.28, Median: 10)
- **Units / Measurement Scale**: Years
- **Missing Value Count**: 0
- **Analytical Relevance**: Overall career maturity, industry seasoning, seniority
- **Proposed Role in Future Modeling**: **Candidate Predictor (Career Lifecycle)**
- **Data Quality Concerns**: Strong collinearity with Age and JobLevel
- **Privacy & Ethical Considerations**: Age proxy.

### 30. `TrainingTimesLastYear`
- **Business Meaning**: Number of formal professional development and training courses attended
- **Data Type**: `int64`
- **Feature Type**: Numerical Discrete
- **Valid / Observed Values**: 0 to 6 (Mean: 2.80, Median: 3)
- **Units / Measurement Scale**: Count of training sessions
- **Missing Value Count**: 0
- **Analytical Relevance**: Upskilling investment, organizational commitment to growth, skill obsolescence
- **Proposed Role in Future Modeling**: **Candidate Predictor (Learning & Development)**
- **Data Quality Concerns**: Does not record training quality, relevance, or voluntary vs mandatory nature
- **Privacy & Ethical Considerations**: Fair access to training opportunities across demographics.

### 31. `WorkLifeBalance`
- **Business Meaning**: Survey rating of balance between personal life and job obligations
- **Data Type**: `int64`
- **Feature Type**: Categorical Ordinal
- **Valid / Observed Values**: 1: Bad (80), 2: Good (344), 3: Better (893), 4: Best (153)
- **Units / Measurement Scale**: Likert 4-point scale
- **Missing Value Count**: 0
- **Analytical Relevance**: Life stage flexibility, personal stress, caretaking friction, retention driver
- **Proposed Role in Future Modeling**: **Candidate Predictor (Well-Being)**
- **Data Quality Concerns**: Heavily clustered around level 3 (60.7% of employees)
- **Privacy & Ethical Considerations**: Personal life balance is private; interventions must be supportive, not invasive.

### 32. `YearsAtCompany`
- **Business Meaning**: Continuous tenure in completed years with current organization
- **Data Type**: `int64`
- **Feature Type**: Numerical Discrete
- **Valid / Observed Values**: 0 to 40 (Mean: 7.01, Median: 5)
- **Units / Measurement Scale**: Years
- **Missing Value Count**: 0
- **Analytical Relevance**: Organizational loyalty, socialization, institutional memory retention
- **Proposed Role in Future Modeling**: **Candidate Predictor (Tenure)**
- **Data Quality Concerns**: Right-skewed with long tail (up to 40 years)
- **Privacy & Ethical Considerations**: Tenure must be examined relative to role opportunities.

### 33. `YearsInCurrentRole`
- **Business Meaning**: Continuous tenure in completed years within current assigned job role
- **Data Type**: `int64`
- **Feature Type**: Numerical Discrete
- **Valid / Observed Values**: 0 to 18 (Mean: 4.23, Median: 3)
- **Units / Measurement Scale**: Years
- **Missing Value Count**: 0
- **Analytical Relevance**: Role fatigue, mastery plateau, readiness for lateral move or promotion
- **Proposed Role in Future Modeling**: **Candidate Predictor (Tenure / Mobility)**
- **Data Quality Concerns**: Cannot exceed YearsAtCompany
- **Privacy & Ethical Considerations**: Stagnation risk.

### 34. `YearsSinceLastPromotion`
- **Business Meaning**: Elapsed years since the employee received their last upward promotion
- **Data Type**: `int64`
- **Feature Type**: Numerical Discrete
- **Valid / Observed Values**: 0 to 15 (Mean: 2.19, Median: 1)
- **Units / Measurement Scale**: Years
- **Missing Value Count**: 0
- **Analytical Relevance**: Career velocity, perceived promotional bottlenecks, upward mobility fairness
- **Proposed Role in Future Modeling**: **Candidate Predictor (Career Growth)**
- **Data Quality Concerns**: Value 0 includes newly hired as well as newly promoted employees
- **Privacy & Ethical Considerations**: Transparency in promotional criteria.

### 35. `YearsWithCurrManager`
- **Business Meaning**: Continuous duration working under supervision of current manager
- **Data Type**: `int64`
- **Feature Type**: Numerical Discrete
- **Valid / Observed Values**: 0 to 17 (Mean: 4.12, Median: 3)
- **Units / Measurement Scale**: Years
- **Missing Value Count**: 0
- **Analytical Relevance**: Supervisory continuity, leadership relationship quality ("people leave managers")
- **Proposed Role in Future Modeling**: **Candidate Predictor (Management Relationship)**
- **Data Quality Concerns**: Cannot exceed YearsAtCompany; sudden drops indicate manager churn or re-org
- **Privacy & Ethical Considerations**: Managerial effectiveness audits must not scapegoat individual supervisors without contextual review.

---

## 4. Proposed Additional HR Data (External / Enterprise Enrichments)
While the IBM dataset provides 35 useful baseline attributes, an enterprise-grade retention analytics program requires additional data points not present in this static snapshot:

1. **Longitudinal Timestamped Dates**:
   - Exact hire date, transfer dates, promotion dates, and departure date.
   - Enables survival analysis, cohort retention curves, and annualized turnover KPIs.
2. **Separation Reason Taxonomy**:
   - Classification into Voluntary Resignation, Involuntary Discharge, Retirement, End of Contract, or Mutual Agreement.
   - Essential because retention interventions only apply to voluntary departures.
3. **Qualitative Exit Interview Feedback**:
   - Primary and secondary self-reported departure reasons, management feedback, and competitor offer details.
4. **Managerial Continuity & Effectiveness**:
   - Manager tenure, manager performance ratings, manager span of control, and manager turnover rate.
5. **Market Compensation Benchmarks**:
   - External market compensation percentile (e.g., Compa-Ratio = Actual Salary / Market Median for Role).
6. **Work Modality & Flexibility**:
   - Remote vs hybrid vs on-site work arrangement flags and flexible working hour arrangements.
7. **Workload & Overtime Quantitative Volume**:
   - Exact overtime hours logged per month rather than a binary Yes/No flag.