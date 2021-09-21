import math
print("hello world") 
''' this is a multiline comment
string is used in "" '''
print(5+8)
print(math.gcd(3,6))
# this is indentation
# if(age<18): 
    # this is inside if

a=34
b="uzma"
c=45.32
d=3

''' operators in python
1. ** exponentiation operator
2. // floor division operator
3. % modulo operator '''

print(a+d)
print(a-d)
print(a*d)
print(a/d)
print(a**d)
print(a//d)
print(a%d)

# rules for creating variables
# 1. variable should start with a letter or an underscore
# 2. variable cannot start with a number
# 3. It can only contain alpha numeric characters
# 4. variable names are case sensitive

typeA=type(a)
print(typeA)
e="31"
# e=3.14
e=int(e) 
# type casting
print(type(e))
print(e+2)

# strings
name="uzma"
name1= '''      my 
                 name is uzma '''
name2="uzma, khan"
print(name1)
print(name[0])
print(name[0:4])
print(name1.strip())
# strip function removes first and last spaces in the string 
print(len(name1))
# len to give the length of the string 
print(name.lower())
print(name.upper())
# lower and upper function to change into lower and upper case respectively
print(name.replace("zm","s"))
print(name2.replace(", ","\n"))
# replace function is used to replace the given string into another string:- var.replace("str","str")
print(name2+name1)
# concatenation of two strings 

# making of template in 3 differnt ways:-
uk="software developer"
temp="{} is a good girl and she will be a good {} one day.".format(name,uk)
print(temp)
temp="{1} is a good girl and she will be a good {0} one day.".format(name,uk)
print(temp)
temp=f"{name} is a good girl and she will be a good {uk} one day."
print(temp)

''' python collections:- 
1. list
2. tuple
3. set
4. dictionary '''

lst=[61,1,2,3,4,54]
print(type(lst))
# indexing
print(lst[2])
print(lst[0:6])
# we can change any value in list
lst[3]=87
print(lst)
print(len(lst))

# list functions:-
lst.append(100)
print(lst)
lst.insert(1,49)
print(lst)
lst.remove(61)
print(lst)
lst.pop()
print(lst)
del lst[4]
print(lst)
lst.clear()
print(lst)
del lst

# tuple
a=("uzma","khan") 
# tuple is defined in parenthesis()
print(a)
print(type(a))
''' tuple is unchangeable, we cannot change values in tuple such as:- a[1]="khanam"
but we can type cast tuple. '''
a=list(a)
print(a)

# set
s1={67,7,7,8,9,8,5,4,6,8,4,4,3,2}
s2={4,5,6,9,2,0}
# set removes the repetitive values 
print(s1)
s1.add(89)
print(s1)
s1.update([98,67,2,5,12,34,54])
print(s1)
print(len(s1))
# s1.remove(90)
s1.discard(90)
# difference between remove and discard is that remove gives a error if wrong value inputted but discard dont
print(s1|s2)
# union of sets
print(s1&s2)
# intersection of sets 
print(s1-s2)
# difference of sets 
print(s1^s2)
# symmetric difference of sets 

''' dictionary 
it is key value pairs stored in an object '''
uzmaDict={
    "name":"uzma",
    "branch":"CS",
    "marks":78.00,
    "year":4
}
print(uzmaDict)
print(uzmaDict["year"])
uzmaDict["marks"]=90
print(uzmaDict)
''' similarly we can use update,clear,pop,del and all the functions we used in list 
can be used in tuples,sets and dictionary too. '''

# conditional statements 
age=60
age=input("enter your age\n")
# we can take input from the users by using input function 
print(age)
print(type(age))
# input function takes value as string 
age=int(age)
print(type(age))
if(age>18):
    print("you can drive")

elif(age==18):
    print("you're still a teen.")

# elif is used for if ladder     
else:
    print("you cannot drive")

# loops or iterative statements 
for i in range(0,1001):
    print(i)

li=[1,9,"uzma"]
for item in li:
    print(item)
# similarly we can use loops to iterate tuples, sets and dictionaries 

i=0
while(i<10):
    print(i+1)
    break
# break is used to break the loop

i=0
while(i<100):
    i=i+1
    if i==78:
        continue
    print(i+1)
# continue is used to skip the iteration 

# functions 
def greet():
    print("good morning sir")
    print("good morning madam")
greet()
def sum(a,b):
    c=a+b
    return c
d=sum(89,67)
print(d)

# class and its constructor 
class employee:
    def __init__(self,gname,gsalary):
        self.name=gname
        self.salary=gsalary
uzma=employee("uk",30000)
print(uzma.name)
print(uzma.salary)     