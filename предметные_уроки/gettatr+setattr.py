class C:
    def __getattr__(self, item):
        if item == 'name':
            return print(56)
        else:
            raise Че за хрень, а не атрибут??(item)

x=C()
x.name
x.age