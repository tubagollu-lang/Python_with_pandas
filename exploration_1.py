import pandas as pd

# SENARYO: Kepler Uzay Teleskobu'ndan gelen bir yıldızın parlaklık verisi
# 'Akis (Flux)': Yıldızın parlaklığı demek. Normalde 1.0 (Tam parlaklık) olmalı.
yildiz_verisi = {
    'Saat': ['22:00', '22:10', '22:20', '22:30', '22:40', '22:50', '23:00'],
    'Parlaklik': [1.00, 1.00, 1.00, 0.98, 0.98, 1.00, 1.00] 
}

df_yildiz = pd.DataFrame(yildiz_verisi)

gezegen_gecisi = df_yildiz[df_yildiz['Parlaklik'] < 1.0]

print("--- Olası Gezegen Geçişi Tespit Edildi! ---")
print(gezegen_gecisi)
