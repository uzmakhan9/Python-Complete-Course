from os import access


class Employee:
    
    increment=3
    no_of_employees=0
    # defining class variables
    
    # constructor
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        Employee.no_of_employees +=1
    
    # defining class function
    def increase(self):
        self.salary=(self.salary*Employee.increment)
        #  A class object can access both class variables as well as instance variables.

# Objects
print(Employee.no_of_employees)
uzma=Employee('uzma','Khan','30000')
print(Employee.no_of_employees)
engineer=Employee('Software','Engineer','30000')
print(Employee.no_of_employees)

print(uzma.fname,engineer.lname,uzma.salary)

uzma.increase()
print(uzma.salary)

print(Employee.__dict__)
# to print all the variables in that particular class
# and to print the variables of a particular instance, we can type this:
print(uzma.__dict__)