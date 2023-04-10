#Kullanıcıdan sayı okuyup, sayı hariç bir şey yazdırsın.

nawstr = input('Enter a number:')
try:
    ival = int(nawstr) #Kullanıcı int türünden sayı girerse except'e bakmaz.
except:
    ival = -1 #int' türünden sayı girilmezsse ekrana Not a number yazar.

if ival > 0:
    print('Nice work')
else:
    print('Not a number')
