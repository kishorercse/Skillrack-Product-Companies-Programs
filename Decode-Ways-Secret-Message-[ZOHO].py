"""
A top secret message string S containing letters from A-Z (only upper case letters) is encoded to numbers using the following mapping:
'A' -> 1, 'B' -> 2 and so on till Z -> '26'

The program has to print the total number of ways in which the received message can be decoded.

Input Format:
The first line contains the string S containing numbers.

Output Format:
The first line contains the number of ways in which S can be decoded.

Boundary Conditions:
1 <= Length of S <= 100

Example Input/Output 1:
Input:
123

Output:
3

Explanation:
1-A 2-B 3-C 12-L 23-W.
Hence 123 can be decoded as ABC or AW or LC, that is in 3 ways.

Example Input/Output 2:
Input:
1290

Output:
0
"""
s=input().strip()
l=len(s)
dp=[0]*l
if s[0]!=0:
    dp[0]=1
for i in range(1,l):
    a=int(s[i])
    b=int(s[i-1:i+1])
    if a>=1 and a<=9:
        dp[i]+=dp[i-1]
    if b>=10 and b<=26:
        if i-2>=0:
            dp[i]+=dp[i-2]
        else:
            dp[i]+=1
print(dp[-1])
