# map function 
# map(function_to_apply, list of inputs)

list1=[3,6,7,9,2,5]

# without map function
sq=[]
for item in list1:
    sq.append(item**2)
print(sq)

# with map function
def square(n):
    return n**2
squ=list(map(square,list1))
print(squ)

# filter function
def greater_than(n):
    if n>2:
        return True
    else:
        return False
list1=[1,2,4,2,7,8,99,46,4782]
greater__than=list(filter(greater_than,list1))
print(greater__than)

# reduce function
from functools import reduce
def sum_num(a,b):
    return a+b
li=[1,2,3,4,5,6,7,8,9]
lis=reduce(sum_num,li)
print(lis)