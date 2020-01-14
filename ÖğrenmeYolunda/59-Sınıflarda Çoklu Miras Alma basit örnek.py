class Ebeveyn:
    def annenin_sac_rengi(self):
        return "sarı"
    def babanın_goz_rengi(self):
        return "mavi"
#Buraya kadar bir sınıf tanımladık. Bu nesne miras alınacakları örnek olarak göstermek için tanımlandı.
class Amca:
    def amcanin_sac_tipi(self):
        return "kıvırcık"

class Cocuk(Ebeveyn,Amca): #Bu şekilde cocuk nesnesi artık ebeveyn nesnesinin özelliklerini de içermiş olacak. Miras alma buna deniyor.
    def __init__(self,adi=""):
        self.adi=adi
    def sac_rengi(self):
        print(self.adi,"nin saç rengi muhtemelen",self.annenin_sac_rengi(),"olacaktır")
    def saci(self):
        print("{0} nin saçı {1} renginde ve {2} olabilir.".format(self.adi,self.annenin_sac_rengi(),self.amcanin_sac_tipi()))
Ensar=Cocuk("Ensar") #Değişkeni atayıp çalıştırdığımızda görüldüğü gibi çıktı veriyor.
Ensar.sac_rengi()
Ensar.saci()
#Çoklu miras almada görüldüğü gibib bir kaç nesnenin özelliklerini tek bir nesnede toplayıp onun değişkenlerinide kullanabilir. bu büyük programlarda çok kullanışlı bir özellik olacaktır.