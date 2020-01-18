class GecersizDeger(Exception):

    def __init__(self, hata_iletisi):
        self.hata = hata_iletisi

    def __str__(self):
        return self.hata


def Deneme(x):
    if int(x) < 0:
        raise GecersizDeger('Negatif sayı girdiniz.')
    return x
try:
    print(Deneme(-5)) #negatif ve pozitif deneyerek anlaşılabilir.
except:
    print('Hata oluştu')
else:
    print('Hatasız işlendi')
finally:
    print('Ne olursa olsun bunun altındakiler işlenir.')