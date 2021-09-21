# take input
print("Enter your Number")
num=int(input())

temp=num
reverse=0

while(num>0):
    dig=num%10
    reverse=reverse*10+dig
    num=num//10
    # floor function

if temp==reverse:
    print("Number is a Palindrome.")
else:
    print("Number is not a Palindrome.")

