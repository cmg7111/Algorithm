N=int(input())
S=[]

for loop in range(N):
    S.append(list(map(int,input().split())))

member=set([i+1 for i in range(N)])
start=[]
link=[]
ret=9999999999

def dfs(depth,var_i):
    global ret
    if depth==N/2:
        start_sum = 0
        link_sum = 0
        link = list(member - set(start))
        print(start,link)
        for start_m1 in start:
            for start_m2 in start:
                if start_m1!=start_m2:
                    start_sum+=S[start_m1-1][start_m2-1]
        for link_m1 in link:
            for link_m2 in link:
                if link_m1!=link_m2:
                    link_sum+=S[link_m1-1][link_m2-1]
        print(start_sum,link_sum)
        ret=min(ret,abs(start_sum-link_sum))


        return
    else:
        for i in range(var_i,N):
            start.append(i+1)
            dfs(depth+1,i+1)
            start.pop()


#print(member)
#print(S)
#dfs로 팀을 짜는 경우의수 출력:
dfs(0,0)

print(ret)
