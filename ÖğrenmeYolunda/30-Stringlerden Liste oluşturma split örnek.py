N = "Fizik:90*Matematik:70*Kimya:50" #örnek cümlemiz
n=N.split("*")  #örnek cümlemizi * işaretine göre split ediyoruz yani listelere çeviriyoruz.
print(n)
a=[]
for i in n:  #Fakat bizim istediğimiz ikili şekilde listeler oluşturmak. Bunun içinde listedeli elemanları tek tek : karakterine göre bölerek yeni bir listeye ekliyoruz.
    a.append(i.split(":"))  #Sonuçta istediğimiz şekli elde ediyoruz.
print(a)

