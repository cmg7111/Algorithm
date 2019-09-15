from collections import deque
t=int(input())
res=[]

for case in range(t):
    n = int(input())
    me=list(map(int,input().split()))
    tar=[]
    for loop in range(0,n):
        tar.append(list(map(int,input().split())))
    tar.append(list(map(int,input().split())))

    queue=deque()
    queue.append(me)
    visited=[0]*(n+2)
    flag=False
    while queue:
        cur=queue.popleft()
        visited[0]=1
        for idx,data in enumerate(tar):
            if visited[idx+1]==0:
                dist=abs(data[0]-cur[0])+abs(data[1]-cur[1])
                if dist<=50*20:
                    visited[idx+1]=1
                    queue.append(data)
        if visited[n+1]==1:
            flag=True
            break

    if flag==True:
        res.append("happy")
    else:
        res.append("sad")

for result in res:
    print(result)