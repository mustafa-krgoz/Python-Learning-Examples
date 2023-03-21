from unittest import result


name = "Mustafa"
surname = 'Karagöz'
age = 20

#print('My name is {} {}'.format(name, surname))
#print('My name is {1} {0}'.format(name, surname))
#print('My name is {n} {s}'.format(s=name,n=surname))
#print("My name is {} {} and I'm {} years old.".format(name, surname, age))

result = 200/700
print("the result is {}".format(result))
print("the result is {r:1.4}".format(r=result))

print(f"My name {name} {surname} and I'm {age} years old.")