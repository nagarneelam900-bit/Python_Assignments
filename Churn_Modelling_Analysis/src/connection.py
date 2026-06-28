import mysql.connector

def getConnection():
        conn=mysql.connector.connect(
            host='localhost',
            port=3306,
            user='NNeelam1',
            password='#Root2026',
            database='Churn_Modeling'
        )
        return conn

