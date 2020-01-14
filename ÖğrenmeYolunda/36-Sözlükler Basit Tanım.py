sozluk={"bald":"kel","car":"araba"} #listelerde zorlanacağımız aramaları sözlük tanımlarında kolayca yapabiliriz.
print(sozluk["car"])
#sozluk = {anahtar1:deger1, anahtar2:deger2 ...} şeklinde tanımlanır ve her anahtar için bir değer vardır.
# bu tip durumlarda kullanımı bellek akzancı ve hız sağlar. Sözlük adı üstünde kelimelerin karşılığı vardır.
sozluk["page"]="sayfa" #bu şekilde sonradan sözlüğe ekleme yapabiliriz. sozluk[anahtar]=deger gibi...
print(sozluk)