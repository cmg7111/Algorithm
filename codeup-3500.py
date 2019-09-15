from collections import deque

map_lst=[]
for loop in range(9):
    map_lst.append(list(map(int,input().split())))

bomb=[]
new_map=[[0]*9 for loop in range(9)]
dy=[-1,-1,0,1,1,1,0,-1]
dx=[0,-1,-1,-1,0,1,1,1]

dy_2=[-1,0,1,0]
dx_2=[0,-1,0,1]

r,c=map(int,input().split())

for y in range(9):
    for x in range(9):
        if map_lst[y][x]==1:
            for dir in range(8):
                next_y=y+dy[dir]
                next_x=x+dx[dir]
                if 0<=next_y<9 and 0<=next_x<9 and map_lst[next_y][next_x]==0:
                    new_map[next_y][next_x]+=1
            new_map[y][x]='_'

def print_map(lst):
    for map_y in range(9):
        for map_x in range(9):
            print(lst[map_y][map_x],end=" ")
        print()

def bfs():
    queue = deque()
    queue.append([r-1,c-1])
    visited=[[0]*9 for loop in range(9)]
    visited[r-1][c-1]=1
    while queue:
        cur=queue.popleft()
        for dir in range(8):
            next_y=cur[0]+dy[dir]
            next_x=cur[1]+dx[dir]
            if 0<=next_y<9 and 0<=next_x<9:
                if visited[next_y][next_x]==0:
                    if new_map[next_y][next_x]==0:
                        visited[next_y][next_x] = 1
                        queue.append([next_y, next_x])
                    elif map_lst[next_y][next_x]==0:
                        visited[next_y][next_x]=9
    #print("-----------")
    #print_map(visited)
    #print("-----------")
    for y_2 in range(9):
        for x_2 in range(9):
            if visited[y_2][x_2]==0:
                new_map[y_2][x_2]='_'
            print(new_map[y_2][x_2],end=" ")
        print()

if map_lst[r-1][c-1]==1:
    new_map=[['_']*9 for loop in range(9)]
    new_map[r-1][c-1]=-1
    for y_3 in range(9):
        for x_3 in range(9):
            print(new_map[y_3][x_3],end=" ")
        print()
elif map_lst[r-1][c-1]==0 and new_map[r-1][c-1]!=0:
    for y_4 in range(9):
        for x_4 in range(9):
            if y_4==r-1 and x_4==c-1:
                print(new_map[r-1][c-1],end=" ")
            else:
                print("_", end=" ")
        print()
else:
    bfs()