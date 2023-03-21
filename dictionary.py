# key - value
# 41 ==> kocaeli 34 ==> İstanbul

sehirler = ['Kocaeli', 'İstanbul']
plakalar = [41, 34]

print(plakalar[sehirler.index('Kocaeli')])
print(sehirler[plakalar.index(34)])

# plakalar = {"key" : "value"}
plakalar = {'İstanbul': 34 , 'Kocaeli': 41}
print(plakalar['İstanbul'])
print(plakalar['Kocaeli'])

plakalar['Ankara'] = 6 # Olmayan bir key için yeni bir eleman ekleyebiliyoruz.
plakalar['Kocaeli'] = 'new value' # Var olan bir key in value sunu değiştiriyoruz.

print(plakalar)

users = {
    'mustafakaragoz':{
        'age': 20,
        'roles': 'softwareengineering',
        'email': 'karagozhalitmustafa@gmail.com',
        'address' : 'Diyarbakir',
        'phone': 86547
    },
    'yunustank':{
        'age': 20,
        'roles': 'computerengineering',
        'email': 'tankengineer@gmail.com',
        'addrees': 'Almanya',
        'phone': 9645340
    }
}
print(users['mustafakaragoz'])
print(users['yunustank']['roles'])
print(users['yunustank']['age'])
