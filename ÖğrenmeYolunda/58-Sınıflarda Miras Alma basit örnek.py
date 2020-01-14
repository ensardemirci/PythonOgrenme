class Ebeveyn:
    def annenin_sac_rengi(self):
        return "sarı"
    def babanın_goz_rengi(self):
        return "mavi"
#Buraya kadar bir sınıf tanımladık. Bu nesne miras alınacakları örnek olarak göstermek için tanımlandı.
class Cocuk(Ebeveyn): #Bu şekilde cocuk nesnesi artık ebeveyn nesnesinin özelliklerini de içermiş olacak. Miras alma buna deniyor.
    def __init__(self,adi=""):
        self.adi=adi
    def sac_rengi(self):
        print(self.adi,"nin saç rengi muhtemelen",self.annenin_sac_rengi(),"olacaktır")

Ensar=Cocuk("Ensar") #Değişkeni atayıp çalıştırdığımızda görüldüğü gibi çıktı veriyor.
Ensar.sac_rengi()