for i in ['5', (5,4), 9, 'm', '6']:
    try:
        print(int(i)*2)

    except TypeError as hata1:
        print('Tip hatası yakalandı: ', hata1.args[0])

    except ValueError as hata2:
        print('Değer hatası yakalandı: ', hata2.args[0])