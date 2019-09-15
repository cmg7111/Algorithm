import copy
N,M=map(int,input().split())

map_lst=[]
for loop in range(N):
    map_lst.append(list(map(int,input().split())))
cctv=[]

cnt=0
for y in range(N):
    for x in range(M):
        if map_lst[y][x]!=0 and map_lst[y][x]!=6:
            cctv.append([y,x,map_lst[y][x],cnt])
            cnt+=1

temp_lst=[]
#print(map_lst)
#print(cctv)

res=999999999

def move(temp_map,cctv,dir):
    if dir==0:
        for y_0 in range(cctv[0],0,-1):
            if temp_map[y_0-1][cctv[1]]==6:
                break
            else:
                if temp_map[y_0-1][cctv[1]]==0:
                    temp_map[y_0-1][cctv[1]]='#'
    elif dir==1:
        for x_0 in range(cctv[1], M-1):
            if temp_map[cctv[0]][x_0+1] == 6:
                break
            else:
                if temp_map[cctv[0]][x_0+1] == 0:
                    temp_map[cctv[0]][x_0+1] = '#'
    elif dir==2:
        for y_1 in range(cctv[0], N-1):
            if temp_map[y_1 + 1][cctv[1]] == 6:
                break
            else:
                if temp_map[y_1 + 1][cctv[1]] == 0:
                    temp_map[y_1 + 1][cctv[1]] = '#'
    elif dir==3:
        for x_1 in range(cctv[1], 0,-1):
            if temp_map[cctv[0]][x_1-1] == 6:
                break
            else:
                if temp_map[cctv[0]][x_1-1] == 0:
                    temp_map[cctv[0]][x_1-1] = '#'

def dfs(depth):
    global temp_lst
    global res
    if depth==len(cctv):
        temp_res=0
        temp_map = copy.deepcopy(map_lst)
        for k in range(0,len(cctv)):
            if cctv[k][2]==1:
                move(temp_map,cctv[k],temp_lst[k])
            elif cctv[k][2]==2:
                if temp_lst[k]==0:
                    move(temp_map, cctv[k], 0)
                    move(temp_map, cctv[k], 2)
                else:
                    move(temp_map, cctv[k], 1)
                    move(temp_map, cctv[k], 3)
            elif cctv[k][2]==3:
                if temp_lst[k]==0:
                    move(temp_map, cctv[k], 0)
                    move(temp_map, cctv[k], 1)
                elif temp_lst[k]==1:
                    move(temp_map, cctv[k], 1)
                    move(temp_map, cctv[k], 2)
                elif temp_lst[k]==2:
                    move(temp_map, cctv[k], 2)
                    move(temp_map, cctv[k], 3)
                else:
                    move(temp_map, cctv[k], 3)
                    move(temp_map, cctv[k], 0)
            elif cctv[k][2] == 4:
                if temp_lst[k] == 0:
                    move(temp_map, cctv[k], 3)
                    move(temp_map, cctv[k], 0)
                    move(temp_map, cctv[k], 1)
                elif temp_lst[k] == 1:
                    move(temp_map, cctv[k], 0)
                    move(temp_map, cctv[k], 1)
                    move(temp_map, cctv[k], 2)
                elif temp_lst[k] == 2:
                    move(temp_map, cctv[k], 1)
                    move(temp_map, cctv[k], 2)
                    move(temp_map, cctv[k], 3)
                else:
                    move(temp_map, cctv[k], 2)
                    move(temp_map, cctv[k], 3)
                    move(temp_map, cctv[k], 0)
            elif cctv[k][2]==5:
                move(temp_map, cctv[k], 1)
                move(temp_map, cctv[k], 2)
                move(temp_map, cctv[k], 3)
                move(temp_map, cctv[k], 0)


        for y in range(N):
            for x in range(M):
                if temp_map[y][x]==0:
                    temp_res+=1
        res=min(res,temp_res)
        return
    else:
        if cctv[depth][2]==1:
            for j_1 in range(0,4):
                temp_lst.append(j_1)
                dfs(depth+1)
                temp_lst.pop()
        if cctv[depth][2]==2:
            for j_2 in range(0,2):
                temp_lst.append(j_2)
                dfs(depth+1)
                temp_lst.pop()
        if cctv[depth][2]==3:
            for j_3 in range(0,4):
                temp_lst.append(j_3)
                dfs(depth+1)
                temp_lst.pop()
        if cctv[depth][2]==4:
            for j_4 in range(0,4):
                temp_lst.append(j_4)
                dfs(depth+1)
                temp_lst.pop()
        if cctv[depth][2]==5:
            for j_5 in range(0,1):
                temp_lst.append(j_5)
                dfs(depth+1)
                temp_lst.pop()


dfs(0)

print(res)


