#Q2) programm to accept two matrices as input and return their product if not return error msg
def inputmatrix(rows,cols,name):
    matrix=[]
    for i in range(rows):
             row=list(map(int,input(f"row {i+1}").split()))
             if len(row) != cols:
                 print(f"col values must be this {cols}")
                 return None
             matrix.append(row)
    return matrix
def multiply(A,B):
    rows1,cols1=len(A),len(A[0])
    rows2,cols2=len(B),len(B[0])
    if cols1!=rows2:
        return "error matrix are incompatiable"
    result=[[0 for q in range(cols2)]for q in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j]+=A[i][k] * B[k][j]
    return result
if __name__=="__main__":
    r1,c1=map(int,input("enter no of rows and cols for matrix A").split())
    r2,c2=map(int,input("enter no of  rows and cols for matrix B").split())
    matrix1=inputmatrix(r1,c1,"firstmatrix")
    matrix2=inputmatrix(r2,c2,"secondmatrix")
    if matrix1 is None or matrix2 is None:
        print("wrong input")
    else:
        result=multiply(matrix1,matrix2)
        print("answer is :")
        print(result if isinstance(result,str) else '\n'.join(map(str,result)))
        