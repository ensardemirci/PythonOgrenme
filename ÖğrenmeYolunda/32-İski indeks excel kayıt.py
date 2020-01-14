kayıt = open("C:/Users/ensar/PycharmProjects/ÖğrenmeYolunda/BenimDosyalarım/iski kayıt.csv","w+")
ilkListe=[[342,"Melike Başer",51],
          [624,"Ahmet Arıyan",67],
          [173,"Selim Yıldırım",31],
          [234,"Mustafa Akgün",89],
          [512,"Aybüke Çoban",12]]
guncelListe=[] #[342,"Melike Başer",51],[624,"Ahmet Arıyan",67],[173,"Selim Yıldırım",31],[234,"Mustafa Akgün",89],[512,"Aybüke Çoban",12]
aboneNo=""
guncelEndeks=""
while aboneNo.lower()!="ç":
    aboneNo=input("Abone numarasını giriniz: ")
    if aboneNo.lower()!="ç":
        for i in ilkListe:
            if i[0]==int(aboneNo) and aboneNo.lower()!="ç":
                print("Abone adı soyadı:", i[1])
                guncelEndeks=input("Güncel endeksi giriniz: ")
                t=int(guncelEndeks)-i[2]
                o=1.2*t
                o=float(o)
                guncelListe.append([i[0],i[1],i[2],int(guncelEndeks),t,o])
                break
        else:
            print("Böyle bir abone numarası yok!")
guncelListe.sort()
ilkListe.sort()
print("Ab.No",'\t',"Adı Soyadı",'\t',"İlk",'\t',"Son",'\t',"Tüketim",'\t',"Ödeme(TL)")
birlesim=[]
for i in guncelListe:
    print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4],'\t','\t',i[5])
    birlesim="{0},{1},{2},{3},{4},{5}\n".format(i[0],i[1],i[2],i[3],i[4],i[5])
    kayıt.write(birlesim)
print(birlesim)

kayıt.close()
