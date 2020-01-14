#Burada yeni bir sınıf oluşturmayı görüyoruz.
import math
class Vektor():
    """Bu bir vektör nesnesidir."""
#Sınıfın içerisine işlev tanımlayıp argüman oalrak girilmesi gerekleri tanımlıyoruz. Burada self ifadesi
#işlevin sadece bu nesneye ait olduğunu belirtir ve dışarıdan çağırmak için kullanılır.
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print("Bir vektör nesnesi oluşturuldu.")
        print(x,y)
    def boyu(self):
        boy=(self.x**2+self.y**2)**(0.5)
        print(boy)
    def aci(self):
        aci=math.degrees(math.tanh(self.x/self.y))
        print(aci)
    def tersi(self):
        self.x=-self.x
        self.y=-self.y
        print(self.x,self.y)
    def yazdir(self):
        print("{0}i + {1}j".format(self.x,self.y))
#Sonuçta görüldüğü gibi vektör adında bir class (sınıf) tanımlamış olduk.
a=Vektor(6,8)
print(a.x)
print(a.y)
a.boyu()
a.aci()
a.yazdir()