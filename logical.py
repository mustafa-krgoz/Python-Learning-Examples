x = 5
hak = 5
devam = 'e'

result = 5 < x < 10
print(result)

#and
sonuc = (x>5) and (x<10)
print(sonuc)
sonuc = (hak > 0) and (devam == 'e')
print(sonuc)

#or
result = (x>0) or (x%2 == 0)
print(result)

#not
result = not(x>0) # Normalde 5 büyüktür ama not ile sonucu false çıkardık.
print(result)

# x =  5 ile 10 arasında çift sayı mı?
result = (x>=5) and (x<10) or (x%2 == 0)
print("x' in sonucu: " , result)