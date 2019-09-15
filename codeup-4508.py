from collections import deque

N=int(input())
M=int(input())

relation_lst=[]
for loop in range(M):
    relation_lst.append(list(map(int,input().split())))

adj=[[] for loop in range(N)]

for make_adj in relation_lst:
    adj[make_adj[0]-1].append(make_adj[1])
    adj[make_adj[1]-1].append(make_adj[0])

res=[]

def bfs(start):
    queue=deque()
    visited=[0]*N
    visited[start-1]=1
    temp=set()
    queue.append(start)
    maximum=0

    while queue:
        cur=queue.popleft()
        temp.add(cur)
        for data in adj[cur-1]:
            if visited[data-1]==0:
                queue.append(data)
                visited[data - 1] = visited[cur - 1] + 1
                maximum=max(maximum,visited[data-1])

    if list(temp) not in res:
        res.append(list(temp))

    return maximum

result=[]
for exe in range(N):
    max_min=bfs(exe+1)
    result.append([max_min,exe+1])


answer=[]
for data1 in res:
    minimum=9999999
    flag=False
    for data2 in range(len(result)):
        if data2+1 in data1:
            minimum=min(minimum,result[data2][0])

    for data3 in range(len(result)):
        if data3+1 in data1:
            if result[data3][0]==minimum and flag==False:
                answer.append(result[data3][1])
                flag=True

print(len(answer))
answer.sort()
for ans in answer:
    print(ans)