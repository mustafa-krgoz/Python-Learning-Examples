# value types => string, number
x = 5
y = 25

x = y 
y = 10 # y de yaptığımız değişiklik x 'i etkilemiyor.

print(x,y)

# references types => list 
a = ['apple', 'banana']
b = ['apple' , 'banana']

a = b 

b[0] = 'grape' # b de yaptığımız değişiklik a yı etkiliyor.
print(a,b)