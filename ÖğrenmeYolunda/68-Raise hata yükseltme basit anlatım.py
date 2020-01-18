def Karekok(x):
    if x < 0:
        raise ValueError('Geçersiz Değer: Karekökü alınacak sayı negatif olamaz')
    return x ** 0.5
print(Karekok(5))
print(Karekok(-5))
