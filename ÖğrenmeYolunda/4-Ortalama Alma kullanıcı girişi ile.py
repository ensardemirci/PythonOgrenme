def ort(x,y,z):     # öncelikle işlevimizi tanımlıyoruz

    return (x+y+z)/3
a = input("ilk sayıyı giriniz: ")   # kullanıcıdan 3 adet sayıyı tek tek girmesini istiyoruz.
b = input("ikinci sayıyı giriniz: ")
c = input("üçüncü sayıyı giriniz: ")
a = float(a) # input string şeklinde aldığı için alınan değerleri float a çeviriyoruz yani ondalık sayılara
b = float(b)
c = float(c)
print("girdiğiniz sayıların ortalaması" , ort(a,b,c)) # en sonunda da işlevimizi çağırıp sonucu print ile yazdırıyoruz.

