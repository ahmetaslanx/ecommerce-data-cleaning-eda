#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
n_rows = 10000

# LIST VE DICT TANIMLAMA
sube_havuzu = ["İstanbul", "Ankara", "İzmir", "Bursa", "İSTANBUL", "istanbul", "Ankara "]
kategori_havuzu = ["Bilgisayar", "Telefon", "Aksesuar", "Beyaz Eşya"]
urun_sozlugu = {
    "Bilgisayar": ["Laptop Pro","Gamer PC","Ofis Bilgisayarı"],
    "Telefon": ["Smart X1","Mega Phone","Eco Mobile"],
    "Aksesuar": ["Kablosuz Mouse","Mekanik Klavye","RGB Kulaklık","27' Monitör"],
    "Beyaz Eşya": ["Robot Süpürge","Filtre Kahve Makinesi"]
}

# RASTGELE VERI URETIM
tarihler = pd.date_range(start="2025-01-01", end="2026-09-01", periods = n_rows)
secilen_subeler = np.random.choice(sube_havuzu, n_rows)
secilen_kategoriler = np.random.choice(kategori_havuzu, n_rows)
secilen_urunler = [np.random.choice(urun_sozlugu[kat]) for kat in secilen_kategoriler]

birim_fiyatlar = np.random.uniform(500, 35000, size = n_rows).round(2)
satis_adedi = np.random.choice([1,2,3,4,5,150], size = n_rows, p=[0.7, 0.15, 0.1, 0.03, 0.01, 0.01])
musteri_puani = np.random.uniform(low = 1.0, high = 5.0, size = n_rows)

# DATAFRAME OLUSTURMA
df_dev = pd.DataFrame({
    "Siparis_ID": range(100000, 100000 + n_rows),
    "Tarih": tarihler,
    "Sube": secilen_subeler,
    "Kategori": secilen_kategoriler,
    "Urun": secilen_urunler,
    "Birim_Fiyat": birim_fiyatlar,
    "Satis_Adedi": satis_adedi,
    "Musteri_Puani": musteri_puani
})
df_dev['Tarih'] = df_dev['Tarih'].dt.floor('s')

# RASTGELE EKSIK VERI (NaN) EKLEME
df_dev.loc[np.random.choice(n_rows, size = 150), "Birim_Fiyat"] = np.nan
df_dev.loc[np.random.choice(n_rows, size = 200), "Musteri_Puani"] = np.nan
df_dev.loc[np.random.choice(n_rows, size = 100), "Sube"] = np.nan

print("Devasa Veri Seti Başarıyla Oluşturuldu !")
print(f"Toplam Satır Sayısı: {df_dev.shape[0]}, Toplam Sütun Sayısı: {df_dev.shape[1]}")
print("\nİlk 5 satır:")
print(df_dev.head())

#--------------------------------------------------------------------------------------------------------------------------------------
# DATA CLEANING

print("Temizlik Öncesi Şubeler:", df_dev["Sube"].unique())

df_dev["Sube"] = df_dev["Sube"].str.strip()
sehir_duzeltme = {
    "istanbul": "İstanbul",
    "İSTANBUL": "İstanbul",
    "İstanbul": "İstanbul",
    "Ankara": "Ankara",
    "ankara": "Ankara",
    "İzmir": "İzmir",
    "izmir": "İzmir",
    "Bursa": "Bursa",
    "bursa": "Bursa"
}

df_dev["Sube"] = df_dev["Sube"].replace(sehir_duzeltme)
print("Kalan Sube NaN Sayısı:", df_dev["Sube"].isna().sum())
print("Kusursuz Şubeler: ",df_dev["Sube"].unique())

# TEMIZLIK ONCESI KAC TANE ANORMAL DEGER VAR ONU GORELIM
anormal_sayisi = (df_dev["Satis_Adedi"] > 10).sum()
print(f"Temizlenecek aykırı satış sayısı: {anormal_sayisi}")
df_dev = df_dev[df_dev["Satis_Adedi"] <= 10]
print(f"Aykırı değerler temizlendi! Kalan toplam satır sayısı: {df_dev.shape[0]}")

# SUBESI OLMAYAN SATISLAR
print(df_dev["Sube"].isna().sum())
df_dev["Musteri_Puani"] = df_dev["Musteri_Puani"].round(2)
print(df_dev.head())

# SUBESI OLMAYAN SATIRLARI SILME VE EKSIK VERILERI DOLDURMA
df_dev = df_dev.dropna(subset=["Sube"])
df_dev["Musteri_Puani"] = df_dev["Musteri_Puani"].fillna(df_dev["Musteri_Puani"].mean())
df_dev["Birim_Fiyat"] = df_dev["Birim_Fiyat"].fillna(df_dev["Birim_Fiyat"].median())

# NaN DEGER KONTROLU
print("\n--- Tüm Sütunlardaki Kalan NaN Sayıları ---")
print(df_dev.isna().sum())
print(f"\nTemizlik Tamamlandı! Nihai Satır Sayısı: {df_dev.shape[0]}")

# SUBELERE GORE CIRO HESAPLAMA
df_dev["Toplam_Tutar"] = df_dev["Birim_Fiyat"] * df_dev["Satis_Adedi"]
sube_ciroları = df_dev.groupby(by="Sube")["Toplam_Tutar"].sum().reset_index()
sube_ciroları = sube_ciroları.sort_values(by="Toplam_Tutar",ascending=False)
sube_ciroları["Toplam_Tutar"] = sube_ciroları["Toplam_Tutar"].round(2)
pd.options.display.float_format = '{:.2f}'.format
print("\n--- Şube Bazlı Toplam Cirolar ---")
print(sube_ciroları)

# KATEGORILERE GORE CIRO HESAPLAMA
kategori_ciroları = df_dev.groupby(by="Kategori")["Toplam_Tutar"].sum().reset_index()
kategori_ciroları = kategori_ciroları.sort_values(by="Toplam_Tutar",ascending=False)
kategori_ciroları["Toplam_Tutar"] = kategori_ciroları["Toplam_Tutar"].round(2)
print("\n--- Kategori Bazlı Ciro Raporu ---")
print(kategori_ciroları)

# SUBELERE GORE ORTALAMA MUSTERI PUANLARI (MEMNUNIYET ANALIZI)
sube_puanlari = df_dev.groupby(by="Sube")["Musteri_Puani"].mean().reset_index()
sube_puanlari = sube_puanlari.sort_values(by="Musteri_Puani",ascending=False)
sube_puanlari["Musteri_Puani"] = sube_puanlari["Musteri_Puani"].round(2)
print("\n--- Şube Bazlı Ortalama Müşteri Puanları ---")
print(sube_puanlari)

# EN COK SATAN URUNLER
urun_satislari = df_dev.groupby(by="Urun")["Satis_Adedi"].sum().reset_index()
urun_satislari = urun_satislari.sort_values(by="Satis_Adedi",ascending=False)
print("\n--- En Çok Satan Ürünler (Adet Bazlı) ---")
print(urun_satislari)

#%%
print(pd.concat([df_dev.head(),df_dev.tail()]))
#%%
