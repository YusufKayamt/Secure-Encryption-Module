# Secure Encryption Module

Bilgi Güvenliği dersi kapsamında Python ile geliştirilmiş, nesne yönelimli bir **klasik şifreleme (rastgele yerine koyma / substitution cipher)** aracı.

> ⚠️ Bu proje eğitim amaçlıdır. Yerine koyma şifreleri frekans analiziyle kırılabilir; gerçek verileri korumak için AES gibi modern ve denetlenmiş algoritmalar kullanılmalıdır.

## Ne yapar?

- Harf, rakam, noktalama ve boşluk karakterlerinden oluşan karakter setini rastgele karıştırarak bir şifreleme anahtarı üretir.
- Şifreleme ve çözme için iki ayrı sözlük (hash map) kullanır; her karakter O(1) sürede dönüştürülür.
- Anahtarı Base64 olarak kodlayıp `.key` dosyasında saklar; dosya varsa mevcut anahtarı yükler, yoksa yenisini üretir.

## Öğrenilenler

- Nesne yönelimli tasarım: anahtar üretme, saklama, yükleme ve dönüştürme işlemlerinin tek sınıfta kapsüllenmesi
- Sözlük tabanlı veri yapılarıyla hızlı eşleştirme
- Kodlama (Base64) ile şifreleme arasındaki fark ve klasik şifrelerin zayıflıkları

## Kullanım

```bash
python3 secure_cipher.py
```

## Geliştirici

**Yusuf Mete Kaya** — [LinkedIn](https://www.linkedin.com/in/yusufmetekaya) · [GitHub](https://github.com/YusufKayamt)
