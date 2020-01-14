deneme = "otobüsün kalkış saati %s varış saati %s mola süresi %d saattir."%("12:30","14:30",1)
print(deneme)
degerler=("12:30","14:30",1)  # burada bir kaç değeri bir değişkene atıyoruz ve gösterim normal parantez şekliden oluyor. Bunlara Tuple(tüp) diyoruz.
deneme2= "otobüsün kalkış saati %s varış saati %s mola süresi %d saattir."%degerler #atanan değerleri bu şekildede yazabiliriz.
print(deneme2)
#Tüpler listelerle aynı mantıkda görünür fakat tüpler bir ekre tanımlandığı zaman elemanları değiştirilemezdir.
#yani değişmeyecek değerleri tüp oalrak atayıp bellek kazancı sağlayabiliriz.

(kalkıs,varis,mola)=("12:30","14:30",1) #buradada görüldüğü gibi birden fazla değişkeni tek satırda tanımlayabiliriz.
print(kalkıs)
print(varis)
print(mola)
kalkıs,varis,mola="12:30","14:30",1 #aynı tanımlamayı parntezler olmadanda yaparsak tüp gibi ele alınır.
print(mola)
#listelerdeki count ve index işlevleri tüplerde de kullanılır.
print("ALAKASIZ__________________________________________")
def den(*sayilar):  # * işareti ile tüpler bu şekilde kullanıcı girdisine bağlı olarak tanımlanabilir.
    for i in sayilar:
        print(i)
    print(sayilar)  #sayilar aslında bir tüp oldu çıktıda da açıkça gürünüyor
den(5,6,8,9,3,2,4,5,66,555)