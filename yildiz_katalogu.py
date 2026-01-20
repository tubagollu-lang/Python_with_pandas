import pandas as pd
veri = {'Yildiz_Adi': ['Sirius', 'Canopus', 'Arcturus', 'Vega' , 'Rigel'], 'Parlaklik': [1000, 850, 600, 920, 450], 'Uzaklik_IY':[8.6, 310, 37, 25, 860]}
df = pd.DataFrame(veri)
print("--- TÜM YILDIZ KATALOĞU ---")
print(df)
print("\n")
parlak_yildizlar = df[df['Parlaklik'] > 800]
print("--- PARLAK YILDIZLAR ---")
print(parlak_yildizlar)
print("\n")
ortalama_uzaklik = df['Uzaklik_IY'].mean()
print(f"Yıldızların ortalama uzaklığı: {ortalama_uzaklik} Işık Yılı")

parlak_yildizlar.to_excel("rapor.xlsx", index=False)
