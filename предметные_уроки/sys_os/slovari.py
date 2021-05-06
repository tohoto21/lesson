from icecream import ic
class Person:
    def __init__(self,name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    def lastName(self):
        return self.name.split()[-1]
    def payUp(self, procent):
        self.pay*= (1.0 + procent)


if __name__ == '__main__':
    bob = Person('Bob Smith', 42 , 30000, 'software')
    sue = Person('Sue Jones',45, 40000, 'hardware')
    print(bob.name, sue.name)

    print(bob.name.split()[-1])
    sue.pay *=1.10
    print(sue.name,':',sue.pay)
    worker = [bob,sue]
    d = [persan.name for persan in worker if persan.pay > 30000]
    print(d)
    ic(bob.lastName())
    sue.payUp(0.2)
    ic(sue.pay)




