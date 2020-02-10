import sqlite3
import shelve
sdb = shelve.open('D:/Ensar Belgeleri/PythonOgrenme/ÖğrenmeYolunda/sqlite/kullanicilar.db')
sdb['melos'] = {'adi':'Melike Başer','parola':'barbi'}
sdb.close()

### Bu da python nesnesini veya veri tiplerini veritabanında saklamak için kullancağımız modüldür.