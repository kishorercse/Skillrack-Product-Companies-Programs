"""
N integer values (positive, zero or negative) are passed as input to the program. The program must print the values of the integers (in the order of occurrence) which are 
greater than all the previous values.

Input Format:
The first line will contain N.
The second line will contain the N integer values, with the values separated by a space.

Output Format:
The first line will contain the integer values which are greater than all the previous values separated by a space.

Boundary Conditions:
2 <= N <= 10000

Example Input/Output 1:
Input:
4
3 -5 8 1

Output:
3 8

Explanation:
3 is the first number and printed. After that 8 is printed as it is greater than 3 and -5.

Example Input/Output 2:
Input:
12
1 2 5 7 19 20 12 11 9 15 45 45

Output:
1 2 5 7 19 20 45
"""
n=int(input())
l=list(map(int,input().split()))
mx=-999999999
for i in range(n):
    if l[i]>mx:
        print(l[i],end=' ')
        mx=l[i]
