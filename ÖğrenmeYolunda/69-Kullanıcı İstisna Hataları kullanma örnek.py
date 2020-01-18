class GecersizDeger(Exception):

    def __init__(self, hata_iletisi):
        self.hata = hata_iletisi

    def __str__(self):
        return self.hata


girdi = input('Pozitif sayı giriniz: ')

if int(girdi) < 0:
    raise GecersizDeger('Negatif sayı girdiniz.')
