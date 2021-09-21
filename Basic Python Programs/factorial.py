# calculate the factoraial of a number
# find the number of trailing zeros in that factorial

def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number*factorial(number-1)

def trailing(num):
    count=0
    i=5
    while(num//i!=0):
        count =  count+(num//i)
        i=i*5
    return count

if __name__=="__main__":
    num=int(input("Enter the number: \n"))
    fact=factorial(num)
    print(f"The factorial of {num} is {fact}")
    number=int(input("Enter a number to find the trailing zeros of its factorial \n"))
    zeros=trailing(number)
    print(f"The no. of trailing zeros in factorial of {number} is {zeros}")
