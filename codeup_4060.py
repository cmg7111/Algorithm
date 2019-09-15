M,N=map(int,input().split())

map_lst=[]
for loop in range(M):
    map_lst.append(list(map(int,input().split())))

dx=[0,-1,0,1]
dy=[-1,0,1,0]

def bfs():
    visited=[[0]*N for loop in range(M)]
    visited2=[[0] * N for loop in range(M)]
    cnt_1=0
    cnt_2=0
    for i in range(M):
        for j in range(N):
            if visited[i][j]==0 and map_lst[i][j]==0:
                queue = [[i,j]]
                while queue:
                    cur = queue.pop(0)
                    visited[cur[0]][cur[1]] = 1
                    for dir in range(4):
                        next_y=cur[0]+dy[dir]
                        next_x=cur[1]+dx[dir]
                        if 0<=next_y<M and 0<=next_x<N:
                            if visited[next_y][next_x]==0:
                                if map_lst[next_y][next_x]==0:
                                    visited[next_y][next_x]=1
                                    queue.append([next_y,next_x])
                cnt_1+=1

            elif visited2[i][j] == 0 and map_lst[i][j] == 1:
                queue = [[i, j]]
                while queue:
                    cur = queue.pop(0)
                    visited2[cur[0]][cur[1]] = 1
                    for dir in range(4):
                        next_y = cur[0] + dy[dir]
                        next_x = cur[1] + dx[dir]
                        if 0 <= next_y < M and 0 <= next_x < N:
                            if visited2[next_y][next_x] == 0:
                                if map_lst[next_y][next_x] == 1:
                                    visited2[next_y][next_x] = 1
                                    queue.append([next_y, next_x])
                cnt_2 += 1

    print(cnt_1,cnt_2)

bfs()