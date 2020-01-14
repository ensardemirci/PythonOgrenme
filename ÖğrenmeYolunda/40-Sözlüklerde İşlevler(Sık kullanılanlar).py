sozluk={"bald":"kel","car":"araba"}
print(sozluk["car"])

sozluk["page"]="sayfa"
print(sozluk)
a=sozluk.keys() # Sözlükteki anahtarları gösterir
print(a)
b=sorted(sozluk.keys()) #anahtarlara göre sıralama yapmak
print(b)
c=sozluk.values() #bu komuttta değerleri gösterir
print(c)
d=sozluk.items() #Sözlüğün elemanları dinamik bir lsiteye dönüştürülür. Dikkat edilirse listenin elemanları birer tüptür.
print(d)
e=sozluk.get("bald","Sözlükte bulunamadı.")
print(e)
f=sozluk.get("window","Sözlükte bulunamadı.") #get işlevi ile sözlükte olan anahtarı daha rahat şekilde alabiliriz. eğer yoksa istediğimiz çıktıyı veridrebiliriz.
print(f)                                    #yani get iki elemandan oluşuyor şekildeki gibi.istenilen anahtar olmadığında hatayı engeller.
g=sozluk.pop("page") # pop işlevi anahtarı silerken değernide döndürür. Yani burada görüldüğü gibi g ye sayfa değerini atamış oluyoruz.
print(sozluk)
print(g)
kopyaSozluk=sozluk.copy() #sözlükleri kopyalamak copy işlevi ile yapılır.
print(kopyaSozluk)
guncelleme={"bald":"dazlak,kel","cat":"kedi"}
sozluk.update(guncelleme)       #update komutu sözlükleri güncellemek için kullanılır. Yeni bir değer atamak veya var olan anahtarın değerini değiştirmek içinde kullanılabilir.
print(sozluk)
