"""
The program must accept N integers and an integer K as the input. The program must print every K integers in descending order as the output. 
Note: If N % K != 0, then sort the final N%K integers in descending order.

Boundary Condition(s):
1 <= N <= 10^4
-99999 <= Array Element Value <= 99999

Input Format:
The first line contains the values of N and K separated by a space.
The second line contains N integers separated by space(s).

Output Format:
The first line contains N integers.

Example Input/Output 1:
Input:
7 3
48 541 23 68 13 41 6

Output:
541 48 23 68 41 13 6

Explanation:
The first three integers are 48 541 23, after sorting in descending order the integers are 541 48 23.
The second three integers are 68 13 41, after sorting in descending order the integers are 68 41 13.
The last integer is 6.
The integers are 541 48 23 68 41 13 6
Hence the output is 541 48 23 68 41 13 6.

Example Input/Output 2:
Input:
5 2
1 -3 -44 2 77 

Output:
1 -3 2 -44 77
"""
n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(0,n,k):
    print(*sorted(l[i:i+k],reverse=True),end=' ')
