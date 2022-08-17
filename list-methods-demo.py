
names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

# 1. "Cenk" ismini listenin sonuna ekleyiniz.
names.append('Cenk')
print(names)
# 2. "Sena" değerini listenin başına ekleyiniz.
names.insert(0, 'Sena')
print(names)
# 3. "Deniz" ismini listeden siliniz.
names.remove("Deniz")
print(names)
# 4. "Cenk" isminin indeksi nedir?
index = names.index('Cenk')
print(index)
# 5. "Ali" Listenin bir elemanı mıdır?
result = 'Ali' in  names
print(result)
# 6. Liste elemanlarını ters çevirin.
names.reverse()
print(names)
# 7. Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)
# 8. "years" listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
print(years)
# 9. str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = ['Chervrolet', 'Dacia']
print(str)
# 10. years dizisinin en büyük ve en küçük elemanı nedir?
min = min(years)
max = max(years)
print(min, max)
# 11. years dizisinde kaç tane 1998 değeri vardır?
print(years.count(1998))

# 12. years dizisinin tüm elemanlarını siliniz.
years.clear()
print(years)

# 13. Kullanıcıdan alacağınız 3 tane marka bilgisini bir liste de saklayınız.
a = input('İlk markayı giriniz:')
b = input('İkinci markayı giriniz:')
c = input('Üçüncü markayı giriniz:')
marks = [a, b, c]
print(marks)



