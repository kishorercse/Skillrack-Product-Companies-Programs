"""
The program must accept a string S as the input. The program must print only the most repeated characters in the string S as the output. If more than one character is repeated 
maximum number of times, then the characters must be printed in the order of their occurrence as the output. If there are no repeated characters in S, then the program must 
print S as the output.

Boundary Condition(s):
1 <= Length of S <= 100

Input Format:
The first line contains the value of S.

Output Format:
The first line contains the most repeated character in the order of their occurrences.

Example Input/Output 1:
Input:
apple

Output:
pp

Explanation:
The most repeated character is p which is occurred two times in apple.
Hence the output is pp

Example Input/Output 2:
Input:
#XRREETRE

Output:
RREERE
"""
s=input().strip()
count={}
mx=-1
for i in s:
    count[i]=count.get(i,0)+1
    mx=max(count[i],mx)
for i in s:
    if count[i]==mx:
        print(i,end='')
