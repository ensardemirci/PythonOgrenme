try:
    print(x) #Try içine çalıştırılacak kod yazıyoruz
except:
    print('Üzgünüm x değişkeni tanımlı değil') # Burada ise kodda hata olduğunda işletilecek kodları yazıyoruz.


yas = input('Yaşınızı giriniz: ')


try:
    yas=int(yas)
    print('Üç yıl sonra {0} yaşında olacaksınız'.format(yas+3))
except:
    print('Sayı değeri girmediniz o yüzden 3 yıl sonra ki yaşınızı söyleyemiyorum')

