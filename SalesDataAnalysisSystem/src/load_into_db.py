
from src.DBConnect import getConnect

def load(sales):
    conn=getConnect()
    cur=conn.cursor()
    for i in range (0,len(sales)):
        data=(int(sales.iloc[i]['ORDERNUMBER']),sales.iloc[i]['ORDERDATE'],sales.iloc[i]['CUSTOMERNAME'],sales.iloc[i]['PRODUCTLINE'],sales.iloc[i]['PRODUCTCODE'],sales.iloc[i]['COUNTRY'],int(sales.iloc[i]['QUANTITYORDERED']),float(sales.iloc[i]['PRICEEACH']),float(sales.iloc[i]['SALES']))
        sql="insert into sales value(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(sql,data)
    conn.commit()
    cur.close()
    conn.close()
print("Data Inserted Successfully")    
        
