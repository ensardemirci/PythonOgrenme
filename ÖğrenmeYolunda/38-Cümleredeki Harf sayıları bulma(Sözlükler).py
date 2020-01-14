cumle= input("Bir cümle giriniz: ")
s={}
for i in cumle:
    if i in s:
        s[i]=s[i]+1
    else:
        s[i]=1
print("Cümledeki harflerin sayısı")
for i in sorted(s):
    print(i,"-->",s[i])
print("\nBoşluk dahil toplam %d çeşit harf vardır" % len(s))
print(s)