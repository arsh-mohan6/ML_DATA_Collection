# I am gathering data from the open dataset of IMDB to create a CSV file for further analysis.
from datasets import load_dataset

import pandas as pd

dataset = load_dataset("imdb")

df = pd.DataFrame(dataset["train"])

df.to_csv("imdb_dataset.csv",index=False)

print("Data Gathering Successfully using Open-DataSet!...........")
print("-"*100)
print(df.head())