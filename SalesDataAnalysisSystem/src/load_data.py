#Step 3
import pandas as pd
from src.cleaning import clean_data
from src.dataVisualization import dataVisualization

#Step4
def load_dataset(path):
    sales=pd.read_excel(path,sheet_name="sales_dataset")
    sales= clean_data(sales)
    sales=dataVisualization(sales)
    return sales