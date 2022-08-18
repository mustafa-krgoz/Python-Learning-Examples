'''
ogrenciler = {
        '120': {
            'ad': 'Ali',
            'soyad': 'Yılmaz',
            'telefon': '532 000 00 01'
        },
        '125': {
            'ad': 'Can',
            'soyad': 'Korkmaz',
            'telefon': '532 000 00 02'
        },
        '128': {
            'ad': 'Volkan',
            'soyad': 'Yükselen',
            'telefon': '532 000 00 03'
        },
    }
    1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
       dictionary içinde saklayınız.
    2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
'''

ogrenciler = {}

name = input("Ogrenci adi: ")
surname = input("Ogrenci soyadi: ")
number = input("Ogrenci no: ")
phone = input("Ogrenci telefon: ")

# ogrenciler[number] = {
#     'ad': name,
#     'soyad': surname,
#     'telefon': phone,
# }

ogrenciler.update({
    number: {
        'Ad': name,
        'Soyad': surname,
        'Telefon': phone,
    }
})



ogrenciler = {}

name = input("Ogrenci adi: ")
surname = input("Ogrenci soyadi: ")
number = input("Ogrenci no: ")
phone = input("Ogrenci telefon: ")


ogrenciler.update({
    number: {
        'Ad': name,
        'Soyad': surname,
        'Telefon': phone,
    }
})



ogrenciler = {}

name = input("Ogrenci adi: ")
surname = input("Ogrenci soyadi: ")
number = input("Ogrenci no: ")
phone = input("Ogrenci telefon: ")

ogrenciler.update({
    number: {
        'Ad': name,
        'Soyad': surname,
        'Telefon': phone,
    }
})




print('*'*50)

ogrNo = input("Ogrenci no:")
ogrenci = ogrenciler[ogrNo]
print(ogrenci)

print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['telefon']}")
