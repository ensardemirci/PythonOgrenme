kayıt = open("C:/Users/ensar/PycharmProjects/ÖğrenmeYolunda/BenimDosyalarım/KelimeSayisi.txt","r")
cumle=kayıt.read()
cumle=cumle.strip().replace("\n"," ").split(" ")
s={}
for i in cumle:
    if i in s:
        s[i]=s[i]+1
    else:
        s[i]=1
print("Kelimelerin sayısı")
for i in sorted(s):
    print(i,"-->",s[i])
print("\nToplam %d farklı kelime vardır" % len(s))
print(s)