d = open("C:/Users/ensar/PycharmProjects/ÖğrenmeYolunda/BenimDosyalarım/KitapListesi.txt")
satır1=d.readline().strip()
satır2=d.readline().strip()
satır3=d.readline().strip()
satır4=d.readline().strip()


satır1=satır1.split(":")
satır2=satır2.split(":")
satır3=satır3.split(":")
satır4=satır4.split(":")

kitaplar=[]
kitaplar=[satır1]+[satır2]+[satır3]+[satır4]

kitaplar[0][0]=int(kitaplar[0][0])
kitaplar[0][4]=int(kitaplar[0][4])
kitaplar[1][0]=int(kitaplar[1][0])
kitaplar[1][4]=int(kitaplar[1][4])
kitaplar[2][0]=int(kitaplar[2][0])
kitaplar[2][4]=int(kitaplar[2][4])
kitaplar[3][0]=int(kitaplar[3][0])
kitaplar[3][4]=int(kitaplar[3][4])


for i in kitaplar:
    print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4])