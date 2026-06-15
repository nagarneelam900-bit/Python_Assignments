import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
def clean_data(sales):
    for col in sales.select_dtypes(include="str").columns:
        print(col,'\t',sales[col].isnull().sum(),'\t Replaced By:',sales[col].mode()[0])
        sales[col]=sales[col].fillna(sales[col].mode()[0])
    
    for col in sales.select_dtypes(include="object").columns:
        print(col,'\t',sales[col].isnull().sum(),'\t Replaced By:',sales[col].mode()[0])
        sales[col]=sales[col].fillna(sales[col].mode()[0])
    
    
    sales['ORDERDATE']=pd.to_datetime(sales['ORDERDATE']).dt.date
  
    print(sales.head(2))
    
    return sales


        
    
        
