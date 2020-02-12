import os
import sqlite3


def resetdb():
    last = input('Tüm bilgiler sıfırlanacaktır yedek alınsın mı ? \n [Y]edekle ve Sil \t [S]ıfırla \t [V]azgeç \n ---> ').strip()
    if last.lower() == 's':
        open = 'D:/Ensar Belgeleri/PythonOgrenme/KendiProjelerim/db'
        os.chdir(open)
        os.remove('bdo.db')
        print(os.getcwd())

