N,M=map(int,input().split())
A=[]
B=[]
for loop in range(4):
    if loop<2:
        A.append(list(map(int,input().split())))
    else:
        B.append(list(map(int,input().split())))

dx=[0,-1,0,1]
dy=[-1,0,1,0]

#A부터
def bfs_a():
    visited_a=[[0]*(N+1) for visited_make in range(M+1)]

    queue=[]
    queue.append([[A[0][1],A[0][0]],])
    print(queue)
    visited_a[A[0][1]][A[0][0]]=1
    print(visited_a)

    path=[]
    while queue:
        cur=queue.pop(0)
        if cur[0][0]==A[1][1] and cur[0][1]==A[1][0]:
            print("최단거리",visited_a[cur[0][1]][cur[0][0]])
            break
        else:
            for dir in range(4):
                next_x=cur[0][1]+dx[dir]
                next_y=cur[0][0]+dy[dir]
                if 0<=next_x<N+1 and 0<=next_y<M+1:
                    if visited_a[next_y][next_x]==0:
                        queue.append([[next_y,next_x],[cur[0][0],cur[0][1]]])
                        visited_a[next_y][next_x]=visited_a[cur[0][0]][cur[0][1]]+1
                        if next_x==A[1][0] and next_y==A[1][1]:
                            break


        print(queue)
print(A,B)

bfs_a()