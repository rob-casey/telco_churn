# standard ds imports
import pandas as pd
import numpy as np

# import model classifier
from sklearn.ensemble import RandomForestClassifier

# import my modules created for this report
import acquire as a
import prepare as p
import visual_explore as v
import model as m

#import unclean data from Codeup mySQL server
df = a.get_telco_data()

df.drop_duplicates(inplace=True)
df = df[df.total_charges!=' ']
df.total_charges = df.total_charges.astype(float)
df['churn_encoded'] = df.churn.map({'Yes': 1, 'No': 0})
df.drop(columns=['payment_type_id','contract_type', 'churn'], inplace=True)


train, validate, test = p.train_validate_test_split(df, "churn_encoded")

train.head()

customer_id = test.customer_id

drivers = ['churn_encoded', 'paperless_billing', 'monthly_charges', 'contract_type_id', 'tech_support', 'internet_service_type_id']

X_train, y_train, X_validate, y_validate, X_test, y_test = p.prep_for_model(train, validate, test, "churn_encoded", drivers)

# create classifier object
rf = RandomForestClassifier(max_depth=4, random_state=27)

# fit model on training data
rf.fit(X_train, y_train)

# get predictions
predictions = rf.predict(X_test)

#get probabilities
probabilities = rf.predict_proba(X_test)[:,1]

probabilities, predictions

final_csv = pd.DataFrame({'customer_id':customer_id, 
                     'probability_of_churn':probabilities, 
                     'predictions_of_churn':predictions})
final_csv.to_csv('predictions.csv', index=False)
