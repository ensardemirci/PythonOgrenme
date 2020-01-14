F=open('C:/Users/ensar/PycharmProjects/ÖğrenmeYolunda/BenimDosyalarım/passwd.txt')
kullanicilar={}
for l in F:
    ls=l.strip()
    k=ls.split(":")
    kullanicilar[k[0]]=[k[1],int(k[2]),int(k[3]),k[4],k[5],k[6]]
import pprint
pprint.pprint(kullanicilar)