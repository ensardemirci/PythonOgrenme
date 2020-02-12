import os,sqlite3,shutil
from datetime import datetime

def deletedb():
    open = 'D:/Ensar Belgeleri/PythonOgrenme/KendiProjelerim/db'
    os.chdir(open)
    os.remove('bdo.db')
    print('{0}\ bdo.db dosyası Backup klasörüne yedeklendi ve sıfırlandı.'.format(os.getcwd()))

def backup():
    dtnow = '{0}'.format(datetime.now()).replace(':','-')
    target = 'D:/Ensar Belgeleri/PythonOgrenme/KendiProjelerim/db/bdo.db'
    dest = 'D:/Ensar Belgeleri/PythonOgrenme/KendiProjelerim/db/Backup/'
    shutil.copy(target, '{0}{1}{2}{3}'.format(dest, 'bdo ', dtnow, '.db'))

def createtable():
    dir = 'D:/Ensar Belgeleri/PythonOgrenme/KendiProjelerim/db/bdo.db'
    conn = sqlite3.connect(dir)
    cur = conn.cursor()
    cur.execute(''' CREATE TABLE WorkerList(
    worker_no INTEGER PRIMARY KEY ,
    city_name VARCHAR(50) NOT NULL ,
    work_place VARCHAR(50) NOT NULL ,
    product VARCHAR(50) NOT NULL ,
    working_count INTEGER NOT NULL ,
    not_working_count INTEGER NOT NULL ,
    total_count INTEGER ) ''')