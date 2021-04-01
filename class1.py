class Employee:
    def computeSalary(self):
        pass
    def giveRaise(self):
        pass
    def promote(self):
        pass
    def retire(self):
        pass

class Engineer(Employee):
    def computeSalary(self):
        pass

bob = Employee()
sue = Employee()
tom = Engineer()
company = [bob, sue, tom]
for emp in company:
    print(emp.computeSalary())
    
