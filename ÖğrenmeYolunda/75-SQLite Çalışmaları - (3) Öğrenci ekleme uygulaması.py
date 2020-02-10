import sqlite3
baglanti = sqlite3.connect('D:/Ensar Belgeleri/PythonOgrenme/ÖğrenmeYolunda/sqlite/ogrenciler.db')
isaretci = baglanti.cursor()
print('Öğrenci verilerini istenen sıra ile giriniz:')

i_ogrenci_no = input('Öğrenci Numarası: ')
i_adi = input('Öğrenci Adı: ')
i_soyadi = input('Öğrenci Soyadı: ')
i_cinsiyeti = input('Öğrenci Cinsiyeti(E/K): ')
i_sinifi = input('Öğrenci Sınıfı: ')
i_telefon_numarasi = input('Telefon Numarası: ')
i_velisi = input('Öğrenci Velisi: ')
i_dogum_yeri = input('Doğum Yeri: ')

isaretci.execute('''INSERT INTO ogrenciler
(ogrenci_no, adi, soyadi, cinsiyeti, sinifi, telefon_numarasi, velisi, dogum_yeri)
VALUES (?,?,?,?,?,?,?,?) ''',(i_ogrenci_no,i_adi,i_soyadi,i_cinsiyeti,i_sinifi,i_telefon_numarasi,i_velisi,i_dogum_yeri))

baglanti.commit()
print('{0} {1} isimli öğrenci başarı ile kaydedildi'.format(i_adi,i_soyadi))
baglanti.close()

