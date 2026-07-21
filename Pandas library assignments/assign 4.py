import pandas as pd 
df = pd.read_csv("students.csv")
print("info : \n", df.info())
print("describe : \n", df.describe())
print("shape : \n", df.shape)
print("Data types : \n", df.dtypes)
