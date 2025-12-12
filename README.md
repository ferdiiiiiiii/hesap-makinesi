# 🧮 Gelişmiş Hesap Makinesi (Terminal / CLI)

Python ile geliştirilmiş, **doğrudan terminal (komut satırı) üzerinde çalışan** interaktif bir hesaplama aracıdır.

## 🚀 Proje Tanımı

Bu uygulama, kullanıcıların terminal ekranındaki menüyü kullanarak ileri düzey matematiksel işlemleri gerçekleştirmesini sağlar. Kullanıcı etkileşimi tamamen klavye girdileri üzerinden yönetilir.

**Temel İşlevler:**
* **Dört İşlem:** Toplama, Çıkarma, Çarpma ve Bölme.
* **Faktöriyel Hesaplama:** Girilen sayının faktöriyelini bulur.
* **Asal Sayı Kontrolü:** Sayının asal olup olmadığını analiz eder.
* **Ortalama Hesaplama:** Girilen sayı dizisinin ortalamasını alır.
* **Hata Yakalama:** Harf girilmesi veya sıfıra bölme gibi durumlarda program kapanmaz, terminal üzerinden kullanıcıyı uyarır.

## 🛠️ Teknik Detaylar

Bu proje, Python'un komut satırı yeteneklerini ve algoritma mantığını göstermektedir:

- **CLI (Command Line Interface):** Grafik arayüz yerine metin tabanlı menü sistemi kullanılmıştır.
- **Modüler Fonksiyonlar:** Her matematiksel işlem ayrı bir fonksiyon (`def`) olarak yazılmıştır.
- **Döngüsel Menü:** `while True` döngüsü ile kullanıcı çıkış yapana kadar terminal aktif kalır.
- **Veri Girişi & İşleme:** `input()` fonksiyonu ile alınan veriler işlenir ve `print()` ile terminale sonuç basılır.

## 💻 Nasıl Çalıştırılır?

Projeyi indirdikten sonra terminal veya komut istemini (CMD) açın ve şu komutu yazın:

```bash
python advanced_calculator.py
