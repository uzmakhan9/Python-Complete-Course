# lambda functions:- one line functions, anonmyous functions
# use when you want to use your function for one time only
'''
Syntax: lambda arguement : manipulate(arguement)
'''
# without lambda function
def add(a,b):
    s=a+b
    return s
# with lambda function
add1=lambda x,y:x+y
print(add1(7,8))