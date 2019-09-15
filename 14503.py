import copy

N,M=map(int,input().split())
cur=list(map(int,input().split()))
map_lst=[]
for loop in range(0,N):
    map_lst.append(list(map(int,input().split())))

mask=copy.deepcopy(map_lst)
res=0

def check():
    global res
    update=True
    while update:
        if mask[cur[0]][cur[1]]==0:
            mask[cur[0]][cur[1]]=2
        if mask[cur[0]][cur[1]-1]!=0 and mask[cur[0]-1][cur[1]] !=0 \
            and mask[cur[0]][cur[1] +1] != 0 and mask[cur[0]+1][cur[1]] != 0:
            if cur[2]==0:
                if mask[cur[0] + 1][cur[1]] != 1 and cur[0] + 1 < N:
                    cur[0]+=1
                else:
                    update=False
            if cur[2]==1:
                if mask[cur[0]][cur[1] - 1] != 1 and cur[1] - 1 >= 0:
                    cur[1]-=1
                else:
                    update = False
            if cur[2]==2:
                if mask[cur[0] - 1][cur[1]] != 1 and cur[0] - 1 >= 0:
                    cur[0]-=1
                else:
                    update=False
            if cur[2]==3:
                if mask[cur[0]][cur[1] + 1] != 1 and cur[1] + 1 < M:
                    cur[1]+=1
                else:
                    update=False
        else:
            #북
            if cur[2]==0:
                if mask[cur[0]][cur[1]-1]==0 and cur[1]-1>=0:
                    cur[2]=3
                    cur[1]-=1
                else:
                    cur[2] -= 1
                    if cur[2] < 0:
                        cur[2] = 3
            #동
            elif cur[2]==1:
                if mask[cur[0]-1][cur[1]] == 0 and cur[0] - 1 >= 0:
                    cur[2]=0
                    cur[0]-=1
                else:
                    cur[2] -= 1
                    if cur[2] < 0:
                        cur[2] = 3
            #남
            elif cur[2]==2:
                if mask[cur[0]][cur[1] +1] == 0 and cur[1] + 1 <M:
                    cur[2]=1
                    cur[1]+=1
                else:
                    cur[2] -= 1
                    if cur[2] < 0:
                        cur[2] = 3
            #서
            elif cur[2]==3:
                if mask[cur[0]+1][cur[1]] == 0 and cur[0] + 1 < N:
                    cur[2]=2
                    cur[0]+=1
                else:
                    cur[2] -= 1
                    if cur[2] < 0:
                        cur[2] = 3
check()

for y in range(N):
    for x in range(M):
        if mask[y][x]==2:
            res+=1

print(res)