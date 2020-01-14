musteriler=[]
a=""
print("Çıkmak ve yazdırmak için 'ç' giriniz.")
if a!="ç":
    while a!="ç":
        a=input("Müşteri adı giriniz: ")
        musteriler.append(a)
else:
     print("Çıkış yapıldı ve müşteriler yazdırıldı.")
musteriler.pop()
musteriler.sort()
print(musteriler)