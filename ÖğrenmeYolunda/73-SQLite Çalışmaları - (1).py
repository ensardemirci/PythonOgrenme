import sqlite3
baglanti = sqlite3.connect('D:/Ensar Belgeleri/PythonOgrenme/ÖğrenmeYolunda/sqlite/ogrenciler.db')
isaretci = baglanti.cursor()
### Bu kısımda veritabanı dosyasını oluşturuyoruz. Tekrar tekrar oluşturulamayacağı için burada yorum satırı halinde duruyor.
# isaretci.execute('''CREATE TABLE ogrenciler(
# kayit_no INTEGER PRIMARY KEY,
# ogrenci_no INTEGER NOT NULL,
# adi VARCHAR(50),
# soyadi VARCHAR(50),
# cinsiyeti VARCHAR(1),
# sinifi VARCHAR(3),
# telefon_numarasi VARCHAR(12),
# velisi VARCHAR(75),
# dogum_yeri VARCHAR(25)
#                 )''')

### Bu kısımda oluşturduğumuz veritabanına verileri girme işlemi gerçekleştiriliyor.
# s = isaretci.execute('''INSERT INTO ogrenciler
# (ogrenci_no, adi, soyadi, cinsiyeti, sinifi, telefon_numarasi, velisi, dogum_yeri)
# VALUES
# (27, 'Ensar', 'Demirci', 'E', '7A', '5673578', 'Mehmet', 'Rize' )''')

### Bu kısımda girilen veriler bellekten harddiske kaydedilip bağlantıyı koparıyoruz.
# print(s.lastrowid)
# baglanti.commit()
# baglanti.close()

### Girilen verilerin çekilmesi bu şekilde sağlanır.
# db = isaretci.execute('SELECT * FROM ogrenciler') ## Burada ki * karakteri tüm alanların getirilmesi anlamına gelir. adi yazsaydı sadece adlarını getirecekti.
# db.fetchone() ## İlk satırda ki geriyi getirir. Tekrar çalıştırılırsa ikinci üçüncü diye devam eder.
# db.fetcall() ## Tüm satırları getirir.
# db.fetcmany(2) ## 2 satırda ki verileri getirir.