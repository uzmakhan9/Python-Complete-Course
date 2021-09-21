class Employee:
    # constructor
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary

# Objects
uzma=Employee('uzma','Khan',30000)
engineer=Employee('Software','Engineer',30000)

print(uzma.fname,engineer.lname,uzma.salary)
