kayıt = open("C:/Users/ensar/PycharmProjects/ÖğrenmeYolunda/BenimDosyalarım/apache.txt","r")
cumle= kayıt.readlines()
d=[]
for i in cumle:
    d.append(i.strip().replace("[","++").replace("]","++").split("++"))
s={}
for i in d:
    if i[1][12:15] in s:
        s[i[1][12:15]]=s[i[1][12:15]]+1
    else:
        s[i[1][12:15]]=1
print("Hangi saatlerde kaç kere giriş yapıldığı \n")
for i in sorted(s):
    print(i,"-->",s[i])

print("\n",s)