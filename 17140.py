r,c,k=map(int,input().split())
MAX=100
map_lst=[[0]*MAX for loop in range(MAX)]

for loop in range(3):
    map_lst[loop][0],map_lst[loop][1],map_lst[loop][2]=map(int,input().split())

#print(map_lst)

cnt=0
col=3
row=3

while True:
    if map_lst[r-1][c-1]==k:
        print(cnt)
        break
    if cnt>100:
        print("-1")
        break
    else:
        if row>=col:
            maximum_col=0
            for y in range(row):
                chk_lst = [0]*100
                make_lst=[]
                for x in range(col):
                    if map_lst[y][x]!=0:
                        chk_lst[map_lst[y][x]-1]+=1
                        map_lst[y][x]=0
                for loop in range(100):
                    if chk_lst[loop]!=0:
                        make_lst.append([loop+1,chk_lst[loop]])
                make_lst.sort(key=lambda x:x[1])
                make_cnt=0
                maximum_col=max(maximum_col,len(make_lst)*2)
                for make_col in range(0,len(make_lst)*2,2):
                    map_lst[y][make_col]=make_lst[make_cnt][0]
                    map_lst[y][make_col+1]=make_lst[make_cnt][1]
                    make_cnt+=1
            col=maximum_col
            #print("row>=col",map_lst)
        else:
            maximum_row = 0
            for x_2 in range(col):
                chk_lst = [0] * 100
                make_lst = []
                for y_2 in range(row):
                    if map_lst[y_2][x_2] != 0:
                        chk_lst[map_lst[y_2][x_2] - 1] += 1
                        map_lst[y_2][x_2] = 0
                for loop_2 in range(100):
                    if chk_lst[loop_2] != 0:
                        make_lst.append([loop_2 + 1, chk_lst[loop_2]])
                make_lst.sort(key=lambda x: x[1])
                make_cnt = 0
                maximum_row = max(maximum_row, len(make_lst) * 2)
                for make_row in range(0, len(make_lst) * 2, 2):
                    map_lst[make_row][x_2] = make_lst[make_cnt][0]
                    map_lst[make_row+1][x_2] = make_lst[make_cnt][1]
                    make_cnt += 1
            row = maximum_row
            #print("col>row",map_lst)
        cnt+=1