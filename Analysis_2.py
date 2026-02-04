# Teleskobun Azimuth (Yatay) eksenindeki iki motorun verisi
motor_veri = {
    'Zaman': ['23:00', '23:01', '23:02', '23:03'],
    'Motor_A_Akim': [2.5, 2.6, 2.5, 2.5], # Stabil çalışıyor
    'Motor_B_Akim': [2.5, 2.8, 3.9, 4.2]  # Gittikçe ısınıyor/zorlanıyor!
}
df_motor = pd.DataFrame(motor_veri)

# Farkı bul
df_motor['Fark'] = df_motor['Motor_B_Akim'] - df_motor['Motor_A_Akim']

# Farkın 1 Amperi geçtiği yerleri göster
ariza = df_motor[df_motor['Fark'] > 1.0]

print("--- Motor B'de Zorlanma Tespit Edildi ---")
print(ariza)
# Sonuç: "Motor B, saat 23:02'den itibaren A'dan çok daha fazla güç çekiyor. Dişlilerde sıkışma olabilir, bakıma almalıyız."
