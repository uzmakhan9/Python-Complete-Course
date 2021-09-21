# importing built-in bisect module
import bisect
number=76
list1=[1,2,6,43,98,789,8765]
# sorted list

print(bisect.bisect(list1,number))
# it will give the index number where we should put this number for the list to be remain sorted

bisect.insort(list1,number)
# it will insert the number to the correct index for the list to be remain sorted

print(list1)