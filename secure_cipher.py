import random
import string
import base64
import os

class GuvenlikModulu:
    def __init__(self, key_file="gizli_anahtar.key"):
        self.key_file = key_file
        self.karakter_seti = string.ascii_letters + string.digits + string.punctuation + " "
        self.sifreleme_sozlugu = {}
        self.cozme_sozlugu = {}
        
        # Eğer anahtar dosyası varsa yükle, yoksa oluştur
        if os.path.exists(self.key_file):
            self.anahtar_yukle()
        else:
            self.yeni_anahtar_olustur()

    def yeni_anahtar_olustur(self):
        """Yeni bir rastgele harita oluşturur ve kaydeder."""
        orijinal = list(self.karakter_seti)
        karistirilmis = orijinal.copy()
        random.shuffle(karistirilmis)
        
        # Sözlük (Dictionary) yapısı kullanıyoruz - Erişim daha hızlıdır
        self.sifreleme_sozlugu = dict(zip(orijinal, karistirilmis))
        self.cozme_sozlugu = dict(zip(karistirilmis, orijinal))
        
        self.anahtar_kaydet(karistirilmis)
        print("[SİSTEM] Yeni kriptografik anahtar üretildi.")

    def anahtar_kaydet(self, key_list):
        """Anahtarı Base64 ile kodlayarak dosyaya yazar (Daha güvenli görünür)."""
        ham_veri = "".join(key_list)
        # Veriyi base64'e çevirip saklayalım ki dosya açılınca okunamasın
        b64_veri = base64.b64encode(ham_veri.encode()).decode()
        
        with open(self.key_file, "w") as f:
            f.write(b64_veri)

    def anahtar_yukle(self):
        """Base64 kodlu anahtarı dosyadan okur."""
        with open(self.key_file, "r") as f:
            b64_veri = f.read()
        
        ham_veri = base64.b64decode(b64_veri).decode()
        
        orijinal = list(self.karakter_seti)
        karistirilmis = list(ham_veri)
        
        self.sifreleme_sozlugu = dict(zip(orijinal, karistirilmis))
        self.cozme_sozlugu = dict(zip(karistirilmis, orijinal))
        print("[SİSTEM] Mevcut anahtar yüklendi.")

    def encrypt(self, metin):
        sonuc = []
        for harf in metin:
            # Sözlükten direkt getir, yoksa harfin kendisini koy
            sonuc.append(self.sifreleme_sozlugu.get(harf, harf))
        return "".join(sonuc)

    def decrypt(self, sifreli_metin):
        sonuc = []
        for harf in sifreli_metin:
            sonuc.append(self.cozme_sozlugu.get(harf, harf))
        return "".join(sonuc)

# --- Arayüz Kısmı ---
def main():
    app = GuvenlikModulu()
    
    while True:
        print("\n=== GÜVENLİK KONSOLU V2 ===")
        print("1. Mesaj Şifrele")
        print("2. Mesaj Çöz")
        print("3. Anahtarı Sıfırla (Dikkat!)")
        print("4. Çıkış")
        
        secim = input("Komut: ")
        
        if secim == '1':
            txt = input("Metin: ")
            print(f">> ŞİFRELİ: {app.encrypt(txt)}")
        elif secim == '2':
            txt = input("Şifreli Metin: ")
            print(f">> ÇÖZÜLMÜŞ: {app.decrypt(txt)}")
        elif secim == '3':
            onay = input("Eski şifreler çözülemez hale gelecek. Emin misin? (e/h): ")
            if onay.lower() == 'e':
                app.yeni_anahtar_olustur()
        elif secim == '4':
            break

if __name__ == "__main__":
    main()
