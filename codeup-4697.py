from collections import deque

R=int(input())
map_lst=[]
for loop in range(R):
    map_lst.append(list(map(int,input().split())))

maximum=0
for max_y in range(R):
    for max_x in range(R):
        maximum=max(maximum,map_lst[max_y][max_x])

dx=[0,-1,0,1]
dy=[-1,0,1,0]

def bfs(limit,answer):
    visited=[[0]*R for loop in range(R)]
    cnt=0
    #print(limit)
    for y in range(R):
        for x in range(R):
            if map_lst[y][x]>limit and visited[y][x]==0:
                queue=deque()
                queue.append([y,x])
                visited[y][x]=1
                while queue:
                    cur=queue.popleft()
                    for dir in range(4):
                        next_y=cur[0]+dy[dir]
                        next_x=cur[1]+dx[dir]
                        if 0<=next_y<R and 0<=next_x<R:
                            if visited[next_y][next_x]==0:
                                if map_lst[next_y][next_x]>limit:
                                    queue.append([next_y,next_x])
                                    visited[next_y][next_x]=1
                cnt+=1

    answer=max(answer,cnt)
    return answer

answer=0
for case in range(maximum):
    answer=bfs(case,answer)

print(answer)