from collections import deque

W,H=map(int,input().split())

map_lst=[]
for loop in range(H):
    map_lst.append(input().split())

cnt=0
dy=[-1,-1,0,1,1,1,0,-1]
dx=[0,-1,-1,-1,0,1,1,1]

def bfs():
    global cnt
    queue=deque()
    visited=[[0]*W for loop in range(H)]
    for y in range(H):
        for x in range(W):
            if visited[y][x]==0 and map_lst[y][x]=='L':
                visited[y][x]=1
                queue.append([y,x])
                while queue:
                    cur=queue.popleft()
                    for dir in range(8):
                        next_y=cur[0]+dy[dir]
                        next_x=cur[1]+dx[dir]
                        if 0<=next_y<H and 0<=next_x<W:
                            if visited[next_y][next_x]==0 and map_lst[next_y][next_x]=='L':
                                queue.append([next_y,next_x])
                                visited[next_y][next_x]=1
                cnt+=1
bfs()
print(cnt)