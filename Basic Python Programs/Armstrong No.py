def checkArmstrong(n):
    sum=0
    number=n
    order=len(str(n))
    while(n>0):
        digit=n%10
        sum+=digit**order
        n=n//10
    if(sum==number):
        print("An Armstrong Number")
    else:
        print("Not An Armstrong Number")

if __name__=="__main__":
    num = int(input("Enter A Number To Check For Armstrong\n"))
    checkArmstrong(num)