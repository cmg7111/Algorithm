from collections import deque

M,N=map(int,input().split())
map_lst=[]
for loop in range(N):
    map_lst.append(list(map(int,input().split())))

queue=deque()
for i in range(N):
    for j in range(M):
        if map_lst[i][j]==1:
            queue.append([i,j])

dx=[0,-1,0,1]
dy=[-1,0,1,0]

def bfs():
    visited=[[0]*M for visited_make in range(N)]
    last=1
    while queue:
        cur=queue.popleft()
        visited[cur[0]][cur[1]]=1
        for dir in range(4):
            next_x=cur[1]+dx[dir]
            next_y=cur[0]+dy[dir]
            if 0<=next_x<M and 0<=next_y<N:
                if map_lst[next_y][next_x]==0:
                    if visited[next_y][next_x]==0:
                        map_lst[next_y][next_x]=map_lst[cur[0]][cur[1]]+1
                        queue.append([next_y,next_x])
                        visited[next_y][next_x]=1
                        last=map_lst[next_y][next_x]

    flag=True
    for loop1 in range(N):
        for loop2 in range(M):
            if map_lst[loop1][loop2]==0:
                flag=False
                break
        if flag==False:
            break

    if flag==False:
        last=0
    print(last-1)

bfs()