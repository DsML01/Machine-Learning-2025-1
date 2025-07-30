import pandas as pd

df = pd.read_csv('diabetes_dataset.csv')

df['Insulin'] = 0
df['SkinThickness'] = 0

df = df.fillna(df.mean(numeric_only=True))

df.to_csv('diabetes_dataset.csv', index=False)