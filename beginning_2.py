import pandas as pd
# SENARYO-1
data = {
    'Yukseklik_m': [1200, 800, 1500, -999, 1100], # -999 sensör hatası olsun
    'Sicaklik_C': [25, 28, 24, 0, 26],
    'Hiz_ms': [10, 50, 12, 0, 11]
}
df = pd.DataFrame(data)

# 1. Klasik Yöntem (Filtreleme)
# Türkçesi: Yüksekliği 1000'den büyük OLANLARI getir
yuksek_irtifa = df[df['Yukseklik_m'] > 1000]

print("--- Sadece 1000m Üstü ---")
print(yuksek_irtifa)

# 2. Çoklu Sorgu 
# Türkçesi: Yüksekliği 1000'den büyük OLSUN VE (&&) Sıcaklık 25'ten küçük OLSUN
ozel_durum = df[(df['Yukseklik_m'] > 1000) & (df['Sicaklik_C'] < 25)]

print("\n--- 1000m Üstü VE Soğuk Olanlar ---")
print(ozel_durum)

#---------------------------------

import pandas as pd

# SENARYO-2: Uydudaki iki sensörden gelen veriler

data = {
    'Zaman': ['10:00', '10:01', '10:02', '10:03', '10:04'],
    'Sensor_1': [25.0, 25.1, 25.2, 80.0, 25.3],  # 10:03'te 80 derece okumuş (HATA OLABİLİR)
    'Sensor_2': [24.9, 25.0, 25.1, 25.2, 25.4]   # Bu normal görünüyor
}
df = pd.DataFrame(data)

# --- İŞTE KARŞILAŞTIRMA SİHRİ ---

# 1. Yeni bir sütun oluşturup farkı hesaplayalım
# (Matematik işlemi yapar gibi sütunları birbirinden çıkarabilirsin)
df['Fark'] = df['Sensor_1'] - df['Sensor_2']

print("--- Fark Hesaplanmış Tablo ---")
print(df)

# 2. Farkın çok olduğu (Hatalı) anı yakalayalım
# "Farkı 5 dereceden büyük olan satırları getir"
hatali_okuma = df[abs(df['Fark']) > 5] 

print("\n--- Sensörlerin Uyuşmadığı Anlar (ALARM!) ---")
print(hatali_okuma)
