d = open("C:/Users/ensar/PycharmProjects/ÖğrenmeYolunda/BenimDosyalarım/Deneme1.txt")
print(d.readline())
print(d.readline())
print(d.readline()) #Her readline yazışta dosyadaki satırı sırayla okur
d.seek(0)
print(d.read())  #Dosyayı baitan okutmak için seek komutu kullanılır. 0 en baş
d.seek(10)
print(d.read())   #Harf sırasına göre sıfırla göründüğü gibi

d.seek(0)
a=d.read()
print(a)    #Metni değişkenede atayabiliriz.
print("armut")
d.seek(0)
for i in d:
    print(i.strip())

d.close   #close komutu ile açılan ehr dosyayı kapatmayı unutmuyoruz.

