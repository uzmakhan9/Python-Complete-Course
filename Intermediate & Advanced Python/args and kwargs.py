# *args and **kwargs 
# can also written this:- *vars and **kvars

def function_1(*args):
    print(type(args))
    if(len(args)==3):
        print("the name is",args[0],"and age is",args[1],"and roll no. is",args[2])
    else:
        print("the name is",args[0],"and age is",args[1])

def printmarks(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,value)

def master(normal,*args,**kwargs):
    print(normal)
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(key,value)

list=["uzma",22]
function_1(*list)
marklist={"uzma":100,"yasira":99,"tahira":98}
printmarks(**marklist)
master("normal arguement",*list,**marklist)
