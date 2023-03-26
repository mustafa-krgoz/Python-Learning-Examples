numbers = [1, 10, 5, 16, 4, 9, 10 ]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val = max(numbers)
val = min(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]

numbers[4] = 40 # Dizideki 4 rakamının yerine 40 sayısını ekledik.

numbers.append(49) # Dizinin sonuna yeni sayı ekliyor.
numbers.append(59)
numbers.insert(3, 78)  # 3. karakterden önce 78 sayısını ekliyor.
numbers.insert(-1, 52)
#numbers.pop() # Sondaki sayı siliniyor.
numbers.pop(0) # İlk karakterdeki sayı siliniyor.
numbers.pop(-1)
numbers.remove(49) # Dizideki istediğimiz sayıyı silebiliyoruz.

numbers.sort() # Liste sayısal büyüklük olarak sıralanır.
numbers.reverse() # Sıraladıktan sonra ters çevirir.
letters.sort() # Liste alfabetik olarak sıralanır.

print(numbers)
print(letters)

print(len(numbers)) # Liste de kaç karakter var?
print(len(letters))

print(numbers.count(10)) # Liste de 10 sayısından kaç tane var?
print(numbers.count('a'))

numbers.clear() # Listedeki tüm elemanları siler.
print(numbers)
