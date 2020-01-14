qs="adi=mustafa&soyadi=baser&yas=40&ili=yozgat"
qsl=qs.split("&")  # Önce listeye çeviriyoruz.
qsll=[]
qss={}

for i in qsl:
    i=i.split("=")   # İÇindeki elelmanları tekrar bölerek liste içinde liste yapıyoruz.
    qsll.append(i)

for i in qsll:  #Listenin elemanlarını sözlüğe abahtar ve değer olarak ekletiyoruz.
    qss[i[0]]=i[1]
print(qss)
sonucKontrol=qss.get("adi","Bulunamadı")  #Kontrol edersek görürüz ki program istediğimiz gibi çalışıyor.
print(sonucKontrol)

