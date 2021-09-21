def transform(a):
    for i in range(len(a)-1):
        if(a[i]==1):
            a[i]=0
            if(a[i+1]==1):
                a[i+1]=0
            else:
                a[i+1]=1
            print(lis)


if __name__=="__main__":
    lis=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    print(lis)
    transform(lis)