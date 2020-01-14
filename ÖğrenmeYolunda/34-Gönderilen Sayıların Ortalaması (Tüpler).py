def ort(*sayilar):
    toplam=0
    for i in sayilar:
        toplam=toplam+i
    ortalama=toplam/len(sayilar)
    print(ortalama)
ort(4,6,8,10,12)

