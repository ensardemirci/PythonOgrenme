kayıt = open("C:/Users/ensar/PycharmProjects/ÖğrenmeYolunda/BenimDosyalarım/apache.txt","r")
cumle= kayıt.readlines()
d=[]
for i in cumle:
    d.append(i.strip().replace('"',"++").split("++"))
s={}
for i in d:
    if i[1][3:6] in s:
        s[i[1][3:6]]=s[i[1][3:6]]+1
    else:
        s[i[1][3:6]]=1
print("Hangi dosya \n")
for i in sorted(s):
    print(i,"-->",s[i])

print("\n",s)