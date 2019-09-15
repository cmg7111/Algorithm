N,M=map(int,input().split())
adj=[[] for loop in range(N)]
for loop in range(M):
    data=list(map(int,input().split()))
    adj[data[1]-1].append(data[0])

res=[]
def dfs(cur,cnt,visited):
    for node in adj[cur-1]:
        if visited[node-1]==0:
            visited[node-1]=1
            dfs(node,cnt+1,visited)
    return sum(visited)-1

def dfs2(node,cnt,visted):
    stack=[]
    stack.append(node)
    while stack:
        cur=stack.pop()
        for next in adj[cur-1]:
            if visited[next-1]==0:
                stack.append(next)
                visited[next-1]=1
    return sum(visited)-1

maximum=0
for input in range(N):
    visited = [0] * N
    visited[input]=1
    result=dfs2(input+1,1,visited)
    res.append([input+1,result])

maximum=0
for chk in res:
    if chk[1]>maximum:
        maximum=chk[1]

for chk_2 in res:
    if chk_2[1]==maximum:
        print(chk_2[0],end=" ")