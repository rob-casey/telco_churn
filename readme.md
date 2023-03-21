# Telco Churn Classification Project
***

## Goals
***
- Find key drivers for Telco Churn
- Walkthrough the construction of a ML classfication Model
- Provide key points, explanations, and takeaways throughout the process

## Data Dictionary
***
| Column Name | Description | Values |
|-------------|-------------|----------|
| customerID  | Unique identifier for the customer | String |
| is_male     | Gender of the customer | {'Yes': 1, 'No': 0} |
| SeniorCitizen | Whether the customer is a senior citizen or not (1, 0) | Integer |
| Partner     | Whether the customer has a partner or not (Yes, No) | String |
| Dependents  | Whether the customer has dependents or not (Yes, No) | String |
| tenure      | Number of months the customer has been with the Telco | Integer |
| PhoneService | Whether the customer has phone service or not (Yes, No) | String |
| MultipleLines | Whether the customer has multiple lines or not (Yes, No, No phone service) | String |
| InternetService | Type of internet service the customer has (DSL, Fiber optic, No) | String |
| OnlineSecurity | Whether the customer has online security or not (Yes, No, No internet service) | String |
| OnlineBackup | Whether the customer has online backup or not (Yes, No, No internet service) | String |
| DeviceProtection | Whether the customer has device protection or not (Yes, No, No internet service) | String |
| TechSupport | Whether the customer has tech support or not (Yes, No, No internet service) | String |
| StreamingTV | Whether the customer has streaming TV or not (Yes, No, No internet service) | String |
| StreamingMovies | Whether the customer has streaming movies or not (Yes, No, No internet service) | String |
| Contract | The contract term of the customer (Month-to-month, One year, Two year) | String |
| PaperlessBilling | Whether the customer has paperless billing or not | {'Yes': 1, 'No': 0} |
| payment_type_id | The customer's payment method | 1, 2, 3, 4 |
| (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic)) | 
| MonthlyCharges | The amount charged to the customer monthly | Float |
| TotalCharges | The total amount charged throughout tenure | Float |
| Churn       | Whether the customer churned or not | {'Yes': 1, 'No': 0} | 

| churn | customer leaving the company | yes or no |
| tenure | how long a customer has had services in months | integer |
| total_charges | total charges over tenure | integer |
| paperless_billing | {'Yes': 1, 'No': 0} |
| payment_type_id | identifer for payment | 1, 2, 3, 4 |
| internet_service_type_id | identifier for internet service | 0, 1, 2 |
| contract_type_id | identifier for contract type | 0, 1, 2 |
| senior_citizen | {'Yes': 1, 'No': 0} |
| device_protection | yes or no (1 or 0)
tech_support: yes or no (1 or 0)
paperless_billing: yes or no (1 or 0)
monthly_charges: what a customer is paying monthly for their services
gender: male or female
is_male: yes or no (1 or 0)
phone_lines: how many phone lines a customer had (0, 1, or 2+)
family: partner + dependents
streaming_services: yes or (no/ no internet) (1 or 0)
online_services: online_backup + online_security
tenure_years: tenure in terms of years (integers)
online_security: yes or (no/ no internet) (1 or 0)
online_backup: yes or (no/ no internet) (1 or 0)
partner: yes or no (1 or 0)
dependents: yes or no (1 or 0)
streaming_tv: yes or (no/ no internet) (1 or 0)
streaming_movies: yes or (no/ no internet) (1 or 0)
multiple_lines: how many phone lines a customer has (0, 1, or 2+)
contract_type: the type of contract a customer has (month-to-month, 1-year, 2-year)
internet_service_type: what type of internet service (None, DSL, or Fiber Optic)
payment_type: what type of method a customer used (mailed check, credit card (automatic), bank transfer (automatic))



## Planning
***
- Acquire
  - Bring in data
- Preparation
  - Handle nulls
  - Encode features
  - Drop columns
  - Add columns
  - Combine columns
- Exploration
  - Visualizations
  - Find drivers of churn
  - Hypothesis Test
  - T-Test, Independent 2 Tail
  - Chi Square Test
- Modeling
  - Evaluation
  - 3 models
- Test
  - Best model
- Conclusion
  - Key takeaways
