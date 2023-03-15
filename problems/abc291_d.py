N,  = map(int,input().split())

ab =[]

dp = [[0,0] for i in range(N)]
dp[0][0] = 1
dp[0][1] = 1


for i in range(N):
    a, b = map(int,input().split())
    ab.append((a,b))

for i in range(1,N):
    for j in range(2):
        for k in range(2):
            if ab[i-1][j] != ab[i][k]:
                dp[i][k] += dp[i-1][j]
 
    dp[i][0] %= 998244353
    dp[i][1] %= 998244353
    
ans = (dp[N-1][0] + dp[N-1][1]) % 998244353
print(ans)
