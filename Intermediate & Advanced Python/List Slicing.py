list1=[2,3,4,5,6,7,8]
print(list1[1:7])
# 7-1=6 elements it will print

print(list1[0:71])
# it will not throw error if we exceed the last limit of the list

print(list1[:5])
print(list1[2:])

# negative slicing
print(list1[:-5])
# print(list1[:-5])=print(list1[:2])

print(list1[::2])
# it will print the list with the gap of 1 element

print(list1[::-2])
# it will print the list reversely with the gap of one element

print(list1[::-1])
# it will reverse the list