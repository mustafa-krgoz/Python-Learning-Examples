# x = 5
# y = 10
# z = 15

x, y, z = 5, 10, 15


# x,y = y,x

x+=5 # x = x+5
y-=2 # y = y-2
z*=2 # z = z*2
z%=10 # Mod alma = bölümünden kalan kaç?
x//=3 # Tam bölme = virgülden sonrayı almıyoruz.
x**=y # 3 üssü 8 yapmış oldu ve x in değeri değişti.

print(x,y,z)

values = 1, 2, 3, 4, 5 # tuple listesi oluşturduk.
print(values)
print(type(values))

x,y,*z = values # z ye * koyarak 3,4,5 liste olmuş oldu.
print(x,y,z)
print(x,y,z[1])