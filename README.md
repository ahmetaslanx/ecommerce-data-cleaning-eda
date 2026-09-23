# 🛒 E-Commerce Data Cleaning & EDA Pipeline

Python ve Pandas kullanarak 10.000 satırlık ham bir e-ticaret veri setini temizleyen, eksik verileri yöneten ve performans raporları çıkaran uçtan uca bir veri analitiği projesidir.

---

## 🚀 Projenin Amacı (Project Overview)
Gerçek dünya verileri her zaman kirlidir: Büyük/küçük harf hataları, eksik veriler (`NaN`) ve aykırı değerler (`outliers`) barındırır. Bu projede, simüle edilmiş bir e-ticaret veri seti üzerinden **veri temizleme (Data Cleaning)** ve **keşifçi veri analizi (EDA)** pratikleri gerçekleştirilmiştir.

## 🛠️ Kullanılan Teknolojiler (Tech Stack)
* **Python**
* **Pandas** (Veri manipülasyonu ve analizi)
* **NumPy** (Simülasyon verisi üretimi ve matematiksel işlemler)

---

## ⚙️ Uygulanan Adımlar (Pipeline Steps)

1. **Data Generation (Veri Üretimi):** `numpy` kullanarak 10.000 satırlık sipariş, şube, kategori, birim fiyat ve müşteri puanı içeren ham veri seti oluşturuldu.
2. **Data Cleaning (Veri Temizleme):**
   * `.str.strip()` ve `.replace()` yardımıyla şube isimlerindeki büyük/küçük harf uyumsuzlukları giderildi.
   * 10 adetten fazla satılan anormal siparişler (`outliers`) veri setinden temizlendi.
   * Şubesi olmayan (`NaN`) satırlar düşürüldü.
3. **Missing Value Imputation (Eksik Veri Doldurma):**
   * *Müşteri Puanları*ndaki eksikler ortalama (`mean`) ile dolduruldu.
   * *Birim Fiyatlar*daki eksikler, çarpık dağılıma karşı güvenli olan medyan (`median`) ile dolduruldu.
4. **EDA & Reporting (Analiz ve Raporlama):**
   * Şube bazlı toplam ciro analizi (`groupby` & `sum`)
   * Kategori bazlı ciro raporu
   * Şubelere göre müşteri memnuniyeti analizi (`mean`)
   * Adet bazlı en çok satan ürünlerin sıralaması

---

## 📊 Örnek Çıktılar (Sample Insights)
* **Zirvedeki Şube:** Toplam ciroda İstanbul şubesi liderliği göğüsledi.
* **Fiyat Stratejisi:** Medyan bazlı imputation sayesinde aşırı pahalı ürünlerin fiyat ortalamasını manipüle etmesi engellendi.

## 💻 Projeyi Çalıştırma (How to Run)
Depoyu klonladıktan sonra terminalde şu komutu çalıştırarak projeyi ayağa kaldırabilirsin:
```bash
python analiz_scripti.py
