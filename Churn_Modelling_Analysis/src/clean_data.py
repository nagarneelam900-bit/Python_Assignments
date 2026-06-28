import pandas as pd
import joblib
import pandas as pd
from src.connection import getConnection

def clean_data():
    churn=pd.read_csv(r"dataset/Churn_Modeling.csv")

    #Removing duplicate data
    churn=churn.drop_duplicates()

    #Removing null values
    churn=churn.dropna()

    #Total Balance
    print("Total Balance")
    print(churn['Balance'].sum())
    print("******************************")

    #Total Salary
    print("Total Salary")
    print(churn['EstimatedSalary'].sum())
    print("********************************")

    #Average Salary
    print("Average Salary")
    print(churn['EstimatedSalary'].mean())
    print("**********************************")

    #Average Credit Score
    print("Average Credit Score")
    print(churn['CreditScore'].mean())
    print("************************************")

    #Region wise Products
    print("Region Wise Products")
    print(churn.groupby('Geography')['NumOfProducts'].sum())
    print("***************************************")

    #Best Customer
    print("Best Customer")
    print(churn.groupby('Surname')['NumOfProducts'].sum().sort_values(ascending=False).head(5))
    print("****************************************")

    #Highest Product Purchase region
    print("Highest Product Purchase region")
    print(churn.groupby('Geography')['NumOfProducts'].sum().idxmax())
    print("*********************************************")

    #Maximum Credit score
    print("Maximum Credit score")
    print(churn.groupby('Surname')['CreditScore'].sum().sort_values(ascending=False).head(3))
    print("**********************************************")

    #Minimum Credit Score
    print("Minimum Credit Score")
    print(churn.groupby('Surname')['CreditScore'].sum().sort_values(ascending=True).head(5))
    print("************************************************")

    #Maximum Active Members
    print("Maximum Active Members")
    print(churn.groupby('Geography')['IsActiveMember'].sum())
    print("***************************************************")
    
    #Saving clean data
    joblib.dump(churn,r"dataset/churn.csv")

    
    print("Hi we are loading data in db")
    
    for i in range(len(churn)):

        conn=getConnection()
        cur=conn.cursor()
        
        val=list(churn.iloc[i].reset_index()[i])
        data=[int(val[0]),int(val[1]),val[2],int(val[3]),val[4],val[5],int(val[6]),int(val[7]),float(val[8]),int(val[9]),int(val[10]),int(val[11]),float(val[12]),int(val[13])]
        sql='insert IGNORE into churn_data value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur.execute(sql,data)

        conn.commit()
        cur.close()
        conn.close()

    print("Data Inserted Successfully")
    
    
    