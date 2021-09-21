# without format function
users=['uzma khan','rhyam','shyam']
computer=['dell','hp','apple']
for i in range(0,len(users)):
    print("computer used by",users[i],"is",computer[i])

# with format function
for i in range(0,len(users)):
    template="computer used by {} is {}".format(users[i],computer[i])
    print(template)

# with format function we can swap the values
for i in range(0,len(users)):
    template="computer used by {1} is {0}".format(users[i],computer[i])
    print(template)