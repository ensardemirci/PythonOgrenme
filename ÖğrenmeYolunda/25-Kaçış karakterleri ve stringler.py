print("_"*40)
a = "o kadar uzun bir ders aldı ki \
gereğini yapacaktır"
print(a)                    #ekran yetersiz kaldığında \ ile devam edebiliriz.
print("_"*40)

b= "Bir baktım pencereye \nTık dedi patladı \nBunu görenler \nGözlerine inanamadı"
print(b)                    # \n kaçış karakteri ile çıktıda satırı bitirip alt satıra geçirebiliriz.
print("_"*40)

ilkListe=[[342,"Melike Başer",51],
          [624,"Ahmet Arıyan",67],
          [173,"Selim Yıldırı",31],
          [234,"Mustafa Akgün",89],
          [512,"Aybüke Çoban",12]]
for i in ilkListe:
    print(i[0],'\t',i[1],'\t',i[2])     # \t kaçış karakteri ise tab(sekme) görevi görerek hizalamalarda kullanabiliriz.
print("_" * 40)

dersSaati='8:15'
print("dersim saat %s de başlıyor" %dersSaati)  #aralara virgül koymak yerine cümleler için bu şekilde %s ile yapılabilir
print("_" * 40)

maas=15
print("maaşlar ayın %d gününde yatıyor" %maas) #aralara virgül koymak yerine sayı değerleri için bu şekilde %d ve onlalık sayılarda %f ile yapılabilir
print("pi sayısının değerini %0.2f alınız" %3.141592653589793) #%0.2f 2 değeri virgülden sonra kaç kasamak alınacağını gösteriyor.
print("_" * 40)

print("maaşlar %s ayın %d gününde %d yatıyor" %("kasım",15,3000)) #.oklu şekilde kullanımda parantezle sırayla yazıyoruz.
print("_" * 40)

print("maaşlar {0} ayın {1} gününde {2} yatıyor".format("kasım",15,3000)) #aynı işlemi format komutu ilede yapabiliriz. Önemli olan indis
                                                                          #numaralarında parantez içinde yazan yerlerde ki girdileri denk getirmek






