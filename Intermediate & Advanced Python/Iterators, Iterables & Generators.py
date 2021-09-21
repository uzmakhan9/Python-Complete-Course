# Iterables:- It is an object which has __iter or __getitem method defined, it gives iterator
# Iterators:- It is an object in which next method is defined to fetch the next element
# Iteration:- The process of iterating & fetching new elements is known as iteration
# Generator:- It is an iterator which can iterate only one time,we can generate on-the-fly values from this
def gen(n):
    for j in range(n):
        yield j

print(gen(10000000))   
for i in gen(10000):
    print(i)

#testing this statement:-"generators iterate only one time",it yield on-the-fly values&dont occupy complete RAM 
ob1=gen(5)
print(next(ob1))
print(next(ob1))
print(next(ob1))
print(next(ob1))
print(next(ob1))
# print(next(ob1))

# integer object is not iterable whereas string object is iterable