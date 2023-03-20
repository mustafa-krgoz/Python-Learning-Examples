# 1. 'Bmw, Mercedes, Opel, Mazda' elemanlarına sahip bir liste oluşturunuz.
cars = ['Bmw', 'Mercedes', 'Opel', 'Mazda']
print(cars)
# 2. Liste kaç elemanlıdır?
print(len(cars))
# 3. Listenin ilk ve son elemanı nedir?
result = cars[0]
print(result)
result = cars[3]
print(result)
# 4. Mazda değerini Toyota ile değiştirin.
cars[-1] = 'Toyota'
a = cars[-1]
print(a)
# 5. Mercedes listenin bir elemanı mıdır?
b = 'Mercedes' in cars
print(b)
# 6. Listenin -2 indeksindeki değer nedir?
c = cars[-2]
print(c)
# 7. Listenin ilk 3 elamnını alın.
d = cars[0:3]
print(d)
# 8. Listenin son 2 elamanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
cars[-2:] = ['Toyota', 'Renault']
e = cars[-2:]
print(e)
# 9. Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
f = cars + ['Audi', 'Nissan']
print(f)
# 10. Listenin son elemanını silin.
del cars[-1]
s = cars
print(s)
# 11. Liste elemanlarını tersten yazdırın.
m = cars[::-1]
print(m)
# 12. Aşağıdaki verileri bir liste içinde saklayınız.
    
    #studentA: Yiğit Bilgi 2010, (70,60,70)
    #studentB: Sena Turan 1999, (80,80,70)
    #studentC: Ahmet Turan 1998, (80,70, 90)

studentA = ['Yigit', 'Bilgi', 2010, [70, 60, 70]]
studentB = ['Sena', 'Turan', 1999, [80, 80, 70]]
studentC = ['Ahmet', 'Turan', 1998, [80, 70, 90]]

# 13. Liste elemanlarını ekrana yazdırınız.

n = studentA[0]
print(n)
n = studentB[3][1]
print(n)
n = f"{studentA[0]} {studentA[1]} {2022-studentA[2]} yaşında ve not ortlaması {(studentA[3][0] + studentA[3][1] + studentA[3][2]) / 3}"
print(n)

