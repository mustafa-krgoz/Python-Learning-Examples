# 1. Girilen 2 sayıdan hangisi büyüktür ? 
import email


a = int(input("İlk sayiyi giriniz:"))
b = int(input("İkinci sayiyi giriniz:"))

result = (a>b)
print(f'a: {a} b: {b} den büyüktür: {result}') 

# 2. Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
# Eger ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

a = int(input('İlk vize notunu giriniz:'))
b = int(input('İkinci vize notunu giriniz:'))
c = int(input('Final notunu giriniz:'))

ortalama = ((a + b)/2)*0.6 + (c*0.4)
print(f' Not Ortalamanız : {ortalama} ve dersten geçme durumunuz: {ortalama>=50}' )

# 3. Girilen bir sayının tek mi çift mi olduğunu yazdırın.
sayi = int(input("Bir sayi giriniz:"))
sonuc = (sayi%2 == 0)
print(f"Girilen sayinin tek veya cift olma durumu: {sonuc}")

# 4. Girilen bir sayının pozitif, negatif olma durumunu yazdırın.
sayi1 = int(input("Bir sayi giriniz:"))
result = (sayi1>0)
print(f"Girilen bir sayinin pozitif veya negatif olma durumu: {result}")

# 5. Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
# (email = mustafa@gmail.com  parola = 3456789)

password = int(input("Parolayı girniz:"))
email = str(input("E-maili giriniz:"))

control = (password == 3456789) 
check = (email == 'mustafa@gmail.com')
print(f"Parola doğru mu? : {control}    E-mail doğru mu?: {check}")

