map_lst=[]
for map_make in range(10):
    map_lst.append(list(input()))

queue=[]
queue.append(list(map(int,input().split())))

dx=[0,-1,0,1]
dy=[-1,0,1,0]

def bfs():
    while queue:
        cur=queue.pop(0)
        map_lst[cur[1]][cur[0]] = '*'
        for dir in range(4):
            next_x=cur[0]+dx[dir]
            next_y=cur[1]+dy[dir]
            if 0<=next_x<10 and 0<=next_y<10:
                if map_lst[next_y][next_x]=='_':
                    queue.append([next_x,next_y])

if map_lst[queue[0][1]][queue[0][0]]=='_':
    bfs()

for i in range(10):
    for j in range(10):
        print(map_lst[i][j],end='')
    print()