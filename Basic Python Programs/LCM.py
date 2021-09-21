a=int(input("Enter First Number to find LCM\n"))
b=int(input("Enter Second Number to find LCM\n"))
maxnum=max(a,b)
while(True):
    if maxnum%a==0 and maxnum%b==0:
        break
    else:
        maxnum += 1
print(f"LCM of {a}, {b} is {maxnum}")