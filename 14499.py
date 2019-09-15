N,M,y,x,K=map(int,input().split())

map_lst=[]
dice=[[0]*3 for i in range(0,4)]
dice[0][0]='X'
dice[0][2]='X'
dice[2][0]='X'
dice[2][2]='X'
dice[3][0]='X'
dice[3][2]='X'
for loop in range(0,N):
    map_lst.append(list(map(int,input().split())))
action=list(map(int,input().split()))

def rotate(dir):
    if dir==1: #동쪽
        temp = dice[1][2]
        dice[1][1:3] = dice[1][0:2]
        dice[1][0] = dice[3][1]
        dice[3][1] = temp
    if dir==2: #서쪽
        temp=dice[1][0]
        dice[1][0:2]=dice[1][1:3]
        dice[1][2]=dice[3][1]
        dice[3][1]=temp
    if dir==3: #북쪽
        temp=dice[0][1]
        for dir3 in range(0,3):
            dice[dir3][1]=dice[dir3+1][1]
        dice[3][1]=temp
    if dir==4: #남쪽
        temp=dice[3][1]
        for dir4 in range(3,0,-1):
            dice[dir4][1]=dice[dir4-1][1]
        dice[0][1]=temp

for move in range(0,len(action)):
    if action[move]==1:
        if x+1<=M-1:
            x+=1
        else:
            continue
    elif action[move]==2:
        if x-1>=0:
            x-=1
        else:
            continue
    elif action[move]==3:
        if y-1>=0:
            y-=1
        else:
            continue
    elif action[move]==4:
        if y+1<=N-1:
            y+=1
        else:
            continue
    rotate(action[move])
    if map_lst[y][x] != 0:
        dice[3][1] = map_lst[y][x]
        map_lst[y][x] = 0
    elif map_lst[y][x] == 0:
        map_lst[y][x] = dice[3][1]
    print(dice[1][1])