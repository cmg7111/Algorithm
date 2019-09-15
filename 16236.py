N=int(input())

map_lst=[]
for i in range (N):
    map_lst.append(list(map(int,input().split())))

shark=[]
feed=[]
for y in range(N):
    for x in range(N):
        if map_lst[y][x]==9:
            shark=[y,x,2,0,0]
            map_lst[y][x]=0

dy=[-1,0,1,0]
dx=[0,-1,0,1]
res=0
def bfs():
    visited=[[0]*N for i in range(N)]
    res=0
    queue=[shark]
    while queue:
        cur=queue.pop(0)
        if 0<map_lst[cur[0]][cur[1]]<cur[2]:
            cur[3]+=1
            map_lst[cur[0]][cur[1]]=0
            if cur[3]==cur[2]:
                cur[2]+=1
                cur[3]=0
            res+=cur[4]
            cur[4]=0
            queue=[]
            visited=[[0]*N for i in range(N)]
        for dir in range(0,4):
            c_y=cur[0]+dy[dir]
            c_x=cur[1]+dx[dir]
            c_t=cur[4]+1
            #맵을 벗어나지 않음
            if 0<=c_y<N and 0<=c_x<N:
                if visited[c_y][c_x] == 0:
                    if 0<=map_lst[c_y][c_x] <= cur[2]:
                        visited[c_y][c_x]=1
                        queue.append([c_y,c_x,cur[2],cur[3],c_t])
                        queue.sort(key=lambda x:(x[4],x[0],x[1]))
    print(res)

bfs()
