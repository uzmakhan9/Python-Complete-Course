import time
def iterative_fibonacci(n):
    if(n==0):
        print(f"fibonacci number at {n}th position is {n}")
        print(f"fibonacci series:- {n}")
    elif(n==1):
        print(f"fibonacci number at {n}th position is {n}")
        print(f"fibonacci series:- {n-1}, {n}")
    else:
        prevNum=0
        preNum=1
        currentNum=0
        lis=[0]
        print("fibonacci series:-")
        for i in range(1,n):
            prevNum=preNum
            preNum=currentNum
            currentNum=preNum+prevNum
            lis.append(currentNum)
        print(lis)
        print(f"fibonacci number at {n}th position is {currentNum}")


def recursive_fibonacci(n):
    if(n==0):
        print(f"fibonacci number at {n}th position is {n}")
        print(f"fibonacci series:- {n}")
    elif(n==1):
        print(f"fibonacci number at {n}th position is {n}")
        print(f"fibonacci series:- {n-1}, {n}")
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
        # print(f"fibonacci number at {n}th position is {fibnum}")

    
if __name__=="__main__":
    num=int(input("Enter a number\n"))
    init=time.time()
    iterative_fibonacci(num)
    # recursive_fibonacci(num)
    print(f"it took {time.time()-init} seconds")