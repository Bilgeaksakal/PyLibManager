kitaplar = []
odunc_kitaplar = []

def kitap_ekle():
    print("Kitap adı, yazar, sayfa sayısı, basım yılı yazılmalı")
    
    kitap_adi = input("Kitap adı: ").strip()
    if not kitap_adi:
        print("Hatalı giriş tekrar deneyiniz.")
        return
    
    yazar = input("Yazar: ").strip()
    if not yazar:
        print("Hatalı giriş tekrar deneyiniz.")
        return
    
    try:
        sayfa_sayisi = int(input("Sayfa sayısı: "))
        if sayfa_sayisi <= 0:
            print("Hatalı giriş tekrar deneyiniz.")
            return
    except ValueError:
        print("Hatalı giriş tekrar deneyiniz.")
        return
    
    try:
        yil = int(input("Basım yılı: "))
        if yil < 0 or yil > 2025:
            print("Hatalı giriş tekrar deneyiniz.")
            return
    except ValueError:
        print("Hatalı giriş tekrar deneyiniz.")
        return
    
    # Aynı kitap kontrolü (büyük/küçük harf duyarsız)
    for kitap in kitaplar:
        if kitap[0].lower() == kitap_adi.lower() and kitap[1].lower() == yazar.lower():
            print("Bu kitap zaten mevcut.")
            return
    
    kitap = [kitap_adi, yazar, sayfa_sayisi, yil]
    kitaplar.append(kitap)
    print("Kitap eklendi.")

def kitap_sil():
    kitap_adi = input("Silinecek kitap adı: ").strip()
    
    for kitap in kitaplar:
        if kitap[0].lower() == kitap_adi.lower():
            kitaplar.remove(kitap)
            print("Kitap silindi.")
            return
    
    print("Kitap bulunamadı.")

def kitaplari_listele():
    if not kitaplar:
        print("Kütüphanede kitap yok.")
        return
    
    print("\n--- Kütüphanedeki Kitaplar ---")
    for i, kitap in enumerate(kitaplar, 1):
        print(f"{i}. Ad: {kitap[0]} | Yazar: {kitap[1]} | Sayfa: {kitap[2]} | Yıl: {kitap[3]}")
    print()

def kitap_odunc_ver():
    kitap_adi = input("Ödünç verilecek kitap adı: ").strip()
    
    for kitap in kitaplar:
        if kitap[0].lower() == kitap_adi.lower():
            kitaplar.remove(kitap)
            odunc_kitaplar.append(kitap)
            print("Kitap ödünç verildi.")
            return
    
    print("Kitap bulunamadı.")

def kitap_odunc_geri_al():
    kitap_adi = input("Geri alınacak kitap adı: ").strip()
    
    for kitap in odunc_kitaplar:
        if kitap[0].lower() == kitap_adi.lower():
            odunc_kitaplar.remove(kitap)
            kitaplar.append(kitap)
            print("Kitap kütüphaneye geri alındı.")
            return
    
    print("Ödünç kitap bulunamadı.")

def odunc_kitaplari_listele():
    if not odunc_kitaplar:
        print("Ödünç verilmiş kitap yok.")
        return
    
    print("\n--- Ödünç Verilmiş Kitaplar ---")
    for i, kitap in enumerate(odunc_kitaplar, 1):
        print(f"{i}. Ad: {kitap[0]} | Yazar: {kitap[1]} | Sayfa: {kitap[2]} | Yıl: {kitap[3]}")
    print()

while True:
    print("\n--- Kütüphane Yönetim Sistemi ---")
    print("1- Kitap Ekle")
    print("2- Kitap Sil")
    print("3- Kitapları Listele")
    print("4- Ödünç Kitap Ver")
    print("5- Ödünç Kitap Geri Al")
    print("6- Ödünç Kitapları Listele")
    print("7- Çıkış")
    
    secim = input("Seçiminiz: ").strip()
    
    match secim:
        case "1":
            kitap_ekle()
        case "2":
            kitap_sil()
        case "3":
            kitaplari_listele()
        case "4":
            kitap_odunc_ver()
        case "5":
            kitap_odunc_geri_al()
        case "6":
            odunc_kitaplari_listele()
        case "7":
            print("Çıkışınız yapılıyor...")
            break
        case _:
            print("Geçersiz seçim")