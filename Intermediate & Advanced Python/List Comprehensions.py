# List Comprehensions
# Dictionary Comprehensions
# Set Comprehensions
# Generator Comprehensions

# without using list comprehensions
list_1=[1,34,67,89,4,3,90,42,9,92]
divide_by_3=[]
for item in list_1:
    if item % 3 == 0:
        divide_by_3.append(item)
print(divide_by_3)

# using list comprehensions
print([item for item in list_1 if item%3==0])

# Dictionary Comprehensions
dict_1={'a':9,'b':8,'A':7,'B':67}
print({k.lower():dict_1.get(k.lower(),0)+dict_1.get(k.upper(),0)for k in dict_1.keys()})

# Set Comprehensions
squared={x**2 for x in [1,1,1,2,2,2,3,3,3,3,4,4,4,4,5,5,55,5,6,66,6,]}
print(squared)

# Generator Comprehensions
gen=(i for i in range(45)if i%3==0)
for item in gen:
    print(item)