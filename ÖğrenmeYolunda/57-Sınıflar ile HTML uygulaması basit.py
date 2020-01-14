"""<select name = "renk" >
<option value = "beyaz">Beyaz</option>
<option value = "kirmizi">Kırmızı</option>
<option value = "siyah">Siyah</ option>
</select>"""
#örnek stml seçim kodlarıdır. Açılır pencedere seçim yapmak için kullanılır. Bunu sınıflarda nasıl kullancağımızı görelim.
class Select:
    def __init__(self,adi='',secenekler=None):
        self.adi=adi
        self.secenekler=secenekler
    def __repr__(self,adi='',secenekler=None):
        eleman='<select name ="%s>\n' %self.adi
        for s in self.secenekler:
            eleman=eleman+'<option value ="%s">%s<\option>\n' %(str(s[0]),str(s[1]))
            eleman=eleman+'</select>'
            return eleman
secimKutusu=Select('renk',[(1,'Mavi'),(2,'Sarı')])
print(secimKutusu)
