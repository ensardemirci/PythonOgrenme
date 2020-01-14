ogrenciler= [] #liste tanımlaması yada ogrenciler=["Mehmeh","Ayşe"] şeklinde direk elemanlı olarak tanımlanabilir.
ogrenciler.append("Ensar")   #Listele elemanlar append koduyla ekleniyor
ogrenciler.append("Mehpare")
ogrenciler.append("Sümeyye")
ogrenciler.append("Demirci")
ogrenciler.append("Erkek")
print(ogrenciler[0]) #liste kaçıncı elemanı istiyorsak onun çıktısı
print(ogrenciler) #liste çıktısı tamamı
p=len(ogrenciler) #listede kaç eleman olduğunu verir.(Listenin Uzunluğu)
print(p)
ogrenciler[4]="Kız"  #kaç numaralı elemanı değiştirmek istiyorsak onu bu şekilde değiştiriyoruz.
print(ogrenciler) #Değişimden sonrası liste çıktısı