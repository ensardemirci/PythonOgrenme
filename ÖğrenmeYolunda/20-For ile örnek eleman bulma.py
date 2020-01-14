ogr = [[27,"Fatih"],[19,"Dilek"],[56,"Selim"],[16,"Tuğba"],[52,"Mehmet"]]
n = input("İsmini öğrenmek istediğiniz öğrencinin numarasını yazınız: ")
n = int(n)

for i in ogr:
    if n == ogr[ogr.index(i)][0]:
        print(ogr[ogr.index(i)][1])






