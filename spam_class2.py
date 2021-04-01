class Spam:
    numinstances = 0
    def count(cls):
        cls.numinstances += 1
    def __init__(self):
        self.count()
    count = classmethod(count)

class Sub(Spam):
    numinstances = 0
    def __init__(self):
        Spam.__init__(self)

class Other(Spam):
    numinstances = 0

x = Spam()
s1,s2 = Sub(),Sub()
d1,d2,d3 = Other(),Other(),Other()
print(Spam.numinstances, Sub.numinstances, Other.numinstances)

