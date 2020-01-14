import os
klasor='C:/Program Files/Common Files/System'
print(os.listdir(klasor))
for i in os.listdir(klasor):
    dosya=os.path.join(klasor,i)
    durum=os.stat(dosya)
    if os.path.isdir(dosya):
        print("Klasör",i)
    elif os.path.isfile(dosya):
        print("Dosya",i)