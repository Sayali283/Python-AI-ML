r=int(input("Enter the no. of rows"))
c=int(input("Enter the no. of columns:"))
print("Enter the elements of matrix A:")
A=[]
for i in range(r):
    row=list(map(int, input().split()))
    A.append(row)
print("Enter the Elements of Matrix B:")
B=[]
for i in range(r):
    row=list(map(int, input().split()))
    B.append(row)
print("\nMatrix A:")
for row in A:
    print(row)
print("/nMatrix B:")
for row in B:
    print(row)
#Addition of two matrix
print("Addition of A and B Matrix:")
for i in range(r):
    for j in range(c):
        print(A[i][j] + B[i][j],end=" ")
        print()
#Substarction of Matrix
print("Substration of A and B Matrix:")
for i in range(r):
    for j in range(c):
        print(A[i][j] - B[i][j],end=" ")
        print()
