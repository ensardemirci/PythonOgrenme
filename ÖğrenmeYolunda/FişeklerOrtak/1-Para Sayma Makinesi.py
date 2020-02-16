try:
    girdi = input('Sayı giriniz: ')
    mod = input('Kaçlık mod sistemi: ')

    furkan = range(1, int(girdi)+1)
    liste = []
    liste_ic =[]

    for i in furkan:
        liste_ic.append(i)
        if i % int(mod) == 0:
            liste.append(liste_ic)
            liste_ic = []

    for i in liste:
        print(i)
except ValueError:
    print('Sayı giriniz.')


