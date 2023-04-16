x = 17
i = 1
while i<(x+2)+1:
    i+=1
    if x%i==0:
        print(x,'asal bir sayi değildir')
        break
    else:
        print(x,'asal bir sayidir')