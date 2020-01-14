d = "Deneme yaparken çok zorlanmayın"
test= d.find("yap")
print(test)         #kelime aramak için find kullanıyoruz çıktı olarak index numarasını verir.
print("çok" in d)   #in komutu ile var mı yok mu kontrol edebiliriz True yada False çıktısnı alırız.
print(d.find("ensar")) #find ile aranan kelime yoksa çıktı olarak -1 verecektir.


yerlesimYerleri=["Bolu","Yozgat","Manavgat","Çanakkale","Çan","Kırıkkale","İnebolu"]
print(yerlesimYerleri.index("Yozgat"))
for i in yerlesimYerleri:    #Listelerde de aynı şekilde find komutunu kullanabiliriz.
    i=i.lower()
    if i.find("bolu") >-1:
        print(i)

print("inebolu".endswith("bolu")) #endswith ve startswith ile cümlenin başlangıç ve bitişlerini kontrol ederek aramalarımızı genişletebiliriz.
print("inebolu".startswith("in"))

print(d.split()) #split komutu ile cümleleri parçalayabiliriz.
print(d.split("e")) #hangi karakter ile split edeceğimizi yazarsak
print("@".join(["ensardemirci","gmail.com"]))   # Join ile ayrı cümleleri birleştirebiliriz. Yine hangi karakter ile birleştirmek istersek yazabiliriz.
print(d.replace("çok","az")) #replace ile cümle kelime harf değiştirebiliriz. yada cüm boşlukları alt çizgi yapabiliriz.
a= "        Ensar    "
print(a)
print(a.strip()) #strip komutu ile cümleyi soyarak beyaz boşluklardan arındıırırz böylece kullanıcı girdilerinde kullanıcı hatalarını almamış oluruz.
print(a.isnumeric()) #isnumeric sayı mı değil mi diye T F çıktısı verir. Bununla kullanıcı girdilerini kontrol edebiliriz.
