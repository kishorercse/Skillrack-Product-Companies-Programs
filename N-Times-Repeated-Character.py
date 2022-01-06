"""
Given a string S and an occurrence frequency N, find the last character in the String that appears exactly N times. If there is no such character occurring N times, print -1 
as the output.

Boundary Condition(s):
2 <= Length of S <= 10^6

Input Format:
The first line contains the string S.
The second line contains the integer N.

Output Format:
The first line contains either the last character in the String that appears exactly N times or -1. 

Example Input/Output 1:
Input:
skillrack
2

Output:
k

Explanation:
Characters occurring 2 times are k l.
The last occurring character is k and hence it is printed as the output.

Example Input/Output 2:
Input:
-!!-==!-
3

Output:
-
"""
s=input().strip()
n=int(input())
count={}
ans=-1
for i in s:
    count[i]=count.get(i,0)+1
    if i==ans and count[i]>n:
        ans=-1
    elif count[i]==n:
        ans=i
print(ans)
