def cember(r):
    c = 2*3.14*r
    a = 3.14*(r**2)
    return c,a
ce = cember(4)
cevre,alan = cember(4) # cevre = c diyoruz alan = a diyoruz. Sırası ile değişkenlere değerler atanıyor.

print("Dairenizin çevresi: " ,cevre)
print("Dairenizin alanı: " ,alan)

# Burada önemli olan return komutundan sonra sıra ile değişkenlere atanacağını bilmek gerekir. İlk yazdığım ilke ikinci ikinciye üçüncü vs.vs.vs şeklinde.