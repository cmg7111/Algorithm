R,C,T=map(int,input().split())
map_lst=[]

for loop in range(R):
    map_lst.append(list(map(int,input().split())))

dx=[0,-1,0,1]
dy=[-1,0,1,0]

dx_1=[1,0,-1,0]
dy_1=[0,-1,0,1]

dx_2=[1,0,-1,0]
dy_2=[0,1,0,-1]

cnt=0
pos=[]
while True:
    if cnt==T:
        break
    else:
        cnt+=1
        #미세먼지 파트
        add_lst=[[0]*C for loop in range(R)]
        for y in range(R):
            for x in range(C):
                if map_lst[y][x] > 0:
                    cnt_spread = 0
                    for dir in range(4):
                        next_y=y+dy[dir]
                        next_x=x+dx[dir]
                        if 0<=next_y<R and 0<=next_x<C and map_lst[next_y][next_x]!=-1:
                            add_lst[next_y][next_x]+=int(map_lst[y][x]/5)
                            cnt_spread+=1
                    map_lst[y][x]-=int(map_lst[y][x]/5)*cnt_spread
                if map_lst[y][x]==-1:
                    pos.append([y,x])
        for y2 in range(R):
            for x2 in range(C):
                map_lst[y2][x2]+=add_lst[y2][x2]

        #공기청정 파트
        for num in range(len(pos)):
            dir=0
            map_lst[pos[num][0]][pos[num][1]]=0
            stack=[[pos[num][0],pos[num][1],map_lst[pos[num][0]][pos[num][1]]]]
            if num == 0:
                while stack:
                    cur=stack.pop()
                    next_y=cur[0]+dy_1[dir]
                    next_x=cur[1]+dx_1[dir]
                    if next_y == pos[0][0] and next_x == pos[0][1]:
                        map_lst[cur[0]][cur[1]]=cur[2]
                        break
                    elif 0<=next_y<R and 0<=next_x<C:
                        stack.append([next_y,next_x,map_lst[cur[0]][cur[1]]])
                        map_lst[cur[0]][cur[1]]=cur[2]
                    else:
                        next_y-=dy_1[dir]
                        next_x-=dx_1[dir]
                        dir+=1
                        next_y+=dy_1[dir]
                        next_x+=dx_1[dir]
                        stack.append([next_y,next_x,map_lst[cur[0]][cur[1]]])
                        map_lst[cur[0]][cur[1]] = cur[2]
            if num==1:
                while stack:
                    cur=stack.pop()
                    next_y=cur[0]+dy_2[dir]
                    next_x=cur[1]+dx_2[dir]
                    if next_y == pos[1][0] and next_x == pos[1][1]:
                        map_lst[cur[0]][cur[1]] = cur[2]
                        break
                    elif 0<=next_y<R and 0<=next_x<C:
                        stack.append([next_y,next_x,map_lst[cur[0]][cur[1]]])
                        map_lst[cur[0]][cur[1]]=cur[2]
                    else:
                        next_y-=dy_2[dir]
                        next_x-=dx_2[dir]
                        dir+=1
                        next_y+=dy_2[dir]
                        next_x+=dx_2[dir]
                        stack.append([next_y,next_x,map_lst[cur[0]][cur[1]]])
                        map_lst[cur[0]][cur[1]] = cur[2]
sum=0
for map_y in range(R):
    for map_x in range(C):
        sum+=map_lst[map_y][map_x]

print(sum)