#!/usr/bin/python

class Employee:
    'Common base class for all employees'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1

    def displayCount(self):
        print("Total Employee: %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name of Employee: %s , Salary  = %d" % (self.name, self.salary))

emp1 = Employee("Chetna", 98000)
emp2 = Employee("Tanmay", 45000)

emp1.displayEmployee()
emp2.displayEmployee()
emp2.displayCount()

print("Display Class Attributes:  ")
print("Employee.__doc__: %s" % Employee.__doc__)
print("Employee.__name__: %s" % Employee.__name__)
print("Employee.__module__: %s" % Employee.__module__)
print("Employee.__bases__: %s" % Employee.__bases__)
print("Employee.__dict__: %s" % Employee.__dict__)