import pandas as pd 
from sqlalchemy import create_engine
from sqlite3 import connect

# Creating Dummy Data
patients = {'patient_id': ['0000', '0001', '0002', '0003'],
            'first_name': ['Lucy', 'Tim', 'Nyla', 'Boot'],
            'last_name': ['Chen', 'Bradford', 'Harper', 'Lee'],
            'date_of_birth': ['1995-04-29', '1993-09-13', '1994-08-03-01', '1987-08-11']}
df1 = pd.DataFrame(patients)

print(df1)

medications = {'medication_id': ['0001', '0002', '0003', '0004'],
            'medication_name': ['Lisinopril', 'Lotensin', 'Humalog', 'Lantus']}
df2 = pd.DataFrame(medications)

print(df2)

patient_medications = {'patient_medication_id': ['1000', '1001', '1002', '1003'],
        'patient_id': ['0000', '0001', '0002', '0003'],
        'medication_id': ['0001', '0002', '0003', '0004'],
        'prescribed_date': ['2023-07-03', '2023-09-27', '2023-08-12', '2023-08-19']}
df3 = pd.DataFrame(patient_medications)

print(df3)

patient_visits = {'patient_visit_number': ['0001', '0002', '0003', '0004'],
        'patient_id': ['0000', '0001', '0002', '0003'],
        'visit_date': ['2022-05-12', '2023-03-14', '2019-10-14', '2023-11-29'],
        'visit_location': ['Las Vegas', 'Austin', 'Minneapolis', 'Denver'],
        'visit_reason': ['Flu', 'COVID', 'Rash', 'Herpes']}
df4 = pd.DataFrame(patient_medications)

print(df4)
