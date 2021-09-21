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

class Inherited(Employee):
    def __init__(self, fname, lname, salary, proglng, exp):
        super().__init__(fname, lname, salary)
        self.progrlang=proglng
        self.expe=exp
    
    def increase(self):
        self.salary=(self.salary*Employee.increment+5)
        return self.salary

shyam=Inherited('shyam','sharma',90000,'python',5)
print(shyam.increase())
print(shyam.salary)
# print function prints the value of return in that particular function but if the function
# doesn't contain any return statement then the print function prints None