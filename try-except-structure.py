#Hatalar için try/except kullanıyoruz.

#When the first conversion fails - it just drops into the except: clause and program continues.
#İlk dönüştürme başarısız olduğunda, tek istisna: yan tümcesine düşer ve program devam eder.

astr = 'Hello bob'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)

#When the second conversion succeeds - it just skips the except: clause and program continue.s
astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)
