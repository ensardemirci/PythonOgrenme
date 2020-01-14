girilen = input("1-500 arasında bir sayı giriniz: ")
girilen = int(girilen)
a=1
if 1<girilen<500:
    while girilen>a:
        a=a+1
        if girilen%a==0 and girilen!=a:
            print("Girdiğiniz Sayı Asal Sayı değildir.")
            break
    else:
        print("Girdiğiniz Sayı Asal Sayıdır")
else:
    print("Aralık dışında bir sayı girdiniz.")