T=int(input())

dx=[-1,-2,-2,-1,1,2,2,1]
dy=[-2,-1,1,2,2,1,-1,-2]

def bfs(queue,target,visited):
    while queue:
        cur=queue.pop(0)
        if cur == target:
            print(visited[target[0]][target[1]])
            break
        else:
            for dir in range(8):
                next_x=cur[0]+dx[dir]
                next_y=cur[1]+dy[dir]
                if 0<=next_x<len(visited) and 0<=next_y<len(visited):
                    if visited[next_x][next_y]==0:
                        visited[next_x][next_y]=visited[cur[0]][cur[1]]+1
                        queue.append([next_x,next_y])

for case in range(T):
    row=int(input())
    queue=[]
    queue.append(list(map(int,input().split())))
    target=list(map(int,input().split()))

    map_lst = [[0] * row for loop in range(row)]
    visited = [[0] * row for loop in range(row)]

    bfs(queue,target,visited)


