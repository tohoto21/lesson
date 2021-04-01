class C:
    data = 'spam'
    def __getattr__(self, name):
        print('getattr: ' + name)
        return getattr(self.data, name)
    def __getitem__(self, i):
        print('getitem: ' + str(i))
        return  self.data[i]
    def __add__(self, other):
        print('add: ' + other)
        return  getattr(self.data, '__add__')(other)


x= C()
print(x+'er')
isinstance(x, object)
