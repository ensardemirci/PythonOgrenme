import os
yol='C:/windows/system32'
dd=[]
klasor=[]
ini=[]
for i in os.listdir(yol):
    dosya=os.path.join(yol,i)
    durum=os.stat(dosya)
    if os.path.isdir(dosya):
        print("{0}/{1} Klasöründeki dosyalara bakılıyor...".format(yol,i))
        klasor.append([i])
    elif os.path.isfile(dosya):
        dd.append([i,os.stat(dosya)[6]])
        if i.endswith(".ini") == True:
            ini.append([i, os.stat(dosya)[6]])
print("Dosya:",dd)
print("Klasör:",klasor)
bb=0
for boyut in dd:
    bb=bb+int(boyut[1])
print("{3}Toplam {0} Dosya {1} Klasör {4}  ini dosyası Vardır. Toplam dosya boyutu {2} Byte'tır.".format(len(dd),len(klasor),bb,"\n",len(ini)))
print(ini)
