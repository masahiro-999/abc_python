N,X = map(int,input().split())

A=[]
B=[]
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

dp = [[False for j in range(X+1)] for i in range(N)]

for i in range(N):
    for x1 in range(X+1):
        prev = 0
        for j in range(B[i]+1):
            if x1 < j*A[i]:
                break                    
            if i == 0:
                prev |= (x1 - j*A[i])==0
            else:
                prev |= dp[i-1][x1 - j*A[i]]
        dp[i][x1] = prev

if dp[N-1][X]:
    print("Yes")
else:
    print("No")
