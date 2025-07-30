import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('diabetes_dataset.csv')

print("Valores ausentes por coluna:")
print(df.isnull().sum())
print("\n")

print("Estatísticas descritivas:")
print(df.describe())
print("\n")



