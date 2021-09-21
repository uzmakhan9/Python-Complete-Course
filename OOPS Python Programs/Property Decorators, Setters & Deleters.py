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
    
    # property decorator
    @property
    def email(self):
        if self.fname==None:
            return 'email not set'
        else:
            return self.fname+'.'+self.lname+'@gmail.com'

    # setter
    @email.setter
    def email(self,given_email):
        name_list=given_email.split('@')[0].split('.')
        self.fname=name_list[0]
        self.lname=name_list[1]

    # deleter
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
    
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
    
if __name__=='__main__':
    shyam=Employee('shyam','sharma',90000)
    rhyam=Employee('rhyam','verma',9)
    print(rhyam.email,shyam.email)
    rhyam.lname='khanna'
    print(rhyam.email)
    shyam.email='sharma.shyam@gmail.com'
    print(shyam.email)
    del shyam.email
    print(shyam.email)