N=int(input())
A=list(map(int,input().split()))
op=list(map(int,input().split()))

#print(N,A,op)

temp=[]

maximum=-9999999999
minimum=9999999999
def dfs(depth,var_i,var_j):
    global temp
    global maximum
    global minimum
    if depth==N-1:
        sum = A[0]
        #print(temp)
        for loop in range(0,len(temp)):
            if temp[loop]==0:
                sum+=A[loop+1]
            elif temp[loop]==1:
                sum-=A[loop+1]
            elif temp[loop]==2:
                sum*=A[loop+1]
            else:
                sum=int(sum/A[loop+1])
        #print(sum)
        maximum=max(sum,maximum)
        minimum=min(sum,minimum)
        return
    else:
        for i in range(var_i,N-1):
            for j in range(0,4):
                if op[j]>0:
                    op[j]-=1
                    temp.append(j)
                    dfs(depth+1,i+1,j)
                    op[j]+=1
                    temp.pop()
            var_j=0

dfs(0,0,0)

print(maximum)
print(minimum)