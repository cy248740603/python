#this is my shopping list
shoplist = ['apple','mango','carrot','banana']

print('I have',len(shoplist),'items to purchase.')

print('These items are:',end = ' ')
for item in shoplist:
    print(item,end = ' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now',shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is',shoplist)

print('The first item I will buy is',shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the',olditem)
print('My shopping list is now', shoplist)
# 我会推荐你总是使用括号
# 来指明元组的开始与结束
# 尽管括号是一个可选选项。
# 明了胜过晦涩，显式优于隐式
zoo = ('python','elephant','penguin')
print('zoo len is',len(zoo))

new_zoo = 'monkey','camel',zoo
print('new zoo len is',len(new_zoo))
print('new zoo is',new_zoo)
print('old zoo is',new_zoo[2])
print('last old zoo is',new_zoo[2][2])
print('Number of animals in the new zoo is',
      len(new_zoo)-1+len(new_zoo[2]))
# “ab”是地址（Address）簿（Book）的缩写

ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])
# 删除一对键值—值配对
del ab['Swaroop']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))
for name,address in ab.items():
    print('Contact {} at {}'.format(name,address))
# 添加一对键值—值配对
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])  

name = 'swaroop'
# Indexing or 'Subscription' operation #
# 索引或“下标（Subscription）”操作符 #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])
# Slicing on a list #
print('Item 1 to 3 is',shoplist[1:3])
print('Item 2 to end is',shoplist[2:])
print('Item 1 to -1 is',shoplist[1:-1])
print('Item start to end is',shoplist[:])
# 从某一字符串中切片 #
print('characters 1 to 3 is',name[1:3])
print('characters 2 to end is',name[2:])
print('characters 1 to -1 is',name[1:-1])
print('characters start to end is',name[:])

bri = set(['brazil', 'russia', 'india'])
'india' in bri.copy()
print('Simple Assignment')
# mylist 只是指向同一对象的另一种名称
mylist = shoplist
# 我购买了第一项项目，所以我将其从列表中删除
del shoplist[0] 

print('shoplist is',shoplist)
print('mylist is',mylist)
# 注意到 shoplist 和 mylist 二者都
# 打印出了其中都没有 apple 的同样的列表，以此我们确认
# 它们指向的是同一个对象
print('Copy by making a full slice')
# 通过生成一份完整的切片制作一份列表的副本
mylist = shoplist[:]
# 删除第一个项目
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
