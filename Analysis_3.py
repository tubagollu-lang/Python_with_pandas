log_defteri = {
    'Proje_Sahibi': ['ODTÜ', 'İTÜ', 'ODTÜ', 'EGE', 'İTÜ'],
    'Kullanim_Suresi_Saat': [4, 5, 3, 8, 2]
}
df_log = pd.DataFrame(log_defteri)

# Her okulun toplam süresini bul
toplam_sureler = df_log.groupby('Proje_Sahibi').sum()

print("--- Kullanım Raporu ---")
print(toplam_sureler)
