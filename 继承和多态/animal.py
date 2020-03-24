# python 也是动态语言
# 本例是python的继承关系
# 继承的最大好处就是子类获得了父类的全部功能
# 第二个好处子类的方法可以覆盖父类的方法，多态？？？？


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('dog is running')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running')
        pass


a = list()  # a 是list类型
b = Animal()  # b 是Animal类型
c = Dog()  # c 是Dog类型

isinstance(a, list)
isinstance(b, Animal)
isinstance(c, Dog)


# dog = Dog()
# cat = Cat()

# dog.run()
# cat.run()

def run_twice(animal):
    animal.run()
    animal.run()


class Tortoise(Animal):
    def run(self):
        print('tortoise is running slowly...')


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
