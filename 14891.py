saw=[]
for i in range(0,4):
    saw.append(input())
K=int(input())
rot=[]
for j in range(0,K):
    rot.append(list(map(int,input().split())))

# 1 (contact = 2(2)) / 2 (contact = 2(3), 6(1)) / 3 (contact = 2(4), 6(2)) / 4 (contact = 6(3))

def rotate(lst,dir):
    if dir==1:
        temp=lst[-1]
        lst=temp+lst[0:7]
    elif dir==-1:
        temp=lst[0]
        lst=lst[1:8]+temp
    return lst

#print(saw,K,rot)

for loop in range(0,K):
    rot_save = [0] * 4
    #첫 시작 톱니바퀴
    select=rot[loop][0]-1
    dir=rot[loop][1]
    rot_save[select]=dir
    #print("----")
    #print(saw,rot[loop])
    for left in range(select-1,-1,-1):
        select_left=left
        if saw[select][6]==saw[select_left][2]:
            break
        else:
            rot_save[select_left]=rot_save[select]*-1
            select=select_left
    select = rot[loop][0] - 1
    for right in range(select+1,4):
        select_right=right
        if saw[select][2]==saw[select_right][6]:
            break
        else:
            rot_save[select_right] = rot_save[select] * -1
            select = select_right

    for k in range(0,4):
        saw[k]=rotate(saw[k],rot_save[k])
    #print(rot_save)
    #print(saw)

print(int(saw[0][0])*1+int(saw[1][0])*2+int(saw[2][0])*4+int(saw[3][0])*8)
