from collections import deque

R,C=map(int,input().split())
map_lst=[]
queue_fire=deque()
queue_me=deque()
exit=[]

visited_me=[[0]*C for loop in range(R)]
for map_y in range(R):
    map_lst.append(list(map(str,input())))
    for map_x in range(C):
        if map_lst[map_y][map_x]=='J':
            queue_me.append([map_y, map_x])
            visited_me[map_y][map_x] = 1
        if map_lst[map_y][map_x]=='F':
            queue_fire.append([map_y,map_x])

dy=[-1,0,1,0]
dx=[0,-1,0,1]

flag=False
while queue_me:
    if flag==True:
        break
    else:
        for move_fire in range(len(queue_fire)):
            cur_fire = queue_fire.popleft()
            for dir in range(4):
                next_y_fire=cur_fire[0]+dy[dir]
                next_x_fire=cur_fire[1]+dx[dir]
                if 0<=next_y_fire<R and 0<=next_x_fire<C:
                        if map_lst[next_y_fire][next_x_fire]!='#' and map_lst[next_y_fire][next_x_fire]!='F':
                            map_lst[next_y_fire][next_x_fire]='F'
                            queue_fire.append([next_y_fire,next_x_fire])

        for move_me in range(len(queue_me)):
            if flag==True:
                break
            cur_me = queue_me.popleft()
            for dir in range(4):
                next_y_me=cur_me[0]+dy[dir]
                next_x_me=cur_me[1]+dx[dir]
                if next_y_me<0 or next_y_me>=R or next_x_me<0 or next_x_me>=C:
                    print(visited_me[cur_me[0]][cur_me[1]])
                    flag = True
                    break
                elif 0 <= next_y_me < R and 0 <= next_x_me < C:
                    if visited_me[next_y_me][next_x_me] == 0:
                        if map_lst[next_y_me][next_x_me] != '#' and map_lst[next_y_me][next_x_me]!='F':
                            visited_me[next_y_me][next_x_me] = visited_me[cur_me[0]][cur_me[1]]+1
                            queue_me.append([next_y_me, next_x_me])

if flag!=True:
    print("IMPOSSIBLE")