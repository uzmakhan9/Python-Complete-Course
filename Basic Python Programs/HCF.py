# import math
# print(math.gcd(9,18))

a=int(input("Enter First Number to find HCF\n"))
b=int(input("Enter Second Number to find HCF\n"))
if a<b:
    min=a
else:
    min=b
for i in range(1,min+1):
    if a%i==0 and b%i==0:
        HCF=i
print(f"HCF of {a}, {b} is {HCF}")
