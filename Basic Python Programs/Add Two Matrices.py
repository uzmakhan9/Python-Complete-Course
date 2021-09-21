def matrix(rows,columns):
    row=[]
    for i in range(1,rows+1):
        col=[]
        for j in range(1,columns+1):
            element=int(input(f"Enter the matrix element at {i}th row & {j}th column:- "))
            col.append(element)
        row.append(col)
    return row

def addition(first,second):
    third=[]
    for i in range(len(first)):
        colu=[]
        for j in range(len(first[0])):
            colu.append(first[i][j]+second[i][j])
        third.append(colu)
    return third

if __name__=="__main__":
    m=int(input("Enter the no. of rows:-\n"))
    n=int(input("Enter the no. of columns:-\n"))
    print("Enter the First Matrix Elements:-\n")
    a=matrix(m,n)
    print(a)
    print("Enter the Second Matrix Elements:- \n")
    b=matrix(m,n)
    print(b)
    c=addition(a,b)
    print(f"The resultant matrix after addition is {c}")
