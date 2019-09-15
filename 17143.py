R,C,M=map(int,input().split())
map_lst=[[0]*C for loop in range(R)]
shark=[]
for loop in range(1,M+1):
    i,j,s,d,z=map(int,input().split())
    shark.append([loop,i-1,j-1,s,d,z,0])
    map_lst[i-1][j-1]=loop

print(shark)
shark.sort(key=lambda x:x[0])

def move(y,x,speed,dir):
    if dir==1 or dir==2:
        speed=speed%(2*(R-1))
    elif dir==3 or dir==4:
        speed = speed % (2 * (C - 1))
    for loop in range(speed):
        if dir==1:
            n_y=y-1
            if n_y<0:
                dir=2
                y+=1
            else:
                y-=1
        elif dir==2:
            n_y=y+1
            if n_y>R-1:
                dir=1
                y-=1
            else:
                y+=1
        elif dir==3:
            n_x=x+1
            if n_x>C-1:
                dir=4
                x-=1
            else:
                x+=1
        elif dir==4:
            n_x=x-1
            if n_x<0:
                dir=3
                x+=1
            else:
                x-=1
    return y,x,dir

king_x=-1
sum=0
#print(map_lst)
while True:
    if king_x==C-1:
        break
    else:
        #낚시왕 이동
        king_x+=1
        # 낚시왕 잡기 O(R)
        for catch_y in range(R):
            if map_lst[catch_y][king_x]!=0:
                #print(map_lst[catch_y][king_x][0])
                sum+=shark[map_lst[catch_y][king_x]-1][5]
                shark[map_lst[catch_y][king_x]-1][6] = 1
                map_lst[catch_y][king_x]=0
                break

        #상어 이동 및 먹기 0=번호/1,2=좌표/3=속력/4=방향/5=크기/6=먹힌 여부 / O(R*C)
        map_lst = [[0]*C for loop in range(R)]
        for shark_loop in range(0,len(shark)):
            if shark[shark_loop][6]==0:
                shark[shark_loop][1],shark[shark_loop][2],shark[shark_loop][4]=move(shark[shark_loop][1],shark[shark_loop][2],shark[shark_loop][3],shark[shark_loop][4])
                if map_lst[shark[shark_loop][1]][shark[shark_loop][2]]==0:
                    map_lst[shark[shark_loop][1]][shark[shark_loop][2]]=shark_loop+1
                else:
                    if shark[map_lst[shark[shark_loop][1]][shark[shark_loop][2]]-1][5]>shark[shark_loop][5]:
                        shark[shark_loop][6]=1
                    else:
                        shark[map_lst[shark[shark_loop][1]][shark[shark_loop][2]]-1][6]=1
                        map_lst[shark[map_lst[shark[shark_loop][1]][shark[shark_loop][2]]-1][1]][shark[map_lst[shark[shark_loop][1]][shark[shark_loop][2]]-1][2]]=shark_loop+1
        print(shark)
print(sum)