"""
The program must accept N integers and an integer K as the input. The program must print the minimum possible sum of N integers by changing the last K bits of an integer to 0s
among the given N integers.

Boundary Condition(s):
2 <= N <= 100
1 <= Each integer value < 2^31
1 <= K <= 30

Input Format:
The first line contains N.
The second line contains N integer values separated by a space.
The third line contains K.

Output Format:
The first line contains an integer value representing the minimum possible sum of N integers.

Example Input/Output 1:
Input:
4
10 7 12 5
2

Output:
31

Explanation:
10 -> 1010
7 -> 0111
12 -> 1100
5 -> 0101
The four possible ways are given below.
(8) + 7 + 12 + 5 = 32
10 + (4) + 12 + 5 = 31
10 + 7 + (12) + 5 = 34
10 + 7 + 15 + (4) = 36
The minimum sum 31 is obtained by changing the last 2 bits of the 2nd integer to 0.

Example Input/Output 2:
Input:
7
81 52 17 3 31 7 10
3

Output:
194

Example Input/Output 3:
Input:
3
8 16 12
4

Output:
24
"""
n=int(input())
l=list(map(int,input().split()))
k=int(input())
res=0
ind=-1
maxDiff=-1
for i in range(n):
    t=(l[i]>>k)<<k
    diff=l[i]-t
    if diff > maxDiff:
        maxDiff=diff
        ind=i
        modify=t
l[ind]=modify
print(sum(l))
