from collections import deque

map_lst=[]
for loop in range(19):
    map_lst.append(list(map(int,input().split())))

dx=[0,1,1,1]
dy=[1,1,0,-1]

flag_black=False
flag_white=False
def dfs_black(y,x,cnt,dir,pos):
    global flag_black
    next_y=y+dy[dir]
    next_x=x+dx[dir]
    if 0<next_y<19 and 0<next_x<19:
        if map_lst[next_y][next_x]==1:
            cnt += 1
            dfs_black(next_y,next_x,cnt,dir,pos)

    if cnt==5 and flag_black==False:
        over_y=next_y+dy[dir]
        over_x=next_x+dx[dir]
        if 0<over_y<19 and 0<over_x<19:
            if map_lst[next_y+dy[dir]][next_x+dx[dir]]!=1:
                flag_black=True
                print("1")
                print(pos[0],pos[1])
        else:
            flag_black = True
            print("1")
            print(pos[0], pos[1])

def dfs_white(y,x,cnt,dir,pos):
    global flag_white
    next_y=y+dy[dir]
    next_x=x+dx[dir]
    if 0<next_y<19 and 0<next_x<19:
        if map_lst[next_y][next_x]==2:
            cnt += 1
            dfs_white(next_y,next_x,cnt,dir,pos)

    if cnt == 5 and flag_white==False:
        over_y = next_y + dy[dir]
        over_x = next_x + dx[dir]
        if 0 < over_y < 19 and 0 < over_x < 19:
            if map_lst[next_y + dy[dir]][next_x + dx[dir]] != 2:
                flag_white = True
                print("2")
                print(pos[0], pos[1])
        else:
            flag_white = True
            print("2")
            print(pos[0], pos[1])

for y in range(19):
    for x in range(19):
        if flag_black==False and flag_white==False:
            if map_lst[y][x]==1:
                pos = [y+1, x+1]
                for dir in range(4):
                    cnt_black = 1
                    next_y=y+dy[dir]
                    next_x=x+dx[dir]
                    if 0<next_y<19 and 0<next_x<19:
                        if map_lst[next_y][next_x]==1:
                            if 0<=y-dy[dir]<19 and 0<=x-dx[dir]<19:
                                if map_lst[y-dy[dir]][x-dx[dir]]!=1:
                                    dfs_black(y, x, cnt_black, dir, pos)
                            else:
                                dfs_black(y, x, cnt_black, dir, pos)
            elif map_lst[y][x]==2:
                pos = [y + 1, x + 1]
                for dir in range(4):
                    cnt_white = 1
                    next_y=y+dy[dir]
                    next_x=x+dx[dir]
                    if 0<next_y<19 and 0<next_x<19:
                        if map_lst[next_y][next_x]==2:
                            if 0<=y-dy[dir]<19 and 0<=x-dx[dir]<19:
                                if map_lst[y-dy[dir]][x-dx[dir]]!=2:
                                    dfs_white(y,x,cnt_white,dir,pos)
                            else:
                                dfs_white(y, x, cnt_white, dir, pos)

if flag_white==False and flag_black==False:
    print("0")