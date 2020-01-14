d = open("C:/Users/ensar/PycharmProjects/ÖğrenmeYolunda/BenimDosyalarım/DosyaOlusturma.txt","w")  # burada görüldüğü gibi w write için
ilkListe=[[342,"Melike Başer",51],      # r salt okuma
          [624,"Ahmet Arıyan",67],      # w yazma kipi
          [173,"Selim Yıldırım",31],    # a sonuna ekleme kipi
          [234,"Mustafa Akgün",89],     # b ikili(binary) kipi
          [512,"Aybüke Çoban",12]]      # t salt metin kipi(Ön tanımlı)
for i in ilkListe:                      # + dosya güncelleme kipi ( hem okuma hem yazma)
    for a in i:
        d.write(str(a)+":")
    d.write("\n")
d.close()