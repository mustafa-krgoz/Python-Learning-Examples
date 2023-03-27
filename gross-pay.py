hrs = input('Enter Hours:')
pay = input("Enter Per Hour:")

try:
    h = float(hrs)
    c = float(pay)
except:
    print('Error, please enter numeric input')
    quit()

if h>40:
    gross = 40*c + (h-40)*(c*1.5)
else:
    gross = h*c
print('Gross Pay:', gross)