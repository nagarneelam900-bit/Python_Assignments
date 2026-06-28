import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from src.fetch_from_db import dataset
from src.train import get_model

def dataVisualization():
    #churn= pd.read_csv(r"dataset/Churn_Modeling.csv")
    churn=dataset()
    
    st.set_page_config(page_title="Churn Modeling Data Analysis System",layout='wide')
    st.title("Churn Modeling Data Analysis")

    filtered_churn=churn.copy()
    
    #Slicers
    col1,col2,col3,col4,col5,col6=st.columns(6)
    with col1:
            customerId=st.selectbox("Select Customer Id",['All']+list(filtered_churn['CustomerId'].unique()))
            if customerId!='All':
                filtered_churn=filtered_churn[filtered_churn['CustomerId']==customerId]
    with col2:
            tenure=st.selectbox("Select Tenure",['All']+list(filtered_churn['Tenure'].unique()))
            if tenure!='All':
                filtered_churn=filtered_churn[filtered_churn['Tenure']==tenure]
    with col3:
            creditscore=st.selectbox("Select Credit Score",['All']+list(filtered_churn['CreditScore'].unique()))
            if creditscore!='All':
                filtered_churn=filtered_churn[filtered_churn['CreditScore']==creditscore]
    with col4:
            geography=st.selectbox("Select Geography",['All']+list(filtered_churn['Geography'].unique()))
            if geography!='All':
                filtered_churn=filtered_churn[filtered_churn['Geography']==geography]
    with col5:
            balance=st.selectbox("Select Balance",['All']+list(filtered_churn['Balance'].unique()))
            if balance!='All':
                filtered_churn=filtered_churn[filtered_churn['Balance']==balance]
    with col6:
            esalary=st.selectbox("Select EstimatedSalary",['All']+list(filtered_churn['EstimatedSalary'].unique()))
            if esalary!='All':
                filtered_churn=filtered_churn[filtered_churn['EstimatedSalary']==esalary]

    #KPI
    col1,col2,col3,col4,col5,col6=st.columns([1,1.5,1.5,1.5,1.5,1.5])
    with col1:
          st.metric("Total Customers",int(filtered_churn['CustomerId'].sum()))
    with col2:
            st.metric("Total No. of Products",round(float(filtered_churn['NumOfProducts'].sum())))
    with col3:
            st.metric("Total Balance",round(float(filtered_churn['Balance'].sum())))
    with col4:
            st.metric("Total Estimated Salary",round(float(filtered_churn['EstimatedSalary'].sum()))) 
    with col5:
            st.metric("Total CreditScore",round(float(filtered_churn['CreditScore'].sum())))  
    with col6:
            st.metric("Active Members",round(float(filtered_churn['IsActiveMember'].sum())))   

    st.dataframe(filtered_churn,height=400)
        

    #Visualization
    col1,col2=st.columns(2)
    with col1:
            fig,ax=plt.subplots(figsize=(10,6))
            sns.barplot(x='Geography',y='NumOfProducts',data=filtered_churn,ax=ax)
            st.pyplot(fig)
    with col2:
            fig,ax=plt.subplots(figsize=(10,4))
            Tenure_members=filtered_churn.groupby('Tenure')['IsActiveMember'].sum().reset_index()
            sns.lineplot(x='Tenure',y='IsActiveMember',data=Tenure_members,ax=ax)
            st.pyplot(fig)  
    col1,col2=st.columns(2)
    with col1:
            fig=plt.figure(figsize=(3,2))
            colors = ['gold', 'blue', 'green']
            region_CustomerId=filtered_churn.groupby('Geography')['CustomerId'].sum().reset_index()
            plt.pie(region_CustomerId['CustomerId'],labels=region_CustomerId['Geography'],textprops={'fontsize': 3},colors=colors)
            st.pyplot(fig)
    with col2:
            fig,ax=plt.subplots(figsize=(8,4))
            sns.histplot(x='CreditScore' ,data=filtered_churn, kde=True, ax=ax)
            st.pyplot(fig)

    
    labels=get_model(churn)
    st.subheader("Credit Score as per Geography ")
    fig,ax=plt.subplots(figsize=(12,3))
    print("We are almost there")
    ax.scatter(churn['CreditScore'],churn['Geography'],c=labels,cmap='plasma')
    st.pyplot(fig)
    
    