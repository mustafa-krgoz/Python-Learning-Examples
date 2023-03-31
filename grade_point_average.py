visa = float(input('Enter your visa note: '))
ffinal = float(input('Enter your final note: '))

average = (visa*0.4) + (ffinal*0.6)

if(ffinal>=50):
    if(average>=50):
        print(f"Average: {average}, You passed the lesson.")
    else:
        print(f"Average: {average}, You did not pass the lesson.")
else:
    print(f'Average: {average}, You did not pass the lesson. ')