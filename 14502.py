import copy
from collections import deque

N,M=map(int,input().split())

map_lst=[]
virus=[]
ret=0

cnt=0

def dfs(depth,var_y,var_x):
    global cnt
    global ret
    if depth==3:
        cnt+=1
        temp = copy.deepcopy(map_lst)
        queue = deque(copy.deepcopy(virus))
        while queue:
            target=queue.popleft()
            for dir in range(0, 4):
                if dir == 0:  # up
                    if target[0] - 1 >= 0 and temp[target[0] - 1][target[1]] == 0:
                        queue.append([target[0] - 1, target[1]])
                        temp[target[0] - 1][target[1]] = 2
                if dir == 1:  # right
                    if target[1] + 1 <= M - 1 and temp[target[0]][target[1] + 1] == 0:
                        queue.append([target[0], target[1] + 1])
                        temp[target[0]][target[1] + 1] = 2
                if dir == 2:  # down
                    if target[0] + 1 <= N - 1 and temp[target[0] + 1][target[1]] == 0:
                        queue.append([target[0] + 1, target[1]])
                        temp[target[0] + 1][target[1]] = 2
                if dir == 3:  # left
                    if target[1] - 1 >= 0 and temp[target[0]][target[1] - 1] == 0:
                        queue.append([target[0], target[1] - 1])
                        temp[target[0]][target[1] - 1] = 2
        safety=0
        for y_2 in range(N):
            for x_2 in range(M):
                if temp[y_2][x_2]==0:
                    safety+=1
        if safety>ret:
            ret=safety

        return
    else:
        for y in range(var_y,N):
            for x in range(var_x,M):
                if map_lst[y][x]==0:
                    map_lst[y][x]=1
                    dfs(depth+1,y,x)
                    map_lst[y][x]=0
            var_x=0

for loop in range(N):
    map_lst.append(list(map(int,input().split())))

for y_2 in range(N):
    for x_2 in range(M):
        if map_lst[y_2][x_2]==2:
            virus.append([y_2,x_2])

dfs(0,0,0)

print(ret)

