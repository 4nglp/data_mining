import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

df = pd.read_csv("Titanic.csv")
print(df.shape)
print(df.isnull().sum())
plt.figure()
msno.matrix(df.sample(250))
plt.show()
df = df.dropna(axis=0, how="any")
print(df.shape)
print(df.isnull().sum())
