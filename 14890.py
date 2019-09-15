N,L=map(int,input().split())
map_lst=[]
for i in range(N):
    map_lst.append(list(map(int,input().split())))

res=0

def checking(map_lst):
    global res
    for y in range(0,N):
        flag=True
        cnt=1
        make=1
        temp=[0]*N
        for x in range(0,N-1):
            #case1
            if map_lst[y][x]==map_lst[y][x+1]:
                cnt+=1
                #연속적인 경우를 저장
                make+=1
            #case2
            if map_lst[y][x]!=map_lst[y][x+1]:
                #높이 차이가 1 이상이면 무조건 불가능
                if abs(map_lst[y][x]-map_lst[y][x+1])>1:
                    flag=False
                else: #높이 차이가 1이면서
                    #낮은곳->높은곳
                    if map_lst[y][x]<map_lst[y][x+1]:
                        #범위 벗어남
                        if x-L<-1:
                            flag=False
                        elif make>=L:
                            idx=x
                            for loop in range(L):
                                if temp[idx]==1:
                                    flag=False
                                else:
                                    temp[idx]=1
                                idx-=1
                            make = 1
                        else:
                            flag=False
                    #높은곳->낮은곳
                    if map_lst[y][x]>map_lst[y][x+1]:
                        #범위 벗어남
                        if x+L>N-1:
                            flag=False
                        else:
                            idx = x+1
                            check=0
                            stack=set([])
                            chk_val = map_lst[y][idx]
                            for loop2 in range(L):
                                if map_lst[y][idx] == chk_val:
                                    if temp[idx]==0:
                                        check+=1
                                        stack.add(idx)
                                else:
                                    flag = False
                                idx += 1
                            if check==L:
                                for data in stack:
                                    temp[data]=1
        #case1
        if cnt==N:
            flag=True
        #최종 검사
        if flag==True:
            res+=1

checking(map_lst)

new_list = list(map(list, zip(*map_lst)))
checking(new_list)


print(res)