import collections

N,L,R=map(int,input().split())
map_lst=[]
for loop in range(N):
    map_lst.append(list(map(int,input().split())))

queue=collections.deque()
dy=[-1,0,1,0]
dx=[0,1,0,-1]

temp = [[0] * N for i in range(N)]
visited = [[0] * N for i in range(N)]
chk=1
res=-1
update=True
while update==True:
    update=False
    chk = 1
    for y_1 in range(N):
        for x_1 in range(N):
            if temp[y_1][x_1]:
                continue
            if visited[y_1][x_1]:
                continue
            queue.append([y_1,x_1])
            while queue:
                cur=queue.popleft()
                visited[cur[0]][cur[1]] = 1
                for dir in range(0,4):
                    next_y=cur[0]+dy[dir]
                    next_x=cur[1]+dx[dir]
                    if 0<=next_y<N and 0<=next_x<N:
                        if visited[next_y][next_x]==0:
                            if L<=abs(map_lst[cur[0]][cur[1]]-map_lst[next_y][next_x])<=R:
                                update=True
                                temp[cur[0]][cur[1]]=chk
                                temp[next_y][next_x]=chk
                                queue.append([next_y,next_x])
                                visited[next_y][next_x] = 1
            chk += 1

    union=[0]*N*N
    cnt=[0]*N*N
    for y in range(N):
        for x in range(N):
            if temp[y][x]!=0:
                union[temp[y][x]-1]+=map_lst[y][x]
                cnt[temp[y][x]-1]+=1

    for y_2 in range(N):
        for x_2 in range(N):
            if temp[y_2][x_2]!=0:
                map_lst[y_2][x_2]=union[temp[y_2][x_2]-1]//cnt[temp[y_2][x_2]-1]
    #print(map_lst)
    temp = [[0] * N for i in range(N)]
    visited = [[0] * N for i in range(N)]
    res+=1

print(res)