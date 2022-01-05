"""

Given a string S as input which consists of multiple words separated by a space, the program must print the count C of the words which are repeated exactly N times. The 
comparison of the words is case sensitive.

Input Format:
The first line contains S
The second line contains N

Output Format:
The first line contains C

Boundary Conditions:
1 <= Length of S <= 10000

Example Input/Output 1:
Input:
one two three four three two five
1

Output:
3

Explanation:
The words which are repeated only once are one, four and five. Hence the count is 3.

Example Input/Output 2:
Input:
one two three four three two five one five Three
2

Output:
4
"""
l=input().split()
c=int(input())
count={}
ans=0
for i in l:
    count[i]=count.get(i,0)+1
for i in count:
    if count[i]==c:
        ans+=1
print(ans)
