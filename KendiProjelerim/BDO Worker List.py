import sqlite3


conn = sqlite3.connect('D:/Ensar Belgeleri/PythonOgrenme/KendiProjelerim/db/bdo.db')
cur = conn.cursor()

"""cur.execute(''' CREATE TABLE WorkerList(
worker_no INTEGER PRIMARY KEY AUTOINCREMENT,
city_name VARCHAR(50),
work_place VARCHAR(50),
product VARCHAR(50),
working_count INTEGER,
not_working_count INTEGER,
total_count INTEGER ) ''') """


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
    last = input('Bilgiler doğru ise kaydetmek için E tekrar girmek için H yazınız').strip()
    if last.lower() == 'e':
        conn.commit()
    else:
        addworker()

def showlist():
    list = cur.execute(' SELECT city_name, work_place, product, working_count, not_working_count, total_count FROM WorkerList').fetchall()
    print('''Şehir İsmi \t Çalışma Alanı \t\t Çıkan Ürün \t Çalışan İşçi Sayısı \t Boşta İşçi Sayısı \t Toplam İşçi Sayısı''')
    print('''========== \t ============= \t\t ========== \t =================== \t ================= \t ==================''')
    for row in list:
        print('{0[0]} \t\t {0[1]} \t {0[2]} \t\t\t\t {0[3]} \t\t\t\t\t\t {0[4]} \t\t\t\t\t {0[5]}'.format(row))


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
        print('{0[0]} \t\t {0[1]} \t {0[2]} \t\t\t\t {0[3]} \t\t\t\t\t\t {0[4]} \t\t\t\t\t {0[5]} \t\t\t\t\t {0[6]}'.format(row))

    last = input('Kaydetmek için E basınız.')

    if last.lower() == 'e':
        conn.commit()
    else:

print('Ana Menü')
first = ''
while first.lower() == '' or 'e':
    first = input('\t İşçi [E]kle \t Liste [G]öster \t İşçi [S]il \n --->')
    if first.lower() == 'e':
        addworker()
        conn.close()
    elif first.lower() == 'g':
        showlist()
        conn.close()
        break
    elif first.lower() == 's':
        deleteworker()
        conn.close()
        break

