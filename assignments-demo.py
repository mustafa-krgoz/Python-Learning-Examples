
from unittest import result


x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6

# 1. Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?
sayi1 = int(input("İlk sayıyı giriniz:"))
sayi2 = int(input("İkinci sayıyı giriniz:"))

carpim = sayi1*sayi2
print('Çarpimin sonucu:' , carpim)
toplam = x + y + z
print('Toplamın sonucu:' ,toplam)
sonuc = (carpim - toplam)
print('Fark:' , sonuc)

# 2. y ' nin x' e kalansız bölümünü hesaplayınız.
b = y // x 
print(b)

# 3. (x,y,z) toplamının mod 3'ü nedir?
result = x + y + z
result %= 3 
print(result)

# 4. y' nin x. kuvvetini hesaplayınız.
result = y**x
print(result)

# 5. x,*y, z = numbers işlemine göre z'nin küpü kaçtır?
x, *y, z = numbers
islem = z*z*z
print("Z'nin küpü:", islem)

# 6. x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır?
x, *y, z = numbers
toplam = y[0] + y[1] + y[2] 
print("Y'nin degerleri toplamı:", toplam)
