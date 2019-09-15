N,M=map(int,input().split())
map_lst=[]
for loop in range(N):
    map_lst.append(list(map(int,input().split())))

max_ans=0
for y in range(N):
    for x in range(M):
        for case in range(5):
            #2개
            if case==0:
                if 0<=x+3<M:
                    sum=0
                    sum=map_lst[y][x]+map_lst[y][x+1]+map_lst[y][x+2]+map_lst[y][x+3]
                    max_ans=max(sum,max_ans)
                if 0<=y+3<N:
                    sum=0
                    sum= map_lst[y][x] + map_lst[y+1][x] + map_lst[y+2][x] + map_lst[y+3][x]
                    max_ans = max(sum, max_ans)
            if case==1:
                if 0<=x+1<M and 0<=y+1<N:
                    sum=0
                    sum=map_lst[y][x]+map_lst[y][x+1]+map_lst[y+1][x]+map_lst[y+1][x+1]
                    max_ans = max(sum, max_ans)
            if case==2:
                if 0<=y+2<N and 0<=x+1<M:
                    sum=0
                    sum=map_lst[y][x]+map_lst[y+1][x]+map_lst[y+2][x]+map_lst[y+2][x+1]
                    max_ans = max(sum, max_ans)
                    sum = map_lst[y][x] + map_lst[y + 1][x] + map_lst[y + 2][x] + map_lst[y][x + 1]
                    max_ans = max(sum, max_ans)
                    sum = map_lst[y][x+1] + map_lst[y + 1][x+1] + map_lst[y + 2][x+1] + map_lst[y][x]
                    max_ans = max(sum, max_ans)
                    sum = map_lst[y][x+1] + map_lst[y + 1][x+1] + map_lst[y + 2][x+1] + map_lst[y+2][x]
                    max_ans = max(sum, max_ans)
                if 0<=x+2<M and 0<=y+1<N:
                    sum = 0
                    sum = map_lst[y][x] + map_lst[y][x+1] + map_lst[y][x+2] + map_lst[y+1][x]
                    max_ans = max(sum, max_ans)
                    sum = map_lst[y][x] + map_lst[y][x+1] + map_lst[y][x+2] + map_lst[y+1][x+2]
                    max_ans = max(sum, max_ans)
                    sum = map_lst[y][x] + map_lst[y+1][x] + map_lst[y+1][x+1] + map_lst[y+1][x+2]
                    max_ans = max(sum, max_ans)
                    sum = map_lst[y+1][x] + map_lst[y+1][x+1] + map_lst[y+1][x+2] + map_lst[y][x+2]
                    max_ans = max(sum, max_ans)
            if case==3:
                if 0<=y+2<N and 0<=x+1<M:
                    sum=0
                    sum=map_lst[y][x]+map_lst[y+1][x]+map_lst[y+1][x+1]+map_lst[y+2][x+1]
                    max_ans = max(sum, max_ans)
                    sum = map_lst[y][x+1] + map_lst[y+1][x+1] + map_lst[y+1][x] + map_lst[y+2][x]
                    max_ans = max(sum, max_ans)
                if 0 <= x + 2 < M and 0 <= y + 1 < N:
                    sum = 0
                    sum = map_lst[y][x] + map_lst[y][x+1] + map_lst[y+1][x + 1] + map_lst[y + 1][x + 2]
                    max_ans = max(sum, max_ans)
                    sum = map_lst[y+1][x] + map_lst[y+1][x+1] + map_lst[y][x+1] + map_lst[y][x+2]
                    max_ans = max(sum, max_ans)
            if case==4:
                if 0 <= y + 2 < N and 0 <= x + 1 < M:
                    sum = 0
                    sum = map_lst[y][x] + map_lst[y + 1][x] + map_lst[y + 1][x + 1] + map_lst[y + 2][x]
                    max_ans = max(sum, max_ans)
                    sum = map_lst[y][x+1] + map_lst[y + 1][x + 1] + map_lst[y + 1][x] + map_lst[y + 2][x+1]
                    max_ans = max(sum, max_ans)
                if 0 <= x + 2 < M and 0 <= y + 1 < N:
                    sum = 0
                    sum = map_lst[y][x] + map_lst[y][x + 1] + map_lst[y + 1][x + 1] + map_lst[y][x + 2]
                    max_ans = max(sum, max_ans)
                    sum = map_lst[y+1][x] + map_lst[y + 1][x + 1] + map_lst[y][x + 1] + map_lst[y+1][x + 2]
                    max_ans = max(sum, max_ans)

print(max_ans)