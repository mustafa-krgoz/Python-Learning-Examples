# 1. Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumun kontrol ediniz.
# Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

isim = input("İsim giriniz:")
yas = int(input("Yaşınızı giriniz:"))
egitim = input("Eğitim bilgilerinizi giriniz:")

if(yas >= 18 and (egitim == 'üniversite' or egitim == 'lise')):
    print("Ehliyet alabilirsiniz.")
else:
    print("Ehliyet alamazsınız.")

# 2. Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgi-
# sini yazdırın.
# 0-24 => 0
# 25-44 => 1
# 45-54 => 2
# 55-69 => 3
# 70-84 => 4
# 85-100 => 5

exam = int(input("İlk yazılı sınav sonucunu giriniz:"))
exam1 = int(input("İkinci yazılı sınav sonucunu giriniz:"))
sozlu = int(input("Sözlü sınav sonucunu giriniz:"))

ortalama = (exam + exam1 + sozlu) / 3

if(ortalama >= 0 and ortalama <= 24):
    print("Notunuz: 0")
elif(ortalama >= 25 and ortalama <= 44):
    print("Notunuz: 1")
elif(ortalama >= 45 and ortalama <= 54):
    print("Notunuz: 2")   
elif(ortalama >=55 and ortalama <= 69):
    print("Notunuz: 3")
elif(ortalama >=70 and ortalama <= 84):
    print("Notunuz: 4")
elif(ortalama >= 85 and ortalama <= 100):
    print("Notunuz: 5")
else:
    print("Geçersiz not")
    
# 3. Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
# 1. Bakım => 1.yıl
# 2. Bakım => 2.yıl
# 3. Bakım => 3.yıl
# ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
# *** datetime modülünü kullanmanız gerekiyor.
# (simdi)-(2022/8/1) => gün

import datetime

tarih = input("Aracınız hangi tarihte trafiğe çıktı:")
tarih = tarih.split("/")

trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days<=365:
    print("1. servis aralığı")
elif days>365 and days<= 365*2:
    print("2. servis aralığı")
elif days>365*2 and days<= 365*3:
    print("3. servis aralığı")
else:
    print("Hatalı süre girdiniz.")
