from collections import deque

M,N,K=map(int,input().split())

map_lst=[[0]*N for loop in range(M)]
for loop2 in range(K):
    x_1,y_1,x_2,y_2=map(int,input().split())
    for y in range(y_1,y_2):
        for x in range(x_1,x_2):
            map_lst[y][x]=1

dy=[-1,0,1,0]
dx=[0,-1,0,1]

queue=deque()
res=[]
def bfs():
    visited=[[0]*N for loop in range(M)]
    for chk_y in range(M):
        for chk_x in range(N):
            if visited[chk_y][chk_x]==0 and map_lst[chk_y][chk_x]==0:
                queue.append([chk_y, chk_x])
                visited[chk_y][chk_x]=1
                area=1
                while queue:
                    cur=queue.popleft()
                    for dir in range(4):
                        next_y=cur[0]+dy[dir]
                        next_x=cur[1]+dx[dir]
                        if 0<=next_y<M and 0<=next_x<N:
                            if map_lst[next_y][next_x]==0 and visited[next_y][next_x]==0:
                                visited[next_y][next_x]=1
                                queue.append([next_y,next_x])
                                area+=1
                res.append(area)

bfs()
res.sort()
print(len(res))
for data in res:
    print(data,end=" ")