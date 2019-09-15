from collections import deque

n,m=map(int,input().split())
map_lst=[]
for loop in range(n):
    map_lst.append(list(map(int,input().split())))

dx=[0,-1,0,1]
dy=[-1,0,1,0]

def bfs():
    queue = deque()
    queue.append([0, 0])
    visited = [[0] * m for loop in range(n)]
    visited[0][0] = 1
    while queue:
        cur=queue.popleft()
        for dir in range(4):
            next_y=cur[0]+dy[dir]
            next_x=cur[1]+dx[dir]
            if 0<=next_y<n and 0<=next_x<m:
                if visited[next_y][next_x]==0:
                    if abs(map_lst[next_y][next_x]-map_lst[cur[0]][cur[1]])<=1:
                        queue.append([next_y,next_x])
                        visited[next_y][next_x]=visited[cur[0]][cur[1]]+1
    print(visited[n-1][m-1])
bfs()