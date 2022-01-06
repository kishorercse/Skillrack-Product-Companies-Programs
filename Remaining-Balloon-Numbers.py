"""
There are N filled balloons each painted with a random number B(i) where i is from 1 to N and the balloons are tied up to a rope in a straight line. M kids who play football
arrive and they decide to burst the balloons with the numbers divisible by their jersey numbers J(a) where a is from 1 to M. The program must print the numbers on the balloons
remaining after all M kids burst the balloons in the order of their occurrence. If none of the balloons are remaining then the program must print -1.

Input Format:
The first line contains N and M separated by a space.
The second line contains N positive integers which denote the numbers on the balloons separated by a space.
The third line contains M positive integers which denote the numbers on the jerseys separated by a space.

Output Format:
The first line contains the numbers on the remaining balloons separated by a space (or -1 if no balloons remain)

Boundary Conditions:
1 <= N <= 9999
1 <= M <= 20

Example Input/Output 1:
Input:
11 3
38 40 11 46 44 48 35 14 39 44 23
2 3 11

Output:
35 23

Explanation:
The 1st kid bursts balloons with numbers which are divisible by 2. So the balloons remaining are 11 35 39 23
The 2nd kid bursts balloons with numbers which are divisible by 3. So the balloons remaining are 11 35 23.
The 3rd kid bursts balloons with numbers which are divisible by 11. So the balloons remaining are 35 23.
"""
n,m=map(int,input().split())
b=list(map(int,input().split()))
j=list(map(int,input().split()))
count=n
for jnum in j:
    for ind in range(n):
        if b[ind]%jnum==0:
            b[ind]=-1
            count-=1
if count>0:
    for i in b:
        if i!=-1:
            print(i,end=' ')
else:
    print(-1)
