#Q2) programm to accept two matrices as input and return their product if not return error msg
def inputmatrix(rows,cols,name):
    matrix=[]
    for i in range(rows):
        for j in range(cols):
             row=list(map(int,input(f"row {i+1}").split()))
             