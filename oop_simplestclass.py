class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hello,my name is',self.name)
    @classmethod
    def how_many(cls):
        pass

p = Person('Oscar')
p.say_hi()
# 前面两行同样可以写作
# Person().say_hi()