def extra(self, arg): ...
class Extras(type):
    def __init__(Class, classname, superclasses, attributedict):
        if required():
            Class.extra = extra

class Client1(metaclass=Extras): ...
class Client2(metaclass=Extras): ...
class Client3(metaclass=Extras): ...
X = Client1()
X.extra()
print(type(Extras))
'''Запуск мета идет после запуска класса и дополняет его  '''
object