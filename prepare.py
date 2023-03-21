import pandas as pd
import numpy as np
import math

from sklearn.model_selection import train_test_split

from acquire import get_telco_data

# Split on telco data, stratifying churn
# Return train, validate, and test as Dataframe.
def telco_split(telco):
    train_validate, test = train_test_split(telco, test_size=.2, 
                                        random_state=369, 
                                        stratify=telco.churn)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=369, 
                                   stratify=train_validate.churn)
    return train, validate, test


def prep_telco_data(telco):
    #change total_charges column to float type
    telco.total_charges = telco.total_charges.replace(' ', np.nan).astype('float')

    # assuming these are new customers who haven't paid/churned yet
    # I will drop these observations as they only represent 0.16 % of the data, NBD
    telco = telco.dropna()

    #encode churn
    telco['churn'] = telco.churn.map({'No': 0, 'Yes': 1})

    #encode paperless billing 
    telco['paperless_billing'] = telco.paperless_billing.map({'No': 0, 'Yes': 1})

    #encode device_protection
    telco['device_protection'] = telco.device_protection.map({'No internet service': 0, 'No': 0, 'Yes': 1})

    #encode gender
    telco['is_male'] = telco.gender.map({'Female': 0, 'Male': 1})

    #encode multiple_lines
    telco['phone_lines'] = telco.multiple_lines.map({'No phone service': 0, 'No': 1, 'Yes': 2})

    #encode online_security
    telco['online_security'] = telco.online_security.map({'No internet service': 0, 'No': 0, 'Yes': 1})

    #encode online_backup
    telco['online_backup'] = telco.online_backup.map({'No internet service': 0, 'No': 0, 'Yes': 1})

    #encode partner
    telco['partner'] = telco.partner.map({'No': 0, 'Yes': 1})

    #encode dependents
    telco['dependents'] = telco.dependents.map({'No': 0, 'Yes': 1})

    #encode streaming_tv
    telco['streaming_tv'] = telco.streaming_tv.map({'No internet service': 0, 'No': 0, 'Yes': 1})

    #encode streaming_movies
    telco['streaming_movies'] = telco.streaming_movies.map({'No internet service': 0, 'No': 0, 'Yes': 1})

    #encode tech_support
    telco['tech_support'] = telco.tech_support.map({'No internet service': 0, 'No': 0, 'Yes': 1})

    #combine partner + dependents
    telco['family'] = telco.partner + telco.dependents

    #combine streaming_tv + streaming_movies
    telco['streaming_services'] = telco.streaming_tv + telco.streaming_movies

    #combine online_security + online_backup
    telco['online_services'] = telco.online_security + telco.online_backup

    #add tenure_years
    telco['tenure_years'] = telco.tenure.apply(lambda x: math.floor(x/12))

    #change 'None':3 to 0 (internet_service_type_id)
    telco['internet_service_type_id'] = telco.internet_service_type_id.map({3: 0, 1: 1, 2: 2})

    #drop columns
    cols_to_drop = ['gender', \
                    'multiple_lines',\
                    'payment_type', \
                    'internet_service_type', \
                    'phone_service', \
                    'contract_type', \
                    'partner', 'dependents', 'customer_id', \
                    'streaming_tv', 'streaming_movies', \
                    'online_security', \
                    'online_backup']
    telco = telco.drop(columns=cols_to_drop)

    train, validate, test = telco_split(telco)

    return train, validate, test