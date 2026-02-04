import pandas as pd

# SENARYO: 3 farklı test uçuşundan gelen veriler karışık halde
data = {
    'Test_Adi': ['Test_A', 'Test_A', 'Test_B', 'Test_B', 'Test_C', 'Test_C'],
    'Hiz_ms':   [10, 12, 45, 48, 20, 22],
    'Motor_Sicakligi': [40, 42, 85, 90, 50, 55]
}
df = pd.DataFrame(data)

# --- BÜYÜK RESMİ GÖRMEK (GROUPBY) ---

# Soru: Her testin ORTALAMA hız ve sıcaklığı nedir?
ozet_tablo = df.groupby('Test_Adi').mean()

print("--- Testlerin Karnesi (Ortalamalar) ---")
print(ozet_tablo)

# Soru: Her testte görülen EN YÜKSEK (Max) sıcaklık neydi?
max_degerler = df.groupby('Test_Adi').max()

print("\n--- En Yüksek Değerler ---")
print(max_degerler)
