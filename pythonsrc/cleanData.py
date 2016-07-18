import pandas as pd
import os

os.chdir("../data")
df = pd.read_csv("titanic_data.csv")

df = df.dropna()

df.to_csv("data.csv",index=False)

