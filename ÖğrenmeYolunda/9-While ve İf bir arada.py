girilen= ""
while (girilen !="ç"):
    girilen = input("Bir sayı giriniz. Çıkmak için ç yazınız: ")
    if girilen == "ç":
        print("Çıkmak istediniz, program sonlandı.")
    else:
        girilen = float(girilen)
        print("Girdiğiniz sayının karakökü: " , girilen**0.5)