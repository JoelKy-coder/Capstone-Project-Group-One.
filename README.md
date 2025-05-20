# PREDICTING BARRIERS TO FINANCIAL INCLUSION AMONG RURAL YOUTH IN KENYA
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
  
**Feature Include**:
- Demographics (age, gender, education).
- Access indicators: use of bank, mobile money, SACCOs.
- Barriers: access to loans, lack of phone, lack of ID.
- Technology: phone ownership, mobile app use.

## DATA PREPARATION
-	Filter for youth aged 18–25
-	Tag respondents as rural or urban (inferred from county)
- Create binary inclusion status: Included vs Excluded
- Encode categorical variables and handle missing values
-	Generate new features e.g. ID ownership, phone ownership, education level


