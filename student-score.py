score = input("Enter score:")

try:
 ex = float(score)
except: 
    print('Error, please enter numeric input.')
    quit()

if 1.0> ex >= 0.9:
        print('A')
elif 0.9> ex >= 0.8:
        print('B')
elif 0.8> ex >= 0.7:
        print('C')
elif 0.7> ex >= 0.6:
        print('D')
elif 0.6 > ex > 0.0:
        print('F')
else:
      print('Error, please enter valid grade.')

