"""
Given a number N, the program must print if N is a step number or not. (A step number is a number which has a digit which is either 1 more or 1 less than the previous digit).

Input Format:
The first line contains N.

Output Format:
The first line contains yes or no

Boundary Conditions:
10 <= N <= 99999999

Example Input/Output 1:
Input:
1212343

Output:
yes

Example Input/Output 2:
Input:
342345

Output:
no

Explanation:
The difference between 2 and 4 is NOT 1.
"""
n=input().strip()
l=len(n)
if all(abs(int(n[i])-int(n[i-1]))==1 for i in range(1,l)):
    print("yes")
else:
    print("no")
