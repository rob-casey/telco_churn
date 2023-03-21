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
| tenure      | Number of months the customer has been with the company | Integer |
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
| PaperlessBilling | Whether the customer has paperless billing or not (Yes, No) | String |
| PaymentMethod | The customer's payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic)) | String |
| MonthlyCharges | The amount charged to the customer monthly | Float |
| TotalCharges | The total amount charged to the customer | Float |
| Churn       | Whether the customer churned or not (Yes, No) | String | 

## Planning
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
