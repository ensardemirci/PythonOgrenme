import time
print(time.time())
#burada Epoch zaman başlangıcı yani 1 Ocak 1970 tarihinden bu yana kaç saniye geçtiğini gösterir.
print(time.localtime())
#Zaman modülü ile zamanı çekebiliriz. localtime ile gösterim bu şekilde olur.
print(time.ctime())
#Bu ise UNIX tipi zaman gösterimi ve bizim için en uygunudur.
import locale
locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254')
#Burada zaman gösteriminin türkçe olması için locale import ettik

print(time.strftime("%d %B %A %Y %H:%M  "))
#Ardından zaman biçimlemeyi kullanarak ki bunların harf değerleri notlarda var istediğimiz şekilde yazdırabiliriz. Önce saat gün vs nasıl istersek.
time.sleep(5)
print("5 saniye bekledik")
#time.sleep ile kodun işletilmesini tam o noktada istediğimiz süre ile bwekletebiliriz. Burada 5 saniye sonra print yazdırdığını görebiliriz.