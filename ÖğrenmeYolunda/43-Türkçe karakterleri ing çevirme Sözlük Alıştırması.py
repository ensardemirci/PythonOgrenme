ceviri={"ş":"s","Ş":"S","ğ":"g","Ğ":"G","ı":"i","İ":"I","ü":"u","Ü":"U","ö":"o","Ö":"O","ç":"c","Ç":"C"}
metinDeneme="""Gazetelerde güncel konular hakkında nesnel bir bakış açısıyla yayımlanan yazılar da makale olarak nitelendirilir. 
Bilimsel veya akademik makaleler ise genellikle bu türde yayın yapan dergi veya kitaplarda yayımlanır. 
Bilgisayarın yaygınlaşması ile birlikte İnternet'te her gün çok sayıda bilimsel makale okurla buluşmaktadır. 
Bilimsel makale, tarama yazıları, değerlendirme yazıları veya herhangi bir bilimsel konferansın ve toplantının tutanakları da makale türünde değerlendirilebilecek yazı türleridir."""
print(ceviri)
def cev(metin):
    for i in metin:
        duzeltme=ceviri.get(i)
        if i in ceviri:
            metin=metin.replace(i,duzeltme)
    return metin

print(cev(metinDeneme))
