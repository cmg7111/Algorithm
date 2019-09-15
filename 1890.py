N=int(input())
map_lst=[]
for loop in range(N):
    map_lst.append(list(map(int,input().split())))

route=[[0]*N for loop in range(N)]

route[0][0]=1
flag=True
for i in range(N):
    for j in range(N):
        if i==j and j==N-1:
            flag=False
        if route[i][j]!=0 and flag==True:
            next_x=j+map_lst[i][j]
            next_y=i+map_lst[i][j]
            if 0<next_x<N:
                route[i][next_x]+=route[i][j]
                #print(i,j,route)
            if 0<next_y<N:
                route[next_y][j]+=route[i][j]
                #print(i,j,route)

print(route[N-1][N-1])