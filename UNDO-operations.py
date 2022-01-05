"""
The program must accept N series of keystrokes as string values as the input. The character ^ represents undo action to clear the last entered keystroke. The program must print
the string typed after applying the undo operations as the output. If there are no characters in the string then print -1 as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Length of each string <= 100

Input Format:
The first line contains the integer N.
The next N lines contain a string on each line.

Output Format:
The first N lines contain the string after applying the undo operations.

Example Input/Output 1:
Input:
3
Hey ^ goooo^^glee^
lucke^y ^charr^ms
ora^^nge^^^^

Output:
Hey google
luckycharms
-1

Example Input/Output 2:
Input:
2
batt^le^^
eu^^^^ropes^

Output:
bat
rope
"""
n=int(input())
for _ in range(n):
    s=input().strip()
    stack=[]
    for i in s:
        if i=='^':
            try:
                stack.pop()
            except IndexError:
                pass
        else:
            stack.append(i)
    if stack:
        print(''.join(stack))
    else:
        print(-1)
