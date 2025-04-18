import sys
input=sys.stdin.readline
INF=int(1e9)
dp=[INF]*((10**6)+1)
dp[1]=0
dp[2]=1
dp[3]=1

N=int(input())
for i in range(4,N+1):
    if i%3==0:
        dp[i]=dp[i//3]+1
    if i%2==0:
        dp[i]=min(dp[i//2]+1,dp[i])

    dp[i]=min(dp[i-1]+1,dp[i])

print(dp[N])