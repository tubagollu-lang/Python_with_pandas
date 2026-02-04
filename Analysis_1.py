import pandas as pd

# Meteoroloji İstasyonundan gelen veri (csv dosyası gibi düşün)
# Nem > 85 TEHLİKE, Rüzgar > 40 km/h TEHLİKE
data = {
    'Saat': ['02:10', '02:20', '02:30', '02:40', '02:50'],
    'Nem_Yuzde': [60, 65, 82, 88, 91],  # 02:40'ta sınırı geçmiş!
    'Ruzgar_kmh': [10, 12, 15, 45, 10]   # 02:40'ta fırtına da çıkmış
}
df = pd.DataFrame(data)

# GÖREV: Tehlikeli anları bul
tehlike_ani = df[(df['Nem_Yuzde'] > 85) | (df['Ruzgar_kmh'] > 40)]

print("--- Kubbenin Kapanması Gereken Anlar ---")
print(tehlike_ani)
