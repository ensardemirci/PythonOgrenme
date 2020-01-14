import os
yol='C:/Program Files/Common Files/System'
print(os.listdir(yol))
print(os.stat(yol),"\n")
dd=[]
klasor=[]
for i in os.listdir(yol):
    dosya=os.path.join(yol,i)
    durum=os.stat(dosya)
    if os.path.isdir(dosya):
        klasor.append([i])
    elif os.path.isfile(dosya):
        dd.append([i,os.stat(dosya)[6]])

print("Dosya:",dd)
print("Klasör:",klasor)
bb=0
for boyut in dd:
    bb=bb+int(boyut[1])
print("{3}Toplam {0} Dosya {1} Klasör Vardır. Toplam dosya boyutu {2} Byte'tır.".format(len(dd),len(klasor),bb,"\n"))