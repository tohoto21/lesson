from icecream import ic
class properties:
    dfg = 50
    def getage(self):
            return 40
    age = property(getage,None,None,None)
    def q(self):
        return 67

x = properties()
ic(x.getage())
a = properties()
ic(a.age)
ic(x.dfg)
a.fgh = 57
ic(a.fgh)
ic(a.q)