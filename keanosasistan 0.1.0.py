import time 
import webbrowser 
anahtar = 1
surum = "0.1.0"
print("selam neyi aratmak istersin ")
print("youtube 1      \ngoogle search 2       \nsurum= 3\n")
anahtar = 1
while anahtar == 1:
    soru = input("(Çıkmak için q)\n=======>")

    if soru == "q":
        print("çıkılıyor...")
        anahtar = 0
    elif soru == "1":
        arama = input("youtubede ne aratmak istersin\n=======>")
        webbrowser.open("https://www.youtube.com/results?search_query=" + arama)
    elif soru == "2": 
        arama2 = input("googlede ne aratmak istersin\n=======>")
        webbrowser.open("https://www.google.com/search?q=" + arama2)
    elif soru == "3":
        print(surum)
    else:
        print("hatalı giriş")
        time.sleep(3)
        break