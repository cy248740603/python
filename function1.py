def say_hello():
    print('hello world')
say_hello()
say_hello()

def printMax(a,b):
    if  a>=b:
        print(a,"is max")
    else:
        print(b,'is max')
printMax(1,2)
x = 3
y = 7
printMax(x,y)

j = 50
def func(x):
    print('j is', x)
    x = 2
    print('change x to',x)
func(j)
print('j is still',j)

k = 45
def func():
    global k
    print('is',k)
    k = 2
    print('change is',k)
func()
print('value for k is',k)

def say(message,times = 1):
    print(message * times)
say("aaa")
say('ooo' ,3)
say(1,3)

def func1(a,b=3,c=4):
    print('a is',a,'and b is',b,'and c is',c)

func1(3,7)
func1(c=4,a=1)

def total(a,*number,**phonebook):
    print('a',a)
    for number_item in number:
        print('number',number_item)
    for frist,second in phonebook.items():
        print(frist,second)
total(1,2,3,4,Jack=1123,John=2231,Inge=1560)

def print_max(x, y):
    '''打印两个数值中的最大数。

    这两个数都应该是整数'''
    # 如果可能，将其转换至整数类型
    x = int(x)
    y = int(y)
    
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)
print(print.__doc__)
help(print_max)
