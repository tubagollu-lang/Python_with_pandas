import pandas as pd
data = {
    'Zaman': ['10:00', '10:05', '10:10', '10:15', '10:20'],
    'Sicaklik_C': [22.5, 24.0, 23.5, None, 25.0],  
    'Basinc_Pa': [1013, 1010, 1012, 1011, 1009],
    'Durum': ['Normal', 'Normal', 'Normal', 'Hata', 'Yüksek']}
df = pd.DataFrame(date)
print("--- TÜM TABLO ---")
print(df)
#---------------------------------
# 1. Sadece sütun isimlerini görelim
print(df.columns)

# 2. İstatistiksel Özet (Ortalama, min, max değerleri şak diye verir)
print(df.describe())

# 3. FİLTRELEME: Sadece Sıcaklığın 23'ten büyük olduğu anları getir
yuksek_sicaklik = df[df['Sicaklik_C'] > 23]
print("\n--- 23 Dereceden Sıcak Anlar ---")
print(yuksek_sicaklik)

# 4. Eksik Veriyi Yönetme (NaN olan satırı atalım)
temiz_df = df.dropna()
print("\n--- Eksik Verisi Olmayan Tablo ---")
print(temiz_df)
#-----------------------------------
#Veriyi Excel dosyası olarak kaydediyoruz (Export)
# 'index=False' diyoruz ki Pandas'ın sol tarafa koyduğu 0,1,2 numaralarını Excel'e yazmasın.
df.to_excel('liste.xlsx', index=False)

#Dosyayı sanki maille gelmiş gibi geri okuyoruz (Import)
# Burada 'read_excel' komutu devreye giriyor
df = pd.read_excel('liste.xlsx')

# Veri çok büyükse sadece başını gösterir
print(df.head())  
# Boş veri var mı, sayı mı yazı mı anlamak için
print(df.info())  
# Sadece belli bir sütunu almak
data = df['Zaman']

