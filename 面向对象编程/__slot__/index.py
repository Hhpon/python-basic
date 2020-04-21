from types import MethodType


class Student(object):
    pass


def set_age(self, age):
    self.age = age


def set_score(self, score):
    self.score = score


Student.set_score = set_score

person1 = Student()

person2 = Student()

person1.set_age = MethodType(set_age, person1)

person1.name = 'hhp'
person2.set_score(100)
person1.set_age(25)

print(person2.score)
print(person1.name)
print(person1.age)
