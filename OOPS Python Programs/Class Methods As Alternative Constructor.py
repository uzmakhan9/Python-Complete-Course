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

# creating another object to demonstrate class method as alternative constructor
ram=Employee.from_str("ram-sharma-60000")
print(ram.salary)
