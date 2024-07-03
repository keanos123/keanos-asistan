import webbrowser
import os
import pywhatkit as pwk
from colorama import init, Fore, Style

init(autoreset=True)  # colorama için otomatik resetleme

surum = "1.1.0"

# Contacts dictionary to store names and numbers
contacts = {}

# Şifre koruması için
def sifre_koruma():
    if not os.path.exists("sifre.txt"):
        print(Fore.YELLOW + "Uygulamayı ilk kez başlatıyorsunuz. Lütfen bir şifre oluşturun.")
        sifre = input(Fore.YELLOW + "Şifrenizi belirleyin: ")
        with open("sifre.txt", "w") as file:
            file.write(sifre)
        print(Fore.GREEN + "Şifre başarıyla oluşturuldu. Program tekrar başlatılacak.")
        return False
    else:
        with open("sifre.txt", "r") as file:
            kaydedilen_sifre = file.read().strip()
        girilen_sifre = input(Fore.YELLOW + "Lütfen şifrenizi girin: ")
        if girilen_sifre == kaydedilen_sifre:
            print(Fore.GREEN + "Doğru şifre! Uygulamaya hoş geldiniz.")
            return True
        else:
            print(Fore.RED + "Yanlış şifre! Tekrar deneyin.")
            return False

# Şifre korumasını kontrol et
while not sifre_koruma():
    pass  # Şifre doğru girilene kadar döngüyü tekrarla

def menu_goster():
    print(Fore.BLUE + "==============================")
    print(Fore.BLUE + "Merhaba! Ne aramak istersin?")
    print(Fore.GREEN + "1. YouTube'da arama yapmak")
    print("2. Google'da arama yapmak")
    print("3. Program sürümünü görmek")
    print(Fore.YELLOW + "4. Masaüstündeki bir dosyayı açmak")
    print(Fore.YELLOW + "5. Python dosyasını çalıştırmak")
    print(Fore.CYAN + "6. WhatsApp üzerinden mesaj göndermek")
    print(Fore.MAGENTA + "7. Kişi eklemek")
    print(Fore.RED + "q. Çıkmak için")
    print(Fore.BLUE + "==============================")

def rehberi_goster():
    print(Fore.MAGENTA + "==============================")
    print(Fore.MAGENTA + "Rehber")
    for isim, numara in contacts.items():
        print(f"{isim}: {numara}")
    print(Fore.MAGENTA + "==============================")

while True:
    menu_goster()
    soru = input(Fore.YELLOW + "Seçiminizi yapın: ")
    
    if soru == "q":
        print(Fore.RED + "Programdan çıkılıyor...")
        break
    elif soru == "1":
        arama = input(Fore.GREEN + "YouTube'da ne aramak istersin?\n=======> ")
        webbrowser.open(f"https://www.youtube.com/results?search_query={arama}")
    elif soru == "2":
        arama = input(Fore.GREEN + "Google'da ne aramak istersin?\n=======> ")
        webbrowser.open(f"https://www.google.com/search?q={arama}")
    elif soru == "3":
        print(Fore.BLUE + f"Programın sürümü: {surum}")
    elif soru == "4":
        dosya_yolu = input(Fore.YELLOW + "Açmak istediğiniz dosyanın tam yolunu girin: ")
        if os.path.exists(dosya_yolu):
            os.startfile(dosya_yolu)
        else:
            print(Fore.RED + "Belirtilen dosya bulunamadı.")
    elif soru == "5":
        python_dosya = input(Fore.YELLOW + "Çalıştırmak istediğiniz Python dosyasının tam yolunu girin: ")
        if os.path.exists(python_dosya) and python_dosya.endswith(".py"):
            os.system(f"python {python_dosya}")
        else:
            print(Fore.RED + "Belirtilen dosya bulunamadı veya Python dosyası değil.")
    elif soru == "6":
        rehberi_goster()
        isim = input(Fore.MAGENTA + "Kişinin adını girin: ")
        if isim in contacts:
            numara = contacts[isim]
            mesaj = input(Fore.CYAN + "Göndermek istediğiniz mesajı girin: ")
            pwk.sendwhatmsg(numara, mesaj, 15, 55)  # 15:55'te mesaj gönderir
            print(Fore.CYAN + "Mesaj gönderildi!")
        else:
            print(Fore.RED + "Bu isimde bir kişi rehberde bulunamadı.")
    elif soru == "7":
        isim = input(Fore.MAGENTA + "Eklemek istediğiniz kişinin adını girin: ")
        numara = input(Fore.MAGENTA + "Eklemek istediğiniz kişinin WhatsApp numarasını girin (+90xxxxxxxxx formatında): ")
        contacts[isim] = numara
        with open("kişiler.txt", "a") as file:
            file.write(f"{isim}: {numara}\n")
        print(Fore.MAGENTA + f"{isim} kişisi rehbere eklendi.")
    else:
        print(Fore.RED + "Hatalı giriş! Lütfen geçerli bir seçenek girin.")
