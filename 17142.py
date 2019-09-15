N,M=map(int,(input().split()))

map_lst=[]
for loop in range(N):
    map_lst.append(list(map(int,input().split())))

virus=[]
visited_lst=[[0]*N for visited_make in range(N)]
for i in range(N):
    for j in range(N):
        if map_lst[i][j]==2:
            virus.append([i,j])

minimum=99999999
virus_lst=[]

dx=[0,-1,0,1]
dy=[-1,0,1,0]

def bfs(chk_lst):
    queue=chk_lst[:]
    visited=[[0]*N for visited_make in range(N)]
    map_lst2=map_lst[:]
    for data in chk_lst:
        map_lst2[data[0]][data[1]]='*'

    last=0
    while queue:
        cur=queue.pop(0)
        for dir in range(4):
            next_x=cur[0]+dx[dir]
            next_y=cur[1]+dy[dir]
            if 0<=next_x<N and 0<=next_y<N:
                if visited[next_x][next_y]==0 and map_lst2[next_x][next_y]!=1 and map_lst2[next_x][next_y]!='*':
                    visited[next_x][next_y]=visited[cur[0]][cur[1]]+1
                    queue.append([next_x,next_y])
                    #last=visited[next_x][next_y]

    flag2=True
    for i2 in range(N):
        for j2 in range(N):
            if map_lst2[i2][j2]==1:
                visited[i2][j2]=-1
            if map_lst2[i2][j2]==2:
                visited[i2][j2]=-1
            if map_lst2[i2][j2]=='*':
                visited[i2][j2]=-1
            if visited[i2][j2]==0:
                flag2=False
            last = max(last, visited[i2][j2])

    if flag2==False:
        last=99999999
    #print(visited,last,flag2)

    return last

def dfs(depth,temp,idx):
    global minimum
    if depth==M:
        #바이러스 선택 완료
        time=bfs(temp)
        minimum=min(time,minimum)
        temp=[]
    else:
        for loop2 in range(idx,len(virus)):
            temp.append(virus[loop2])
            dfs(depth+1,temp,loop2+1)
            temp.pop()

temp=[]
dfs(0,temp,0)
#퍼질 수 없는 경우
if minimum==99999999:
    minimum=-1

print(minimum)