import sqlite3
conn = sqlite3.connect('D:/Ensar Belgeleri/PythonOgrenme/ÖğrenmeYolunda/sqlite/yazar.db')
cur = conn.cursor()
"""
cur.execute(''' CREATE TABLE yazarlar(
yazar_no INTEGER PRIMARY KEY AUTOINCREMENT,
adi VARCHAR(100) ) ''')

cur.execute(''' CREATE TABLE kitaplar(
kitap_no INTEGER PRIMARY KEY AUTOINCREMENT,
kitap_adi VARCHAR(100),
stok_adedi VARCHAR(20),
kitap_yazari VARCHAR(10)) ''')
"""
db_yazar = cur.execute('SELECT yazar_no,adi FROM yazarlar')

def yazarekle():
    i_adi = input('Yazar isim ve soyisim giriniz: ')
    cur.execute('''INSERT INTO yazarlar (adi) VALUES ('{0}')'''.format(i_adi))
    conn.commit()
def kitapekle():
    i_kitap_adi = input('Kitabın adını giriniz: ')
    i_stok_adedi = int(input('Kitap stok adedini giriniz: '))
    yazarlar = []
    for i in db_yazar.fetchall():
        yazarlar.append(i[1])
        print(i[0],':',i[1])
    yazar_sec = int(input('Yazar Numarası seçiniz: '))
    cur.execute('''INSERT INTO kitaplar (kitap_adi,stok_adedi,kitap_yazari) VALUES ('{0}','{1}','{2}') '''.format(i_kitap_adi, i_stok_adedi, yazarlar[yazar_sec-1]))
    conn.commit()
def arama():
    girdi = input('Aranacak kelimeyi giriniz: ')
    sonuc = cur.execute('''SELECT kitap_adi, kitap_yazari FROM kitaplar WHERE kitap_adi LIKE '%{0}%' OR kitap_yazari LIKE '%{0}%' ORDER BY kitap_adi DESC '''.format(girdi))
    for i in sonuc.fetchall():
        print(i)
def satis():
    print('No \t Kitap Adı \t \t Yazarı \t  Stok')
    print('== \t ======= \t \t ===== \t \t ====')
    kitaplard = cur.execute(''' SELECT kitap_no, kitap_adi, kitap_yazari, stok_adedi FROM kitaplar ''')
    kitaplar = []
    for i in kitaplard:
        kitaplar.append(i)
    for satir in kitaplar:
        print('{0} \t {1} \t\t {2} \t {3}'.format(satir[0],satir[1],satir[2],satir[3]))

    satilacak = int(input('\n Hangi kitap satılacak: '))
    cur.execute('''UPDATE kitaplar SET stok_adedi=stok_adedi-1 WHERE kitap_no='{0}' '''.format(satilacak))
    conn.commit()
    conn.close()

print('Ana Menü: Yapmak istediğiniz işlem nedir ? ')
giris =''
while giris.lower() == '' or 'k':
    giris = input('[Y]azar Girişi \t [K]itap Girişi \t [A]rama \t [S]atış \n')

    if giris.lower() == 'y':
        yazarekle()
        conn.close()
        break
    elif giris.lower() == 'k':
        kitapekle()
    elif giris.lower() == 'a':
        arama()
        conn.close()
        break
    elif giris.lower() == 's':
        satis()
        conn.close()
        break
