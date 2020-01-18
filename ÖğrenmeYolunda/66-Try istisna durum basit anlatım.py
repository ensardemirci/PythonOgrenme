    import os

    klasor = input('Oluşturmak istediğiniz klasörü yazınız: ')
    try:
        os.mkdir((klasor))
    except WindowsError as hata:
        print('İstediğiniz klasör oluşturulamadı. Sebebi: {0}'.format(hata.args[
                                                                          1]))  # burada args özelliğinin ilk elemanı [0] hata numarasını ikinci elemanı [1] hata tanımını verir.
