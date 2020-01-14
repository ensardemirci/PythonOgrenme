class Otobus:
    def __init__(self,oturak=48):
        self.oturak=oturak
    def yolcu_bindir(self,binen):
        self.binen=binen
        if binen>self.oturak:
            print("Yolcu kapasitesi aşıldı. Boş koltuk sayısı: {0}".format(self.oturak))
        else:
            return self.oturak-binen
    def yolcu_indir(self,inen):
        self.inen=inen
        if inen>self.binen:
            print("Olandan daha fazla yolcu indirilemez. ")
        else:
            return self.binen-inen
    def bos_koltuk(self):
        return self.oturak-self.binen+self.inen
O=Otobus()
O.yolcu_bindir(49)
O.yolcu_indir(12)
print(O.bos_koltuk())
