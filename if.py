number = 23
guess = int(input('Enter an integer :'))

if guess == number :
    # 新块从这里开始
    print('==')
    print('==')
    # 新块在这里结束
elif guess < number:
    print('<<')
else:
    print('>>')
print('done')