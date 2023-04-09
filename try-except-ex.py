astr = 'Bob'
try:
    print('Hello')
    istr = int(astr) #Burada hata olduğu için direkt except'e gider.
    print("There")
except: # try'ın içindekilere geri dönmez.
    istr = -1
print('Done', istr)
