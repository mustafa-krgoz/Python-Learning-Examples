# Identity Operator: is

x = y = [1,2,3]
z = [1,2,3]

print(x==y) # x ve y nin değerleri eşit mi?
print(x==z) 
print(x is y) # x ve y nin adresi aynı mı?
print(x is z) # x ve z nin adresi aynı mı?

x = [1,2,3]
y = [2,4]

del x[2] # x'in 2. indeksindeki elemanı sildik.(yani 3 değerini sildik.)
y[1] = 1 # y'nin 1. indekindeki elamana 1 değerini atadık.(yani 4 değeri 1 değerine çevrildi.)
y.reverse()
print("x ve y değerleri birbirine eşit mi?:", x==y)
print("x ve y adresleri birbirne eşit mi?:" ,x is y)

# Membership Operator: in

x = ["apple, banana"]
print("banana" in x) # banana, x listesinin içinde mi?

name = 'Çınar'
print('a' in name) # a karakteri, name dizisinin içinde mi?
print('a' not in name) # a karakteri, name dizisinin içinde DEĞİL mi?