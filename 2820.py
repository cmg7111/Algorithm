N,M=map(int,input().split())

emp_lst=[]
sub_lst=[set() for loop in range(N)]
for loop in range(N):
    if loop==0:
        emp_lst.append([int(input()),0])
    else:
        emp_lst.append(list(map(int,input().split())))
        sub_lst[emp_lst[loop][1]-1].add(loop+1)

def dfs(start,visited):
    stack=[start]
    while stack:
        cur=stack.pop()
        for node in sub_lst[cur-1]:
            if visited[node-1]==0:
                sub_lst[start-1].add(node)
                visited[node-1]=1
                stack.append(node)

for node in range(N):
    visited = [0] * N
    visited[node] = 1
    dfs(node+1,visited)

res=[]
for loop2 in range(M):
    input_query=list(map(str,input().split()))
    if input_query[0] == 'p':
        for emp in sub_lst[int(input_query[1]) - 1]:
            emp_lst[emp - 1][0] += int(input_query[2])
    elif input_query[0] == 'u':
        res.append(emp_lst[int(input_query[1]) - 1][0])

for data_out in res:
    print(data_out)