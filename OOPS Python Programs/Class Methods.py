class Employee:
    
    increment=3
    no_of_employees=0
    
    # constructor
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        Employee.no_of_employees +=1
    
    # defining class function
    def increase(self):
        self.salary=(self.salary*Employee.increment)
    
    # class method decorator
    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount
        # cls is a class & in class methods we pass class as a arguement

# Objects
print(Employee.no_of_employees)
uzma=Employee('uzma','Khan','30000')
print(Employee.no_of_employees)
engineer=Employee('Software','Engineer','30000')
print(Employee.no_of_employees)

print(uzma.salary)
Employee.change_increment(2)
uzma.increase()
print(uzma.salary)

print(Employee.__dict__)
# to print all the variables in that particular class