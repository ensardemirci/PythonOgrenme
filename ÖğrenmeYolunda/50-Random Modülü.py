import random
a=random.random()
print(a)
#random modülü ile program her çalıştığında rastgele bir sayı elde edebiliriz. 0-1 arasında rastgele bu şekilde sayı verir.
b=random.randrange(50,68)
print(b)
#Burada ile randrage komutu ile belli aralıkta rastgele sayılar verebiliriz.
c=random.choice(["maça","kupa","sinek","karo"])
print(c)
#herhangibir listeden tüpten cümleden vs. ranstegele seçim yapmak için choice kullanabiliriz.
def zar():
    print(random.randrange(1,7),random.randrange(1,7))
zar()
#Burada da görüldğü gibi tavla zarı atmak için bu işlevi kullanabiliriz.

