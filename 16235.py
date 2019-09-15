import copy
from collections import deque
N,M,K=map(int,input().split())

a=[]
for loop in range(N):
    a.append(list(map(int,input().split())))

queue=[]
for loop2 in range(M):
    x,y,z=map(int,input().split())
    queue.append([x,y,z,True])

map_lst=[[5]*(N+1) for i in range(N+1)]

dy=[-1,-1,-1,0,0,1,1,1]
dx=[-1,0,1,-1,1,-1,0,1]

year=0
new_queue=[]
for year in range(K):
    flag=True
    for season in range(0, 4):
        for cur in range(len(queue)):
            survivor=deque()
            if season==0:
                if map_lst[queue[cur][0]][queue[cur][1]] >= queue[cur][2] and queue[cur][3] == True:  # 양분 먹을 수 있음
                    map_lst[queue[cur][0]][queue[cur][1]] -= queue[cur][2]
                    queue[cur][2] += 1
                    survivor.append(cur)
                elif map_lst[queue[cur][0]][queue[cur][1]] < queue[cur][2]:  # 양분 못먹음
                    map_lst[queue[cur][0]][queue[cur][1]]+=queue[cur][2]//2
                cur=survivor
            elif season==2: #번식
                if queue[cur][2]%5==0 and queue[cur][3]!=False:
                    for make in range(0,8):
                        candi_y=queue[cur][0]+dy[make]
                        candi_x=queue[cur][1]+dx[make]
                        if 0<candi_y<=N and 0<candi_x<=N:
                            queue.append([candi_y,candi_x,1,True])

    for y in range(1,N+1):
        for x in range(1,N+1):
                map_lst[y][x]+=a[y-1][x-1]

#queue.sort(key=lambda x: (x[2]))

cnt=0
for y2 in range(len(queue)):
    if queue[y2][3]==True:
        cnt+=1
print(cnt)