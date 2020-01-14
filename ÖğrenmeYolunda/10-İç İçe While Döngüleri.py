i=1
while i<6:
    j=1               #Kod çalıştığındada anlaşılavağı gibi önce içeride ki while döngüsü tamamlanıp sonra bir üstteki döngüye devam ediyor.
    while j<6:        #programın çıktısında gayet ne anlaşılıyor ki önce j ler 5 e tamamlanıyor sonra i 1 artıyor sonra tekrar j 5 e kadar geliyor
        print(i,j,i*j*'*')  # böylelikle en dışta ki döngünün karşılaştırması i 5 olunca döngü sonlanıyor.
        j=j+1
    i=i+1