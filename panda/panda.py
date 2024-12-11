import pandas as pd

df = pd.read_csv("Churn_Modelling.csv")

print(df)
x = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
print(y)
