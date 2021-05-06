class C:
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):
        return C(self.data - other)

    def __reper__(self):
        return ' data: %s' % self.data

d=C(7)
print(d)