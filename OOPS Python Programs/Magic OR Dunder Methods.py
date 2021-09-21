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
    
    # class method
    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount
        # cls is a class & in class methods we pass class as a arguement
    
    # class method as constructor    
    @classmethod
    def from_str(cls,string):
        fname,lname,salary=string.split("-")
        return cls(fname,lname,salary)

    @staticmethod
    def isopen(day):
        if day=="sunday":
            return False
        else:
            return True
    
    # defining dunder method
    def __add__(self,other):
        return self.salary + other.salary
    
    def __repr__(self):
        return 'Employee({},{},{})'.format(self.fname,self.lname,self.salary)
    
    def __str__(self):
        return 'The name of employee is {}'.format(self.fname)


shyam=Employee('shyam','sharma',90000)
rhyam=Employee('rhyam','verma',9)
print(rhyam+shyam)
print(rhyam)