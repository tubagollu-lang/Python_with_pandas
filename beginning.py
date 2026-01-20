import pandas as pd
df = pd.read_csv("veriler.csv")
print(df.head())
print(df.info())
sicak_gunler = df[df['Sicaklik']> 20]
