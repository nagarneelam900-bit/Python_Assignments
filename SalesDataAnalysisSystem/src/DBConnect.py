import mysql.connector

def getConnect():
    conn=mysql.connector.connect(
        host='localhost',
        port=3306,
        user='NNeelam1',
        password='#Root2026',
        database='Automobile_sales'
    )
    return conn