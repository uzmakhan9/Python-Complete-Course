def matrix(rows,columns):
    row=[]
    for i in range(1,rows+1):
        column=[]
        for j in range(1,columns+1):
            element=int(input(f"Enter the matrix element at {i}th row & {j}th column:- "))
            column.append(element)
        row.append(column)
    return row

def multiply(first,second):
    third=[]
    sum=0
    for i in range(len(first)):
        row=[]
        for j in range(len(second[0])):
            for k in range(len(second)):
                sum += first[i][k]*second[k][j]
            row.append(sum)
            sum=0
        third.append(row)
    return third

if __name__=="__main__":
    m=int(input("Enter the no. of rows of first matrix:-\n"))
    n=int(input("Enter the no. of columns of first matrix:-\n"))
    o=int(input("Enter the no. of rows of second matrix:-\n"))
    p=int(input("Enter the no. of columns of second matrix:-\n"))
    if(n==o):
        print("Enter the First Matrix Elements:-\n")
        a=matrix(m,n)
        print(a)
        print("Enter the Second Matrix Elements:- \n")
        b=matrix(o,p)
        print(b)
        c=multiply(a,b)
        print(f"The resultant matrix after multiplication is {c}")
    else:
       print("**** Can't Multiply Two Matrices!!! ****\n"
        "Columns of First Matrix doesn't match with the Rows of the Second Matrix") 
