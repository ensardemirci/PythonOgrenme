import math
class Vektor():
    """Bu bir vektör nesnesidir."""
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def boyu(self):
        boy=(self.x**2+self.y**2)**(0.5)
        return boy
    def aci(self):
        aci=math.degrees(math.tanh(self.x/self.y))
        print(aci)
    def tersi(self):
        self.x=-self.x
        self.y=-self.y
        print(self.x,self.y)
    def yazdir(self):
        print("{0}i + {1}j".format(self.x,self.y))
# add ile toplama işleminin kendi nesnemize göre nasıl yapılacağını belirleyebiliriz. Yanı bu sınıfta toplama işlemi bu şekilde oluyor diyoruz.
#Vektöre toplama işlemine göre kulamızı ekliyoruz.
    def __add__(self, other): #Toplama işleci belirleme
        return Vektor(self.x+other.x,self.y+other.y)
    def __gt__(self, other): #Büyüklük küçüklük işleci belirleme
        if self.boyu()>other.boyu():return True
    def __eq__(self, other):
        if self.boyu() == other.boyu(): return True
A=Vektor(6,8)
B=Vektor(3,4)
C=A+B  #Toplanan vektör burada
print(A>B)
print(A==B)
