print("hello world")
age = 20
name = 'Oscar'
print('my name is {0} ,age = {1}'.format(name,age))
print('my name is' + name + 'age = ' + str(age))
# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:%^11}'.format('hey'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'  
print('{name} + {age}'.format(name = 'aa',age = 1))
print('a b c',end = '')
print(' d')
print("What's\\n your \
    name?")
print('What\'s your name?')
print(r"Newlines are indicated by \n")
