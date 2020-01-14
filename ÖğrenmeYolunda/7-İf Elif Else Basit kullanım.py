girilen = input("Bir sayı giriniz: ")
if int(girilen)==0:                     #sıfırda bir çift sayı ama biz sıfır yazmasını istedik o yüzden ilk sınamayı ona atadık eğer altta olsaydı elif e geçtiğinde sıfırı devamlı
                                        # çift olarak verecektir.
    print("Girdiğiniz sayı sıfırdır")
elif int(girilen)%2==0:                 #İstediğimiz kadar elif bloku ekleyebiliriz.
    print("Girdiğiniz sayı çift sayıdır")
else:
    print("Girdiğiniz sayı tek sayıdır")


