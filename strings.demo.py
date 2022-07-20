#website = "http://www.sadikturan.com"
#course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
# 2- 'website' içinden www karakterlerini alın.
# 3- 'website' içinden com karakterlerini alın.
# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
    #name,surname, age, job = 'Bora','Yılmaz', 32, 'Mühendis'
# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.  
# 'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'  
# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
# 8- 'abc' ifadesini yan yana 3 defa yazdırın.

import abc
from re import S
from unittest import result


website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1.soru cevap
print(len(course))
# 2.soru cevap
print(website[7:10])
# 3.soru cevap
print(website[-3:])
# 4.soru cevap
print(course[:15])
print(course[-15:])
# 5.soru cevap
print(course[::-1])
# 6.soru cevap
name,surname, age, job = 'Bora','Yılmaz', 32, 'Engieer'
print(f"My name is {name} {surname} I'm {age} years old and I'm an {job}")
# 7.soru cevap 
s = 'Hello World'
s = s[0:6] + "W" + s[-4:]
print(s)
# 8. soru cevap
result = 'abc '*3
print(result)



