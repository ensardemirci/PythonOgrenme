import sqlite3
conn = sqlite3.connect('D:/Ensar Belgeleri/PythonOgrenme/ÖğrenmeYolunda/sqlite/ogrenci.db')
cur = conn.cursor()
"""
cur.execute(''' CREATE TABLE ogrenciler(
kayit_no INTEGER PRIMARY KEY AUTOINCREMENT,
adi VARCHAR(50),
soyadi VARCHAR(50),
ogrenci_no VARCHAR(4),
tel_no VARCHAR(13) ) ''') """


i_adi = input('Öğrenci Adı: ')
i_soyadi = input('Öğrenci Soyadı: ')
i_ogrenci_no = input('Öğrenci Numarası: ')
i_tel_no = input('Telefon Numarası: ')

cur.execute('''INSERT INTO ogrenciler
(adi, soyadi, ogrenci_no, tel_no)
VALUES ("{0}","{1}","{2}","{3}") '''.format(i_adi,i_soyadi,i_ogrenci_no,i_tel_no))

conn.commit()
conn.close()