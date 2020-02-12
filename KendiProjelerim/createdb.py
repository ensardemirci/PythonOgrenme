import sqlite3

def createtable():
    conn = sqlite3.connect('D:/Ensar Belgeleri/PythonOgrenme/KendiProjelerim/db/bdo.db')
    cur = conn.cursor()
    cur.execute(''' CREATE TABLE WorkerList(
    worker_no INTEGER PRIMARY KEY AUTOINCREMENT,
    city_name VARCHAR(50),
    work_place VARCHAR(50),
    product VARCHAR(50),
    working_count INTEGER,
    not_working_count INTEGER,
    total_count INTEGER ) ''')
