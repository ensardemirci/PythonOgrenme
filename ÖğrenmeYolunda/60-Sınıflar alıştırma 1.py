class Kullanicilar:
    def __init__(self,kullanici_adi=""):
        self.kullanici_adi=kullanici_adi
    def sifre(self):
        F = open('C:/Users/ensar/PycharmProjects/ÖğrenmeYolunda/BenimDosyalarım/passwd.txt')
        for l in F:
            ls = l.strip()
            k = ls.split(":")
            if k[0]==self.kullanici_adi:
             print(int(k[2]), int(k[3]), k[4], k[5], k[6])
    def home(self):
        F = open('C:/Users/ensar/PycharmProjects/ÖğrenmeYolunda/BenimDosyalarım/passwd.txt')
        for l in F:
            ls = l.strip()
            k = ls.split(":")
            if k[0] == self.kullanici_adi:
                print(k[5])
    def gecos(self):
        F = open('C:/Users/ensar/PycharmProjects/ÖğrenmeYolunda/BenimDosyalarım/passwd.txt')
        for l in F:
            ls = l.strip()
            k = ls.split(":")
            if k[0] == self.kullanici_adi:
                print(k[4])
a=Kullanicilar("jdoe")
a.sifre()
a.home()
a.gecos()