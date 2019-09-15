N=int(input())
map_lst=[]

dx=[0,-1,0,1]
dy=[-1,0,1,0]

def bfs():
    visited=[[0]*N for loop in range(N)]
    comp=1

    for cur_x in range(N):
        for cur_y in range(N):
            flag=False
            cnt = 1
            queue=[[cur_x,cur_y]]
            if visited[cur_x][cur_y]==0:
                while queue:
                    cur=queue.pop(0)
                    for dir in range(4):
                        next_x=cur[0]+dx[dir]
                        next_y=cur[1]+dy[dir]
                        if 0<=next_x<N and 0<=next_y<N:
                            if visited[next_x][next_y]==0:
                                if map_lst[cur[0]][cur[1]] == '1':
                                    visited[cur[0]][cur[1]] = comp
                                    flag = True
                                    if map_lst[next_x][next_y]==map_lst[cur[0]][cur[1]]:
                                        visited[next_x][next_y]=comp
                                        queue.append([next_x, next_y])
                                        cnt += 1
                if flag==True:
                    comp+=1
                    res.append(cnt)

for i in range(N):
    map_lst.append(list(map(str,input())))

print(map_lst)

res=[]
bfs()

print(len(res))
res.sort()
for j in range(len(res)):
    print(res[j])