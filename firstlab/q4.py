def inputmatrix(rows,cols):
    matrix=[]
    for i in range(rows):
             row=list(map(int,input(f"row {i+1}").split()))
             if len(row) != cols:
                 print(f"col values must be this {cols}")
                 return None
             matrix.append(row)
    return matrix
def transpose(matrix):
    return[list(row) for row in zip(*matrix)]
if __name__=="__main__":
     r1,c1=map(int,input("enter no of rows and cols for matrix A").split())
     matrix=inputmatrix(r1,c1)
     if matrix is None:
         print("input is wrong")
     transp=transpose(matrix)
     print ("transposed matrix is ")
     for row in transp:
         print(row)
         
    