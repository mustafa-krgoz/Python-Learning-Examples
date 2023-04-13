list = [1, 2, 3]
tuple = (1, 'iki', 3)

print(type(list))
print(type(tuple))

print(list[1])
print(tuple[1])

print(len(list))
print(len(tuple))

list = ['Ali', 'Ahmet']
tuple = 'Damla', 'Ayşe' ,'Ayşe'
names = ('Demet', 'Emel') + tuple
print(names)

list[0] = 'Mustafa'
#tuple[0] = 'Yunus' # Tuple listesinde bu şekilde nesneyi değiştiremiyoruz.


print(list)
print(tuple)

print(tuple.count('Ayşe'))
print(tuple.index('Damla'))