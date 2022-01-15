"""
As a final year project certain students in a college have designed a Robot which can move front, back, left or right in a given rectangular grid of dimension L*B units
(L denotes the length from left to right and B denotes the breadth from top to bottom). Always the robot moves in units which are of integer values. The robot cannot move 
outside the grid (That is the robot cannot go beyond L and B units). A sequence of N movement instructions are given to the robot to move in the desired direction 
(F-front or up, B-back or down, L-left, R-right) and the robot moves if the destination falls within the limit of the grid dimensions. Else the robot does not move. 
Assume the robot always starts at the bottom left of the grid. The program must print the number of movement instructions C for which the robot did not move (as the 
destination was outside the grid)

Input Format:
The first line contains L and B separated by a space.
The second line contains N which denotes the number of instructions.
The third line contains N instructions separated by one or more spaces.

Output Format:
The first line contains C which denoted the count of instructions for which the robot did not move.

Boundary Conditions:
1 <= L, B <= 999
1 <= N <= 999
C <= N

Example Input/Output 1:
Input:
6 5
9
3R 2L 11R 4F 4R 2F 3B 5L 4B

Output:
3

Explanation:
The robot did not move for the instructions 11R, 2F and 4B as they will make the robot go outside the grid.
"""
l,b=map(int,input().split())
n=int(input())
d=input().split()
c=0
col=0
row=b
for i in d:
    aa,bb=int(i[:-1]),i[-1]
    if bb=='F':
        if row-aa<0:
            c+=1
        else:
            row-=aa
    elif bb=='B':
        if row+aa>b:
            c+=1
        else:
            row+=aa
    elif bb=='L':
        if col-aa<0:
            c+=1
        else:
            col-=aa
    elif bb=='R':
        if col+aa>l:
            c+=1
        else:
            col+=aa
print(c)
