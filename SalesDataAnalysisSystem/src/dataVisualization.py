import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def dataVisualization(sales):
    #sales = pd.read_excel(r"dataset/Automobiles_sales_dataset.xlsx")
    st.set_page_config(page_title="Automobile Sales Data Analysis System", layout='wide')
    st.title("Automobile Sales Analysis System...")

    filtered_sales=sales.copy()
    print(sales.columns)
    print("=======================")
    print(filtered_sales.columns)
    print("=======================")
    
    print(filtered_sales.head(5))
    col1,col2,col3,col4,col5=st.columns(5)
    try:
        with col1:
            country=st.selectbox("Select Country",['All']+list(filtered_sales['COUNTRY'].unique()))
            if country!='All':
                filtered_sales=filtered_sales[filtered_sales['COUNTRY']==country]
        with col2:
            productLine=st.selectbox("Select Product Line",['All']+list(filtered_sales['PRODUCTLINE'].unique()))
            if productLine!='All':
                filtered_sales=filtered_sales[filtered_sales['PRODUCTLINE']==productLine]
        with col3:
            quantityOrdered=st.selectbox("Select Quantity Ordered",['All']+list(filtered_sales['QUANTITYORDERED'].unique()))
            if quantityOrdered!='All':
             filtered_sales=filtered_sales[filtered_sales['QUANTITYORDERED']==quantityOrdered]
        with col4:
            Sales=st.selectbox("Select Sales",['All']+list(filtered_sales['SALES'].unique()))
            if Sales!='All':
                filtered_sales=filtered_sales[filtered_sales['SALES']==Sales]
        with col5:
            yearid=st.selectbox("Select Year",['All']+list(filtered_sales['YEAR_ID'].unique()))
            if yearid!='All':
                filtered_sales=filtered_sales[filtered_sales['YEAR_ID']==yearid]
        col1,col2,col3,col4,col5,col6=st.columns([1,1.5,1.5,1.5,1.5,1.5])
        with col1:
            st.metric("Total Revenue",round(float(filtered_sales['SALES'].sum())))
        with col2:
            st.metric("Total Profit",round(float(filtered_sales['SALES'].sum())))
        with col3:
            st.metric("Top region",round(float(filtered_sales.groupby('COUNTRY')['SALES'].sum().max())))
        with col4:
            st.metric("Top Product",filtered_sales['PRODUCTLINE'].max())
        with col5:
            st.metric("Monthly Growth",round(float(filtered_sales.groupby('MONTH_ID')['SALES'].sum().max())))
        col1,col2=st.columns(2)
        with col1:
            fig,ax=plt.subplots(figsize=(20,8))
            sns.barplot(x='COUNTRY',y='SALES',data=filtered_sales,ax=ax)
            st.pyplot(fig)
        with col2:
            fig,ax=plt.subplots(figsize=(10,4))
            monthly_sales=filtered_sales.groupby('MONTH_ID')['SALES'].sum().reset_index()
            sns.lineplot(x='SALES',y='MONTH_ID',data=monthly_sales,ax=ax)
            st.pyplot(fig)   
        col1,col2=st.columns(2)
        with col1:
            fig=plt.figure(figsize=(6,4))
            region_sale=filtered_sales.groupby('COUNTRY')['SALES'].sum().reset_index()
            plt.pie(region_sale['SALES'],labels=region_sale['COUNTRY'],textprops={'fontsize': 3})
            st.pyplot(fig)
        with col2:
            fig,ax=plt.subplots(figsize=(10,6))
            sns.histplot(x='PRODUCTLINE' ,data=filtered_sales, kde=True, ax=ax)
            st.pyplot(fig)
    except KeyError as e:
        print("Missing key:", e)
    

    #1. Sales By Region(Country)
   # 

    return sales


       