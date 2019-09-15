N,M,K=map(int,input().split())

adj_lst=[[] for loop in range(N)]
for loop in range(K):
    inp_1,inp_2,val=map(int,input().split())
    if inp_1<inp_2:
        adj_lst[inp_1-1].append([inp_2,val])

dp=[[0]*M for loop in range(N)]
for init in adj_lst[0]:
    dp[init[0]-1][1]=max(dp[init[0]-1][1],init[1])

for idx_chk,data_chk in enumerate(adj_lst):
    if idx_chk==0:
        continue
    for data in data_chk:
        for num in range(M-1):
            if dp[idx_chk][num]!=0:
                dp[data[0]-1][num+1]=max(dp[data[0]-1][num+1],dp[idx_chk][num]+data[1])

ans=dp[N-1]
ans.sort(reverse=True)
print(ans[0])