from src.connection import getConnection
import pandas as pd

def dataset():
    conn=getConnection()
    cur=conn.cursor()
    sql="select Distinct * from churn_modeling.churn_data"
    cur.execute(sql)
    data=cur.fetchall()
    cur.close()
    names=['RowNumber', 'CustomerId', 'Surname', 'CreditScore', 'Geography',
       'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
       'IsActiveMember', 'EstimatedSalary', 'Exited']
    churn=pd.DataFrame(data,columns=names)
    return churn


