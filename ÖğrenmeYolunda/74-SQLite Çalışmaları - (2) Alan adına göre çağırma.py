import sqlite3
baglanti = sqlite3.connect('D:/Ensar Belgeleri/PythonOgrenme/ÖğrenmeYolunda/sqlite/ogrenciler.db')
### Bu kısımda veriyi satır fabrikasını kullanarak tüp dışında sanki sözlükten veri çeker gibi çekmeyi gördük. Hangi alanı istiyorsanız adıyla çağırdık.
baglanti.row_factory = sqlite3.Row
isaretci = baglanti.cursor()
db = isaretci.execute('SELECT adi,soyadi, telefon_numarasi FROM ogrenciler')
for i in db.fetchall():
    print(i['adi'], i['soyadi'], i['telefon_numarasi'])