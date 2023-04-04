fruits = {'orange', 'apple', 'banana'}
# print(fruits[0])  Liste indekslenemez.

for x in fruits:
    print(x)

fruits.add('cherry') # Listeye cherry bilgisini ekledi.
fruits.update(['mango','grape']) # Listeye mango ve grape i ekledi.
fruits.remove('orange') # Orange'ı listeden sildi.
fruits.discard('apple') # Apple'ı sildi.

print(fruits)
fruits.pop() # Listedeki ilk eleamanı sildi.
fruits.clear()
print(fruits)




myList = [1,2,2,4,5,6,6,3]
print(set(myList)) # Tekrarlayan elemanlar dizi içerisinden çıkarılır.


