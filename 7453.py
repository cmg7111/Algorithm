n=int(input())
A=[]
B=[]
C=[]
D=[]

cnt=0

for loop in range(n):
    a,b,c,d=map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

res_AB=[]
res_CD=[]
for i in range(n):
    for j in range(n):
        res_AB.append(A[i]+B[j])
        res_CD.append(C[i]+D[j])

res_CD.sort()

def binary(target,CD):
    global cnt
    start=0
    end=len(CD)-1
    while start<=end:
        mid=(start+end)//2
        if CD[mid]==target:
            cnt+=1
            keep=mid
            while True:
                mid=mid-1
                if mid>=0:
                    if CD[mid]==target:
                        cnt+=1
                    else:
                        break
                else:
                    break
            while True:
                keep=keep+1
                if keep<=end:
                    if CD[keep]==target:
                        cnt+=1
                    else:
                        break
                else:
                    break
            return
        elif CD[mid]<target:
            start=mid+1
        else:
            end=mid-1

print(res_AB,res_CD)
for key in res_AB:
    binary(-key,res_CD)

print(cnt)