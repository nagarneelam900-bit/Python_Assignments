from src.load_data import load_dataset
from src.load_into_db import load

path=r"dataset/Automobiles_sales_dataset.xlsx"

sales=load_dataset(path)


load(sales)
