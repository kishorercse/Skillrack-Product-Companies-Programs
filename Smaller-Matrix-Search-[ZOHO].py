"""
A bigger NxN matrix is passed as the input. Also a smaller MxM matrix is passed as input. The program must print TRUE if the smaller matrix can be found in the bigger matrix.
Else the program must print FALSE.

Input Format:
First line will contain the value of N.
Second line will contain the value of M.
Next N lines will contain the values in the N*N matrix with each value separated by one or more space.
Next M lines will contain the values in the M*M matrix with each value separated by one or more space.

Output Format:
First line will contain the string value TRUE or FALSE

Boundary Conditions:
3 <= N <= 20
2 <= M <= N

Example Input/Output 1:
Input:
3
2
4 5 9
1 3 5
8 2 4
3 5
2 4

Output:
TRUE

Example Input/Output 2:
Input:
3
2
4 5 9
1 3 5
8 2 4
4 5
1 4

Output:
FALSE
"""
n=int(input())
m=int(input())
a=[input().split() for _ in range(n)]
b=[input().split() for _ in range(m)]
for i in range(n-m+1):
    for j in range(n-m+1):
        r=0
        f=True
        for ii in range(i,i+m):
            c=0
            for jj in range(j,j+m):
                if a[ii][jj]!=b[r][c]:
                    f=False
                    break
                c+=1
            if not f:
                break
            r+=1
        else:
            print("TRUE")
            exit()
print("FALSE")
