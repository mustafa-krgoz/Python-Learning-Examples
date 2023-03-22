# Girilen bir sayının 0 ile 100 arasında olup olmadığını kontrol ediniz.
 
number = int(input("Bir sayı giriniz:"))
if(number>0 and number<100):
    print("Sayı 0 ile 100 arasındadır.")
else:
    print("Sayı 0 ile 100 arasında değildir.")


# 2. Girilen bir sayının çift sayı olup olmadığını kontrol ediniz.

number = int(input("Bir sayı giriniz:"))

if(number % 2 == 0):
   print("Sayı çiftir.")
else:
    print("Sayı tektir.")

# 3. Email ve parola bilgileri ile giriş kontrolü yapınız.