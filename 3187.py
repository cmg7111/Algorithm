#input
R,C=map(int,input().split())

map_lst=[]
for y in range(R):
    map_lst.append(input())


#양 늑대 전체 수
total_wolf=0
total_sheep=0
for map_y in range(R):
    for map_x in range(C):
        if map_lst[map_y][map_x]=='v':
            total_wolf+=1
        if map_lst[map_y][map_x]=='k':
            total_sheep+=1

#북 서 남 동
dy=[-1,0,1,0]
dx=[0,-1,0,1]

def bfs():
    global total_wolf
    global total_sheep
    visited=[[0 for loop in range(C)] for loop2 in range(R)]

    for chk_y in range(R):
        for chk_x in range(C):
            queue=[[chk_x,chk_y]]
            wolf_cnt=0
            sheep_cnt=0
            while queue:
                cur=queue.pop(0)
                #이동
                for dir in range(0,4):
                    c_x=cur[0]+dx[dir]
                    c_y=cur[1]+dy[dir]
                    #조건 검사
                    if 0<=c_y<R and 0<=c_x<C:
                        if visited[c_y][c_x]==0:
                            if map_lst[c_y][c_x]!='#':
                                visited[c_y][c_x]=1
                                if map_lst[c_y][c_x]=='v':
                                    wolf_cnt+=1
                                if map_lst[c_y][c_x]=='k':
                                    sheep_cnt+=1
                                queue.append([c_x,c_y])

            #개체수 비교
            if sheep_cnt>wolf_cnt:
                total_wolf-=wolf_cnt
            else:
                total_sheep-=sheep_cnt

    print(total_sheep,total_wolf)

bfs()