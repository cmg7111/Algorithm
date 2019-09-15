N=int(input())

map_lst=[]
for loop in range(N):
    map_lst.append(input())

map_lst2=[]
for m2_x in range(N):
    temp=''
    for m2_y in range(N):
        if map_lst[m2_x][m2_y]=='G':
            temp+='R'
        else:
            temp+=map_lst[m2_x][m2_y]
    map_lst2.append(temp)

dy=[-1,0,1,0]
dx=[0,-1,0,1]

def bfs():
    case1=0
    case2=0
    visited_1=[[0 for loop in range(N)] for loop2 in range(N)]
    visited_2=[[0 for loop3 in range(N)] for loop4 in range(N)]
    for map_x in range(N):
        for map_y in range(N):
            queue=[[map_x,map_y]]
            if visited_1[map_x][map_y]==0:
                while queue:
                    cur = queue.pop(0)
                    color=map_lst[cur[0]][cur[1]]
                    visited_1[cur[0]][cur[1]]=1
                    for dir in range(4):
                        c_x=cur[0]+dx[dir]
                        c_y=cur[1]+dy[dir]
                        if 0 <= c_x < N and 0 <= c_y < N:
                            if visited_1[c_x][c_y]==0:
                                if map_lst[c_x][c_y]==color:
                                    visited_1[c_x][c_y] = 1
                                    queue.append([c_x,c_y])
                case1+=1

            queue2 = [[map_x, map_y]]
            if visited_2[map_x][map_y] == 0:
                while queue2:
                    cur = queue2.pop(0)
                    color = map_lst2[cur[0]][cur[1]]
                    visited_2[cur[0]][cur[1]] = 1
                    for dir in range(4):
                        c_x = cur[0] + dx[dir]
                        c_y = cur[1] + dy[dir]
                        if 0 <= c_x < N and 0 <= c_y < N:
                            if visited_2[c_x][c_y] == 0:
                                if map_lst2[c_x][c_y] == color:
                                    visited_2[c_x][c_y] = 1
                                    queue2.append([c_x, c_y])
                case2+=1
    print(case1, case2)

bfs()