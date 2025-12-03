import pandas as pd

# Read Excel file
df = pd.read_excel("data/data.xlsx")

df.to_csv("data/data_excel.csv")

# Display first 5 rows (optional)
print(df.head())