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
    def __init__(self,Na=Nokta(),Nb=Nokta()):
        self.Na=Na
        self.Nb=Nb
     #   if Na==Nb:
     #       raise BaseException('İki aynı nokta,doğru oluşturulamaz')

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
class Ucgen(Dogru,Nokta):
    def __init__(self,Da=Dogru(),Db=Dogru(),Dc=Dogru()):
        self.Da=Da
        self.Db=Db
        Dc=Dogru(Da.Na,Db.Nb)
        self.Dc=Dc
        if self.Da == self.Db:
            raise ValueError('Bir üçgenin iki kenarı aynı doğru olamaz')
    def ucuncu_dogru(self):
        return self.Dc
    def alani(self):
        u=(self.Da.boyu()+self.Db.boyu()+self.Dc.boyu())/2
        print(u)
        alan=(u*(u-self.Da.boyu())*(u-self.Db.boyu())*(u-self.Dc.boyu()))**0.5
        return alan

N1=Nokta(6,10)
N2=Nokta(12,18)
N3=Nokta(12,18)
N4=Nokta(6,15)
D1=Dogru(N1,N2)
D2=Dogru(N1,N2)
U1=Ucgen(D1,D2)
print(U1.ucuncu_dogru())
print(U1.alani())