import sqlite3
import time
baglanti = sqlite3.connect('D:/Ensar Belgeleri/PythonOgrenme/ÖğrenmeYolunda/sqlite/ogrenciler.db')
isaretci = baglanti.cursor()
### Bu kısımda adı Sümeyye olan öğrenciyi Sümeyye Duha olarak update ediyoruz. Where süzgecini kullanarak
isaretci.execute(''' UPDATE ogrenciler SET adi='Sümeyye Duha' WHERE adi='Sümeyye' ''')

### Bu kısımda sınıfı 9A olan öğrencileri veritabanından siliyoruz.
isaretci.execute(''' DELETE FROM ogrenciler WHERE sinifi='9A' ''')

### Bu kısımda var olan tablomuzun adını değiştiriyoruz sonra tekrar eski adına geri hale getiriyoruz.
isaretci.execute(''' ALTER TABLE ogrenciler RENAME TO okul_ogrencileri ''')
isaretci.execute(''' ALTER TABLE okul_ogrencileri RENAME TO ogrenciler ''')

### Burada veritabanımıza yeni bir alan ekliyoruz. Yorum satırı halinde kalması lazım çünkü aynı alan eklemesi yaparsak hata alırız.
# isaretci.execute(' ALTER TABLE ogrenciler ADD dogum_tarihi FLOAT ')

isaretci.execute('''UPDATE ogrenciler SET dogum_tarihi=%f WHERE adi='Sümeyye Duha' ''' %time.mktime((2021,6,15,0,0,0,0,0,0)))

### Bu ifade ile DATETIME şeklinde veriyi çağırabiliriz.
# isaretci.execute('''Select adi,soyadi,DATETIME(dogum_tarihi,"unixepoch") From ogrenciler Where kayit_no=4 ''')

### Bu kısımda veritabanımıza yeni bir tablo ekliyoruz.
# isaretci.execute('''CREATE TABLE ogretmenler
# (ogr_no INTEGER PRIMARY KEY AUTOINCREMENT,
# adi VARCHAR(50),
# soyadi VARCHAR(50),
# sinifi VARCHAR(3) ) ''')
# baglanti.commit()

baglanti.commit()
baglanti.close()

