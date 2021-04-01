from icecream import ic
class Spam:
    numinstances = 0
    def __init__(self):
        Spam.numinstances = Spam.numinstances + 1
    def printNuminstances(cls):
        print('Number of instances created: %s' % Spam.numinstances)
    printNuminstances = classmethod(printNuminstances)

class Sub(Spam):
    def printNuminstances(cls):
        print("Extra stuff...", cls)
        Spam.printNuminstances()
    printNuminstances = classmethod(printNuminstances)

class Other(Spam): pass

a = Spam()
ic(a.printNuminstances())
b = Sub()
ic(b.printNuminstances())
z = Other()
ic(z.printNuminstances())
