rehber = open("C:/Users/ensar/PycharmProjects/ÖğrenmeYolunda/BenimDosyalarım/TelefonRehberi.txt","r+")
rehberKontrol=rehber.read() # txtden önceden girilmiş rehberi okuyup değişkene atıyoruz
ad=input("Aramak istediğiniz adı giriniz: ").strip().title()
soyad=input("Aramak istediğiniz soyadı giriniz: ").strip().title()  #Kullanıcıdan girdileri istiyoruz
adSoyad="{0}{1}{2}".format(ad,":",soyad).strip().title()   # gelen girdileri txt formatımıza uygun şekilde birleştiriyoruz. title ile kullanıcı hatalarını yok etmiş oluyoruz
sonuc= adSoyad in rehberKontrol   # açıklayıcı olması için sonuç için ayrı bir değişken atayıp doğruluğunu kontrol edeceğiz
rehberListe=[]
rehberListe=rehberKontrol.split("\n")
rehberListe2=[]     #Burada daha önceden str olan değişkenimizi listeye çeviriyoruz. İstediğimiz yerden ayırması için satır sonu kullanıyoruz
for i in rehberListe:
    rehberListe2.append(i.split(":"))  # Listeyi istediğimiz şekile getiriyoruz. print edip istediğimiz aşamayı görebiliriz.
if sonuc==True:   #daha önceden tanımladığımız sonuc değişkenini burada kullanıyoruz ve şart sağlanıyorsa kodu çalıştırıyor
    for a in rehberListe2:
        birlesim="{0}{1}{2}".format(str(a[0]),":",str(a[1]))    #burada girilen girdileri listeye çevirip ilerde karşılaştırmak için değişkene atıyoruz (birlesim)
        if birlesim==adSoyad:       #yeni bir sınama ile doğruluğunu kontrol ediyoruz
            print(a[0],a[1],"Telefon numarası: ",str(a[2]))    #sonucu bulduysa eğer yazdırıyoruz istenilen telefon numarası geliyor.
else:
    eklemeGirdi=input("Numara rehberde yok (e)klemek ister misiniz ?: ").lower().strip()   #eğer isim soyisim bulunamazsa yeni bir girdi istiyoruz ki yeni numara için
    if eklemeGirdi=="e":
        eklemeNumara=input("Numarayı yazınız: ").strip()   #yeni numarayı değişkene atıyoruz
        rehber.write("\n{0}{1}{2}{3}{4}".format(ad,":",soyad,":",eklemeNumara))  #burada txt dosyasına yeni numarayı yeni satıra ekliyoruz
        print("Numara eklendi: {0}:{1}".format(adSoyad,eklemeNumara))   #ve sonuçta numara eklenirse eklenen numarayı yazıyoruz.

    else:
        print("Sonlandı")   #eğer kullanıcı numara eklemek istemezse buraya geliyoruz
rehber.close() #en son txt kapatıp kaydediyoruz.
