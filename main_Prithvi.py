import pandas as pd

data = pd.read_csv("Metadata and Protein Data for Module 1.csv")

for column in data.columns:
    print(column)