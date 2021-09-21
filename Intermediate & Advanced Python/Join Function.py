list1=['chalk','duster','board','pen']

# without join function
for item in list1:
    if item !='pen':
        print(item,"and ",end="")
    else:
        print(item)

# with join function
print(" and ".join(list1))