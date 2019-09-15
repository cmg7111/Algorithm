from collections import deque

N=int(input())
M=int(input())

chk=[0]*101

relation=deque()
for loop in range(M):
    relation.append(list(map(int,input().split())))

print(relation)
lst=set()
while relation:
    cur=relation.popleft()
    for data in cur:
        print(data)
        chk[data]+=1
        for data2 in relation:
            if data in data2:
                lst.add(set(cur)|set(data2))
print(lst)