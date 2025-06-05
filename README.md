## PREDICTING BARRIERS TO FINANCIAL INCLUSION AMONG RURAL YOUTH IN KENYA
![image](https://github.com/user-attachments/assets/2b9cae88-bb05-458e-864d-ff57cb10bb89)


## Overview
The FinAccess 2024 Household Survey reveals a complex financial inclusion landscape in Kenya. While significant progress has been made, disparities persist across counties, rural youth remain disproportionately excluded, and issues related to consumer protection and rising debt stress are of growing concern. This capstone project aims to leverage the FinAccess 2024 dataset to provide data-driven insights that can inform policy and interventions. 
## Objectives
Understand why rural youth (aged 18–35) in Kenya remain largely excluded from financial services, and identify the key demographic, technological, and economic barriers they face
## Dataset 
**Source**: 
- [FinAccess House Household Survey](https://docs.google.com/spreadsheets/d/1kBfKMxkdPoYKvh9-SgLOaMNhBedn411l/edit?usp=sharing&ouid=115471613002921533452&rtpof=true&sd=true)
  
**Provider**:
- KNBS, CBK & FSD Kenya.
  
**Key Features**
- The dataset includes 35 columns, covering:
- Demographics: Age, gender, marital status, education level, household size.
- Employment: Self-employment status, casual/seasonal work.
- Financial Access: Bank/microfinance account usage, mobile money services (MPesa, Airtel Money), SACCO membership.
- Barriers: Economic constraints, lack of ID, geographic access issues, trust in financial institutions.
- Behavioral Insights: Internet access, financial advice sources, savings habits, loan repayment behavior.

**Data Preprocessing**
Steps Performed:
- Data Loading: The dataset was loaded into a pandas DataFrame for analysis.
- Initial Exploration:
 Checked for duplicates (4 duplicates found and removed).
 Summarized statistical properties of numerical features.
- Identified unique values and missing data in each column.
- Handling Missing Values:
  Columns with high missing values (e.g., Economic Barriers, GeographicAccessBarriers) were noted for potential exclusion or imputation.
- Other missing values were retained for further analysis.
- Feature Renaming: Columns were renamed for clarity and consistency (e.g., A18. AGE OF RESPONDENT → RespondentAge).

**Key Findings (Preliminary)**
- Demographics: The average age of respondents is 25.6 years, with a household size of 4.4.
- Employment: 18% are self-employed, while 33% work as casual/seasonal workers.
- Financial Access:
  99.6% use MPesa, while only 8.5% use Airtel Money.
 80.8% possess a national ID, but 19.3% cite lack of ID as a barrier to opening a bank account.
- Internet Access: 59% of respondents have internet access, indicating potential for digital financial services.

**Next Steps**
- Exploratory Data Analysis (EDA):
Visualize distributions of key variables (e.g., age, education, financial access).
Investigate correlations between financial exclusion and other factors.
- Feature Engineering:
Create derived features (e.g., binary flags for financial inclusion).
Handle categorical variables through encoding.
- Model Building:
Train classification models (e.g., logistic regression, random forest) to predict financial exclusion.
Evaluate model performance using accuracy, F1-score, and feature importance.
- Policy Recommendations:
Summarize findings to inform interventions by FSD Kenya and CBK.
- Tools Used
Python Libraries: Pandas, NumPy, Matplotlib, Seaborn.
Environment: Jupyter Notebook (Google Colab).





