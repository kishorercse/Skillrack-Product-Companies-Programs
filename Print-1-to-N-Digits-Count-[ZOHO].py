"""
A positive integer N is passed as the input. If we print all the numbers from 1 to N continuosly, the program must find the number of characters(digits) C printed and print the 
count C as the output.

Input Format:
The first line contains N.

Output Format:
The first line contains C.

Boundary Conditions:
1 <= N <= 9999999

Example Input/Output 1:
Input:
2

Output:
2

Explanation:
We print 12 and hence the total number of characters is 2.

Example Input/Output 2:
Input:
15

Output:
21

Explanation:
We print 123456789101112131415 and hence the total number of characters is 21.
"""
n=input().strip()
l=len(n)
n=int(n)
c=int('1'+'0'*(l-1))
res=0
while c>0:
    res+=l*(n-c)+1
    n=c
    c//=10
    l-=1
print(res)
