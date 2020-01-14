import modulD
a=modulD.adi
print(a)
b=modulD.soyadi
print(b)
c=modulD.renkler
print(c)
#Buraya kadar olan kısımda görüldüğü gibi kendi yazdığımız modülü bu şekilde çağırırsak tek tek içindeki nesnelere böyle ulaşmamız gerekir.
from modulD import *
print(renkler)
#Bu şekilde çağırırsak görüldüğü gibi renkler nesnesi artık değişken olarak atanmış oldu.
renkler=["siyah","beyaz"]
print(renkler)
from modulD import renkler as anarenkler
print(anarenkler)
print(renkler)
#Eğer modül içindeki nesnenin adı başka değişkende var ise örnekte ki gibi modül içindeki nesneyi başkabir isimle çağırabiliriz. Burada modül içinde ki renkleri anarenkler olarak içerdik.
print(dir(modulD))
#Başkası tarafından yazılan modülleri içerdiğimizde nesnelerini öğrenmek için dir komutunu kullanabiliriz.
#Modüllerde importtan sonra değişiklik yaptığınızda tekrardan import etmeniz gerekir  yada reload yapmanız gerekir çünkü hangi hali ile import edilirse o kullanılır.

