with open('currencyConvertor.txt') as f:
    lines=f.readlines()
# learn file handling for better understanding

currencyDict={}
# made an empty dictionary
for line in lines:
    parsed=line.split("\t")
    # split is a function who splits the string by given separator into a list
    currencyDict[parsed[0]]=parsed[1]
    # parsing that splitted list into dictionary

amount=int(input("Enter the amount: \n"))
print("Enter the name of currency you want to convert this amount to?\nAvailable Options:-\n")
[print(item) for item in currencyDict.keys()]
# we can also use print statement as written above(list comprehensions)
currency=input("please enter one of these values:\n")
print(f"{amount} INR is equal to {amount*float(currencyDict[currency])} {currency}")
# because inputted currency is string type,thus we have to type cast it into float 
# for the currency conversion