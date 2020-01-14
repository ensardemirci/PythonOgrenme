simgeler=["Karo","Maça","Sinek","Kupa"]
sayilar=[1,2,3,4,5,6,7,8,9,10,"Bacak","Kız","Papaz"]
kagitlar=[]
for simge in simgeler:
    for sayi in sayilar:
        kagitlar.append([simge,sayi])
#Buraya kadar iskambil kağıtlarının oluşturulmasını tamamladık. Çıktıda görüldüğü gibib 52 deste şeklinde görünüyor.
import random
kagitlarKarisik=[]
while True:
    a=random.choice(kagitlar)
    if a not in kagitlarKarisik:
        kagitlarKarisik.append(a)
    elif len(kagitlarKarisik)==52:
        break
#Burada ise kağıtları kagitlarkarisik adından yeni bir listeye her seferinde karışık olacak şekilde ekledik.
oyuncu1=kagitlarKarisik[0:13]
oyuncu2=kagitlarKarisik[13:26]
oyuncu3=kagitlarKarisik[26:39]
oyuncu4=kagitlarKarisik[39:52]
#Ardından karışık olarak eklenen listeden her oyuncuya eşit miktarda kartı bölüştürerek dağıttık.
for yazim in oyuncu1,oyuncu2,oyuncu3,oyuncu4:
    print(yazim)