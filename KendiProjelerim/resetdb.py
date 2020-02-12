import os, sqlite3, shutil
from datetime import datetime,date



def resetdb():
    last = input('Tüm bilgiler sıfırlanacaktır yedek alınsın mı ? \n [Y]edekle ve Sil \t [S]ıfırla \t [V]azgeç \n ---> ').strip()
    if last.lower() == 's':
        target = 'D:/Ensar Belgeleri/PythonOgrenme/KendiProjelerim/db/bdo.db'
        dest = 'D:/Ensar Belgeleri/PythonOgrenme/KendiProjelerim/db/Backup/'
        shutil.copy(target,'{0}{1}{2}{3}'.format(dest,'bdo',,'.db'))
        open = 'D:/Ensar Belgeleri/PythonOgrenme/KendiProjelerim/db'
        os.chdir(open)
        os.remove('bdo.db')
        print('{0}\ bdo.db dosyası Backup klasörüne yedeklendi ve sıfırlandı.'.format(os.getcwd()))

