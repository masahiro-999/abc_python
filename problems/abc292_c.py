# 正整数の組 
# (A,B,C,D) であって、
# AB+CD=N を満たすものの個数を求めてください。

N,  = map(int,input().split())

ans = 0

t = [0]*(N)

for a in range(1,N+1):
    for b in range(1,N+1):
        if a*b >= N:
            break
        t[a*b] += 1

ans = 0
for i in range(1, N):
    ans += t[i] * t[N-i]

print(ans)