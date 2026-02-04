import pandas as pd

# 1. Veri Hazırlığı: Saniyelik veri
data = {
    'Zaman': ['10:00:01', '10:00:02', '10:00:03', '10:00:04'],
    'Sicaklik': [20, 20, 30, 30] 
}
df = pd.DataFrame(data)

# ÖNEMLİ: Pandas'ın zamanı bükebilmesi için "Zaman" sütununu tanıması lazım.
# Şu an o sütunu "yazı" sanıyor, onu "tarih/saat" formatına çeviriyoruz:
df['Zaman'] = pd.to_datetime(df['Zaman'])

# Zaman sütununu "Index" (yani satır başlığı) yapıyoruz.
# Resample sadece index üzerinde çalışır.
df = df.set_index('Zaman')

# --- İŞLEM ANI ---
# '2S' = 2 Saniye demek.
# "Verileri 2 saniyelik paketler halinda grupla ve ortalamasını (mean) al"
ozet = df.resample('2S').mean()

print(ozet)

#------------------------------
