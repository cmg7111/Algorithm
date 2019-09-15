from collections import deque

M,N,H=map(int,input().split())
map_lst=[]
queue=deque()
for make_map_h in range(H):
    temp=[]
    for make_map_y in range(N):
        temp.append(list(map(int,input().split())))
        for input_x in range(M):
            if temp[make_map_y][input_x]==1:
                queue.append([make_map_h,make_map_y,input_x])
    map_lst.append(temp)

dx=[0,-1,0,1,0,0]
dy=[-1,0,1,0,0,0]
dh=[0,0,0,0,1,-1]

def bfs():
    visited=[[[0]*M for visited_make in range(N)] for loop in range(H)]
    last=1
    flag = True
    while queue:
        cur=queue.popleft()
        visited[cur[0]][cur[1]][cur[2]]=1
        for dir in range(6):
            next_x=cur[2]+dx[dir]
            next_y=cur[1]+dy[dir]
            next_h=cur[0]+dh[dir]
            if 0<=next_h<H and 0<=next_x<M and 0<=next_y<N:
                if map_lst[next_h][next_y][next_x]==0:
                    if visited[next_h][next_y][next_x]==0:
                        map_lst[next_h][next_y][next_x]=map_lst[cur[0]][cur[1]][cur[2]]+1
                        queue.append([next_h,next_y,next_x])
                        visited[next_h][next_y][next_x]=1
                        last=map_lst[next_h][next_y][next_x]

    for loop in range(H):
        for loop1 in range(N):
            for loop2 in range(M):
                if map_lst[loop][loop1][loop2]==0:
                    flag=False
                    break
            if flag==False:
                break
        if flag==False:
            break

    if flag==False:
        last=0
    print(last-1)

bfs()