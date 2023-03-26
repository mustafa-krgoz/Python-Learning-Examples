# 1. Girlen bir sayının 1-100 arasında olup olmadığını kontrol ediniz.
from operator import index
from unicodedata import name


sayi = int(input("Bir sayi giriniz:"))
result = (1 < sayi < 100)
print("Girilen sayı 1 ile 100 arasında mı?:" , result)

# 2. Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
sayi1 = int(input("Bir sayi giriniz:"))
result = (sayi1 > 0) and (sayi % 2 == 0)
print("Girilen bir sayı pozitif çift sayı mı?:" , result)

# 3. Email ve parola bilgileri ile giriş kontrolü yapınız.
password = int(input("Parolayı giriniz:"))
email = str(input("Emaili giriniz:"))

sonuc = (password == 1234) and (email == 'mustafa@gmail.com')
print(sonuc)

# 4. Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
sayi1 = int(input("İlk sayıyı giriniz:"))
sayi2 = int(input("İkinci sayıyı giriniz:"))
sayi3 = int(input("Üçüncü sayıyı giriniz:"))

result = (sayi1>sayi2) and (sayi1>sayi3)
print(f"sayi1 en büyüktür: {result}")

result = (sayi2>sayi1) and (sayi2>sayi3)
print(f"sayi2 en büyüktür: {result}")

result = (sayi3>sayi1) and (sayi3>sayi2)
print(f"sayi3 en büyüktür: {result}")

# 5. Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız?
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırılsın.
# a) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
# b) Finalden 70 alındığında ortalamanın önemi olmasın.

vize1 = int(input("İlk vize notunu giriniz:"))
vize2 = int(input("İkinci vize notunnu giriniz:"))
final = int(input("Final notunu giriniz:"))

ortalama = ((vize1 + vize2) / 2) * 0.6 + (final*0.4)
result = (final >= 50) and (ortalama >=50)
sonuc = (ortalama>=50) or (final>=70)

print(f"Ortalama: {ortalama >= 50} ve geçme durumu 1: {result}, geçme durumu 2: {sonuc} ")

# 6. Kişinin ad, kilo ve boy biligilerini alıp kilo indekslerini hesaplayınız.
# Formül: (kilo/boy uzunluğunun karesi)
# Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
# 0-18.4 => Zayıf
# 18.5-24.5 => Normal 
# 25.0-29.9 => Fazla Kilolu
# 30.0-34.9 => Şişman(Obez)

ad = input("İsim giriniz:")
kilo = float(input("Kilo giriniz:"))
boy = float(input("Boy bilgisini giriniz:"))

index = kilo / (boy**2)
zayif = (index >=0 ) and (index <= 18.4)
normal = (index >= 18.5) and (index<= 24.5)
kilolu = (index >= 25.0) and (index<= 29.9)
obez = (index >= 30.0) and (index <= 34.9)

print(f"{ad}'nın kilo indekis {index} ve kilo değerlendirmen zayıf {zayif}")
print(f"{ad}'nın kilo indekis {index} ve kilo değerlendirmen normal {normal}")
print(f"{ad}'nın kilo indekis {index} ve kilo değerlendirmen kilolu {kilolu}")
print(f"{ad}'nın kilo indekis {index} ve kilo değerlendirmen obez {obez}")