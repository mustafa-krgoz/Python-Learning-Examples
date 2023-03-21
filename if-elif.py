from tkinter import Y


x = int(input("x:"))
y = int(input("y:"))

if(x>y):
    print("x, y'den büyüktür.")
elif(y>x):
    print("y, x'ten büyüktür.")
else:
    print("x ve y birbirine eşittir.")
    


sayi = int(input("Sayı giriniz:"))

if(sayi>0):
    print("Sayı pozitiftir.")
elif(sayi<0):
    print("Sayı negatiftir.")
else:
    print("Sayı 0 dır.")