def square(arg):
    return arg**2

class Sum:
    def __init__(self, val):
        self.val = val
    def __call__(self, arg):
        return  self.val +arg

class Product:
    def __init__(self, val):
        self.val = val
    def method(self, arg):
        return self.val * arg

class Negate:
    def __init__(self, val):
        self.val = -val
    def __repr__(self):
        return  str(self.val)


s = Sum(2)
p = Product(3)
a = [square, s, p.method]
for i in a:
    print(i(5))

print(a[-1](7))

print(list(map(lambda i: i(5),a)))
actions = [square, s, p.method, Negate]
table = {act(5): act for act in actions}
for (key, value) in table.items():
    print('{0:2} => {1}'.format(key, value))