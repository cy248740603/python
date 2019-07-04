number = 23
running = True

while running:
    guess = int(input('input number :'))
    
    if guess == number:
        running = False
    elif guess > number:
        print('>>')
    else:
        print('<<')
else :
    print('done')