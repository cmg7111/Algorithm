n=int(input())
lst=list(map(int,input().split()))

dp=lst[:]

for loop in range(1,n):
    dp[loop]=max(dp[loop-1]+lst[loop],dp[loop])

print(dp)
dp.sort(reverse=True)
print(dp[0])