import pandas as pd
from src.clean_data import clean_data
from src.dataVisualization import dataVisualization



#Step4
def load_dataset(path):
    churn=pd.read_csv(path)
    print(churn)
    print("1.We are in Clean data*********************")
    clean_data()
    print(churn)
    print("We are in data visualization")
    dataVisualization()

   
    