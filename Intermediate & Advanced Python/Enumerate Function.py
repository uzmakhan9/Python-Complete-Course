list1=['uzma','khanam','rhyam','shyam']

# without enumerate function
i=0
for item in list1:
    i=i+1
    if i%2==0:
        print(item)

# with enumerate function
for i, item in enumerate(list1):
    if(i+1)%2==0:
        print(item)