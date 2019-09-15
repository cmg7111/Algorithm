N,M=map(int,input() .split())

house=[]
chic=[]
maplist=[]

temp=[]

def dfs(depth):
    global result
    if len(temp)==M:
        temp_dist=0
        print(temp)
        for i in range(0,len(house)):
            dist = 99999999999
            for j in range(0,len(temp)):
                dist=min(dist,abs(house[i][0]-temp[j][0])+abs(house[i][1]-temp[j][1]))
            temp_dist+=dist

        if result>temp_dist:
            result=temp_dist

        return

    for loop in range(depth,len(chic)):
        temp.append(chic[loop])
        dfs(loop+1)
        temp.pop()


for i in range(N):
    maplist.append(list(map(int,input().split())))

for y in range(N):
    for x in range(N):
        if maplist[y][x]==1:
            house.append([y,x])
        if maplist[y][x]==2:
            chic.append([y,x])
result=99999999
dfs(0)
print(result)