import math

def topla(x, y):
    return x + y

def cikar(x, y):
    return x - y

def carp(x, y):
    return x * y

def bol(x, y):
    if y == 0:
        return "Hata: Bir sayı 0'a bölünemez!"
    return x / y

def faktoriyel(n):
    if n < 0:
        return "Hata: Negatif sayıların faktöriyeli hesaplanamaz."
    if n == 0 or n == 1:
        return 1
    sonuc = 1
    for i in range(2, n + 1):
        sonuc *= i
    return sonuc

def asal_kontrol(n):
    if n <= 1:
        return "Asal Değildir"
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return "Asal Değildir"
    return "Asaldır"

def ortalama(liste):
    if not liste:
        return 0
    return sum(liste) / len(liste)


def ana_program():
    print("Hesap Makinesine Hoş Geldiniz!")
    
    while True: 
       
        print("     İŞLEM MENÜSÜ")
        
        print("1: Toplama")
        print("2: Çıkarma")
        print("3: Çarpma")
        print("4: Bölme")
        print("5: Faktöriyel")
        print("6: Asal Kontrol")
        print("7: Ortalama")
        print("8: ÇIKIŞ") 
        

        secim = input("Yapmak istediğiniz işlem (1-8): ")

       
        if secim == '8':
            print("Programdan çıkılıyor... ")
            break 

        
        elif secim in ['1', '2', '3', '4']:
            try:
                s1 = float(input("Birinci sayıyı girin: "))
                s2 = float(input("İkinci sayıyı girin: "))
                
                if secim == '1':
                    print(f"\n>> SONUÇ: {topla(s1, s2)}")
                elif secim == '2':
                    print(f"\n>> SONUÇ: {cikar(s1, s2)}")
                elif secim == '3':
                    print(f"\n>> SONUÇ: {carp(s1, s2)}")
                elif secim == '4':
                    print(f"\n>> SONUÇ: {bol(s1, s2)}")
            except ValueError:
                print("\nHATA: Lütfen sayısal bir değer giriniz!")

        
        elif secim in ['5', '6']:
            try:
                s = int(input("İşlem yapılacak tam sayıyı girin: "))
                
                if secim == '5':
                    print(f"\n>> SONUÇ: {s}! = {faktoriyel(s)}")
                elif secim == '6':
                    print(f"\n>> SONUÇ: {s} sayısı {asal_kontrol(s)}")
            except ValueError:
                print("\nHATA: Lütfen bir tam sayı giriniz!")

        
        elif secim == '7':
            try:
                veri = input("Sayıları aralarında boşluk bırakarak girin (Örn: 10 20 30): ")
                sayi_listesi = [float(x) for x in veri.split()]
                if not sayi_listesi:
                     print("\nUyarı: Hiç sayı girmediniz.")
                else:
                    print(f"\n>> SONUÇ: Ortalama = {ortalama(sayi_listesi)}")
            except ValueError:
                print("\nHATA: Lütfen sayıları doğru formatta giriniz!")

        else:
            print("\nGeçersiz seçim! Lütfen 1 ile 8 arasında bir numara girin.")
        
        

if __name__ == "__main__":
    ana_program()