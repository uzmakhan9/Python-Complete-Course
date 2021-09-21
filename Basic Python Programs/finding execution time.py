from time import time

def function1(a,b):
    return a+b

def function2(a,b):
    num1=a
    num2=b
    if(a>b and a!=3):
        pass
    sum([4,3])
    return a+b

if __name__=='__main__':
    
    init=time() 
    # to initialize the time
    
    for i in range(0,100000):
        function1(3,5)
    
    print("function 1 execution time: ",time()-init)
    
    init=time()
    #  again initializing the time
    
    for i in range(0,100000):
        function2(3,5)
    
    print("function 2 execution time: ",time()-init)