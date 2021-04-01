from icecream import ic
class A:
    def __get__(self, instance, owner): return 40
    def __set__(self, instance, value): instance.g = value
class d:
        age = A()
x = d()
ic(x.age)
x.age = 42
ic(x.age)
ic(x.g)