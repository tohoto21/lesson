class Method:
    def imeth(self, x):
        print([self, x])

    @staticmethod
    def smeth(x):
        print([x])

    @classmethod
    def cmeth(cls, x):
        print([cls, x])

    @property
    def name(self):
        return 'Bob ' + self.__class__.__name__

a = Method()
print(a.name)
