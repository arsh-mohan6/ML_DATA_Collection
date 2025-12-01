import os
import pandas as pd
data = {
    "name":["Arsh","Mohan","Nishant","Anannya","Aksahat","Aditya","Ishika","Ishani","Astha"],
        "age":[21,20,19,23,17,14,24,25,29],
        "gender":['M','M','M','F','M','M','F','F','F'],
        "Education":["B-tech","M-tech","MA","MBA","10th","7th","MSC","B-ed","MA"]
        }
df = pd.DataFrame(data)
os.makedirs("data", exist_ok=True)

df.to_csv("data/manual_data.csv",index=False)
print("Saved Data in Manual Sucessfully!")
print(df.head())