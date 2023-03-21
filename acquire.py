import pandas as pd
import numpy as np

from env import host, password, user

def get_connection(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

sql_query = '''
SELECT *
FROM customers
JOIN contract_types
	USING(contract_type_id)
JOIN internet_service_types
	USING(internet_service_type_id)
JOIN payment_types
	USING(payment_type_id);'''

def get_telco_data():
    return pd.read_sql(sql_query, get_connection('telco_churn'))