import sqlite3
from columnar import columnar
from KendiProjelerim import dboptions

dir = 'D:/Ensar Belgeleri/PythonOgrenme/KendiProjelerim/db/bdo.db'
conn = sqlite3.connect(dir)
cur = conn.cursor()

def mainmenu():
    print('\nAna Menü')
    first = input('\t İşçi [E]kle \t Liste [G]öster \t İşçi [S]il \t Kapat [K]aydet \t [D]atabase \n --->').strip()

    if first.lower() == 'e':
        addworker()
        mainmenu()

    elif first.lower() == 'g':
        showlist()
        mainmenu()

    elif first.lower() == 's':
        deleteworker()
        mainmenu()
    elif first.lower() == 'k':
        conn.close()
    elif first.lower() == 'd':
        conn.close()
        dbmenu()
        mainmenu()

def addworker():
    i_city_name = input('Şehir ismini giriniz: ').strip()
    i_work_place = input('Çalışma alanını giriniz: ').strip()
    i_product = input('Çıkan ürünü giriniz: ').strip()
    i_working_count = int(input('Çalışan işçi sayısını giriniz: ').strip())
    i_not_working_count = int(input('Boşta işçi sayısını giriniz: ').strip())
    i_total_count = i_not_working_count + i_working_count

    cur.execute(''' INSERT INTO WorkerList (city_name, work_place, product, working_count, not_working_count, total_count)
    VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')'''.format(i_city_name, i_work_place, i_product, i_working_count, i_not_working_count, i_total_count))

    print('''
Şehir İsmi= {0}
Çalışma alanı: {1}
Çıkan ürün: {2}
Çalışan işçi sayısı: {3}
Boşta işçi sayısı: {4}
Toplam işçi sayısı: {5}'''.format(i_city_name, i_work_place, i_product, i_working_count, i_not_working_count, i_total_count))
    last = input('Bilgiler doğru ise kaydetmek için E tekrar girmek için H yazınız: \n --->').strip()
    if last.lower() == 'e':
        conn.commit()
    else:
        mainmenu()

def showlist():
    list_u = list(cur.execute(' SELECT * FROM WorkerList').fetchall())
    list_n = []
    for row in list_u:
        list_n.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
    header = [' KAYIT NO ',' ŞEHİR İSMİ ',' ÇALIŞMA ALANI ', ' ÇIKAN ÜRÜN ', ' ÇALIŞAN İŞÇİ SAYISI ', ' BOŞTA İŞÇİ SAYISI ',' TOPLAM İŞÇİ SAYISI ']
    try:
        table = columnar(list_n, header, no_borders=False, terminal_width=500, max_column_width=20, wrap_max=1, justify='c')
        print(table)
    except IndexError:
        print('Liste Boş')

def deleteworker():
    list = cur.execute(' SELECT * FROM WorkerList').fetchall()
    print('''Kayıt No \t Şehir İsmi \t Çalışma Alanı \t\t Çıkan Ürün \t Çalışan İşçi Sayısı \t Boşta İşçi Sayısı \t Toplam İşçi Sayısı''')
    print('''======== \t ========== \t ============= \t\t ========== \t =================== \t ================= \t ==================''')
    for row in list:
        print('\t{0[0]} \t\t {0[1]} \t\t\t {0[2]} \t {0[3]} \t\t\t\t {0[4]} \t\t\t\t\t\t {0[5]} \t\t\t\t\t {0[6]}'.format(row))

    del_no = input('Silmek istediğiniz satırın Kayıt No giriniz: ')

    cur.execute('DELETE FROM WorkerList WHERE worker_no = "{0}" '.format(del_no))

    list_n = cur.execute(' SELECT * FROM WorkerList').fetchall()
    for row in list_n:
        list.append(row)
    print('''Kayıt No \t Şehir İsmi \t Çalışma Alanı \t Çıkan Ürün \t Çalışan İşçi Sayısı \t Boşta İşçi Sayısı \t Toplam İşçi Sayısı''')
    print('''======== \t ========== \t ============= \t ========== \t =================== \t ================= \t ==================''')
    for row in list:
        print('\t{0[0]} \t\t {0[1]} \t\t\t {0[2]} \t {0[3]} \t\t\t\t {0[4]} \t\t\t\t\t\t {0[5]} \t\t\t\t\t {0[6]}'.format(row))

    last = input('Kaydetmek için E basınız.')

    if last.lower() == 'e':
        conn.commit()
    else:
        mainmenu()

def dbmenu():
    last = input('Database Ayarları \n [Y]edekle ve Sil \t [V]azgeç \n ---> ').strip()
    if last.lower() == 'y':
        dboptions.backup()
        dboptions.deletedb()
        dboptions.createtable()
    else:
        mainmenu()

mainmenu()

