ePosta=""
son={}
while True:
    ePosta = input("e mail giriniz(Yazdırmak için x basınız): ")
    if ePosta.lower()=="x":
        break
    ad = input("Adı: ")
    soyad = input("Soyadı: ")
    son[ePosta]={"soyadi":soyad,"adi":ad}
print(son)