from collections import deque

K=int(input())
W,H=map(int,input().split())

map_lst=[]
for loop in range(H):
    map_lst.append(list(map(int,input().split())))

dy=[-2,-1,1,2,2,1,-1,-2]
dx=[-1,-2,-2,-1,1,2,2,1]
dy_k=[-1,0,1,0]
dx_k=[0,-1,0,1]

def bfs():
    visited=[[[0]*(K+1) for loop in range(W)] for loop in range(H)]
    queue = deque()
    queue.append([0, 0, 0])
    visited[0][0][0]=1
    flag=False
    last=0
    while queue:
        cur=queue.popleft()
        if cur[0]==H-1 and cur[1]==W-1:
            flag=True
            last=cur[2]
            break
        for dir_k in range(4):
            next_y_k=cur[0]+dy_k[dir_k]
            next_x_k=cur[1]+dx_k[dir_k]
            if 0<=next_y_k<H and 0<=next_x_k<W and map_lst[next_y_k][next_x_k]==0:
                if visited[next_y_k][next_x_k][cur[2]]==0:
                    visited[next_y_k][next_x_k][cur[2]]=visited[cur[0]][cur[1]][cur[2]]+1
                    queue.append([next_y_k,next_x_k,cur[2]])
        if cur[2]<K:
            for dir in range(8):
                next_y=cur[0]+dy[dir]
                next_x=cur[1]+dx[dir]
                if 0<=next_y<H and 0<=next_x<W and map_lst[next_y][next_x]==0:
                    if visited[next_y][next_x][cur[2]+1]==0:
                        visited[next_y][next_x][cur[2]+1]=visited[cur[0]][cur[1]][cur[2]]+1
                        queue.append([next_y,next_x,cur[2]+1])

    if flag==True:
        print(visited[H-1][W-1][last]-1)
    else:
        print("-1")

bfs()