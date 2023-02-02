def addmatrix(A,B):
    result=[[0,0,0],[0,0,0],[0,0,0]]
    #for rows
    for i in range(len(A)):
        #for columns
        for j in range(len(A[0])):
            result[i][j]=A[i][j]+B[i][j]
    for k in result:
        print(k)
    return 0
A=[[3,4,5],[2,3,4],[2,4,5]]
B=[[3,4,5],[2,3,4],[2,4,5]]
print("Result : ")
addmatrix(A,B)
