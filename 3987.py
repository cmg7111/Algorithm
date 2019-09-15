N,M=map(int,input().split())
map_lst=[]
for make_map in range(N):
    map_lst.append(list(map(str,input())))

PR,PC=map(int,input().split())

dy=[-1,0,1,0]
dx=[0,1,0,-1]

data=["U","R","D","L"]

voyager=False
res=[]
def dfs(dir):
    global voyager
    stack = []
    stack.append([PR-1, PC-1])
    keep=dir
    cnt=1
    while stack:
        if cnt>500*500:
            voyager=True
            print(data[keep])
            print("Voyager")
            res.append([keep,"Voyager"])
            break
        cur=stack.pop()
        next_y=cur[0]+dy[dir]
        next_x=cur[1]+dx[dir]
        #범위 안
        if 0<=next_y<N and 0<=next_x<M:
            if map_lst[next_y][next_x]=='/' or map_lst[next_y][next_x]=='\\':
                if map_lst[next_y][next_x]=='/':
                    if dir==0:
                        dir=1
                    elif dir==1:
                        dir=0
                    elif dir==2:
                        dir=3
                    elif dir==3:
                        dir=2
                    cnt += 1
                    stack.append([next_y, next_x])
                elif map_lst[next_y][next_x]=='\\':
                    if dir==0:
                        dir=3
                    elif dir==1:
                        dir=2
                    elif dir==2:
                        dir=1
                    elif dir==3:
                        dir=0
                    cnt += 1
                    stack.append([next_y, next_x])
            else:
                cnt += 1
                stack.append([next_y,next_x])

    if voyager==False:
        res.append([keep,cnt])

for case in range(4):
    dfs(case)
    if voyager==True:
        break

if voyager==False:
    res.sort(key=lambda x:x[1],reverse=True)
    print(data[res[0][0]])
    print(res[0][1])