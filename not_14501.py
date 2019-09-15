N=int(input())
lst=[]


for loop in range(N):
    lst.append(list(map(int,input().split())))

lst.append([0,1])
maximum=0

dp=[[0]*N for loop2 in range(0,N)]


print(dp)
print(lst)



