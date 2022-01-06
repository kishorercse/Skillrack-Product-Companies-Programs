"""
The program must accept two string values S1 and S2 as the input. The program must find the absolute difference between the number of common characters and the number of
uncommon characters in the string values and print the value as the output.

Boundary Condition(s):
1 <= Length of S1, Length of S2 <= 10^6

Input Format:
The first line contains S1
The second line contains S2

Output Format:
The first line contains the positive integer value denoting the absolute difference

Example Input/Output 1:
Input:
abcdxyza
bcdxmnomm

Output:
2

Explanation:
Common characters are bcdx and the count is 4.
Uncommon characters are ayzmno and the count is 6.
Hence difference is 4-6 = -2. But as absolute difference is asked, the output is 2.

Example Input/Output 2:
Input:
aaaaaaaa
bbbbbbbcccccc

Output:
3
"""
a=input().strip()
b=input().strip()
d={} # char in one string = -1 or -2, char in both strings = 0
for i in a:
    d[i]=-1
for i in b:
    if d.get(i,-100)>=-1:
        d[i]=0
    else:
        d[i]=-2
common=uncommon=0
for i in d:
    if d[i]==0:
        common+=1
    else:
        uncommon+=1
print(abs(common-uncommon))
