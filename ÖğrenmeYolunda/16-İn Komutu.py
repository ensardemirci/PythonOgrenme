komsuIller=["Kırıkkale","Kırşehir","Nevşehir","Kayseri","Sivas","Tokat","Amasya","Çorum"]
print("Yozgata komşu illeri öğrenelim.")
girilen=input("İlk harfi büyük yazınız: ")


#i=0
#while i<len(komsuIller):
#    if komsuIller[i]==girilen:
#        print("Tebrikler doğru il girdiniz")
#        break
#    i=i+1
#else:
#    print("Üzgünüm yanlış il girdiniz")


if girilen in komsuIller:       #Yukarıda ki kodlar yerine sadece in komutu ile daha rahat şekilde istediğimizi yapabiliyoruz.
    print("Tebrikler doğru il girdiniz.")
else:
    print("Yanlış il girdiniz.")