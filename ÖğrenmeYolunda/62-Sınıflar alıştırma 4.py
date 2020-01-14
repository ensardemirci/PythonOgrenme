class Nokta:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __repr__(self):
        return  "Nokta ({0},{1})".format(self.x,self.y)
    def __eq__(self, other):
        if self.x==other.x and self.y==other.y:
            return True
        else:
            return False
class Dogru(Nokta):
    """Doğru tanımlandı"""
    def __init__(self,Na=Nokta(),Nb=Nokta()):
        self.Na=Na
        self.Nb=Nb
        if Na==Nb:
            raise ValueError('İki aynı nokta,doğru oluşturulamaz')
    def __repr__(self):
        return "Doğru 1.Nokta ({0},{1}) 2.Nokta ({2},{3})".format(self.Na.x,self.Na.y,self.Nb.x,self.Nb.y)
    def boyu(self):
        return ((self.Nb.x-self.Na.x)**2+(self.Nb.y-self.Na.y)**2)**0.5
    def __gt__(self, other):
        if self.boyu()>other.boyu():
            return True
        else:
            return False
    def __eq__(self, other):
        if self.Na==other.Na and self.Nb==other.Nb or self.Na==other.Nb and self.Nb==other.Na :
            return True
        else:
            return False

N1=Nokta(6,10)
N2=Nokta(12,18)
N3=Nokta(6,8)
N4=Nokta(1,1)
N5=Nokta(6,10)
N6=Nokta(12,18)
D1=Dogru(N1,N2)
D2=Dogru(N3,N4)
D3=Dogru(N5,N6)
D4=Dogru(N6,N5)
print(D1.boyu())
print(D1>D2)
print(D1==D3)
print(D3==D4)
print(D2==D4)