ogrenciler=[]
no=0
while True:
    no=no+1
    ad=input("ad giriniz: ")
    if ad=="ç":
        break
    soyad=input("Soyad giriniz:")
    telno=input("Tel No Giriniz: ")
    ogrenci=[no,ad,soyad,telno]
    print(ogrenci)
    ogrenciler.append(ogrenci)
for i in ogrenciler:
    print(i)
    
