print("Çıkmak için ç yazınız")
while True:
    i = input("Karekök almak için bir sayı giriniz: ")
    if  i=="ç":
        print("Programdan çıktınız")
        break           #Program eğer bu if koşulunu sağlarsa yani ç yazılırsa break oluyor ve program sonlanıp döngüden çıkılıyor.
    if float(i)<0:
        print("Negatif sayı girdiniz")
        continue    #Eğer negatif sayı girilirse bu if bloku çalışıyor ve ekrana negatif yazdıktan sonra Continue komutu Döngünün bundan sonraki kısmını çalıştırmayıp
    k=float(i)**0.5 #döngüyü başa döndürüyor. Döngü çalışmaya devam ediyor. Sonrası zaten normal while döngüsü işliyor.
    print("Karekök : ",k)