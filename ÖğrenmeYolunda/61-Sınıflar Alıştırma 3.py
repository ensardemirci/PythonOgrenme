class Nokta:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __repr__(self):
        return  "Nokta ({0},{1})".format(self.x,self.y)
    def __eq__(self, other):
        if self.x==other.x and self.y==other.y :
            return True
        else:
            return False
N1=Nokta(3,5)
N2=Nokta(3,5)
print(N1.x)
print(N1.y)
print(N2)
print(N1==N2)