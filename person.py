from classtools import AttrDisplay
class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def LastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * float(1 + percent * 0.01))
    #def __repr__(self):
        #for i in self.__dict__:
            #return self.__dict__.get(i)
            #return '[%s: %s]' %(i, self.__dict__[i] )
        #return '[%s: "%s", %s]' % (self.__class__.__name__,  self.name, self.pay)

class Manager(Person):
    def __init__(self, name,job, pay):
        Person.__init__(self, name,'mng', pay)
    def giveRaise(self, percent, bonus=10):
        return Person.giveRaise(self, percent + bonus)

#class Department:
    #def __init__(self,*args):
        #self.members = list(args)
    #def addMember(self, person):
        #self.members.append(person)
    #def giveRaises(self, percent):
        #for person in self.members:
            #person.giveRaise(percent)
    #def showAll(self):
        #for person in self.members:
#print(person)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    tom = Manager('Tom Jones', job='mng', pay=50000)
    #development = Department(bob,sue)
    #development.addMember(tom)
    #development.giveRaises(10)
    #development.showAll()
    #development.members
    #print(Manager.__bases__)
    #print(tom.__dict__)
    #print(bob)
    #for i in bob.__dict__:
    #print('%s: %s' % (i, bob.__dict__[i]))
    #print(sue)
    #print(bob.lastName(), sue.lastName())
    #sue.giveRaise(.10)
    print(sue)
    #tom = Manager('Tom Jones', 50000)
    #tom.giveRaise(.10)
    #print(tom.lastName())
    #print(tom)
