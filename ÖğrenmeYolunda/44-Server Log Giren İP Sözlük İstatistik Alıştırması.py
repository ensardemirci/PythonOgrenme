kayıt = open("C:/Users/ensar/PycharmProjects/ÖğrenmeYolunda/BenimDosyalarım/apache.txt","r")
cumle= kayıt.readlines()
d=[]
for i in cumle:
    d.append(i.strip().split(" - - "))
print(d)
s={}
for i in d:
    if i[0] in s:
        s[i[0]]=s[i[0]]+1
    else:
        s[i[0]]=1
print("Giren IP'ler ve sayıları\n")
for i in sorted(s):
    print(i,"-->",s[i])

print("\n",s)
