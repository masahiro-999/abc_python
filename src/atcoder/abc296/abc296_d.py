N,M = map(int, input().split())

inf = 2 ** 63 - 1

ans = inf 
s = int(M**0.5)

for a in range(1,inf):
    b = int((M+a-1)/a)
    if a > b:
        break
    if b <=N:
        ans = min(ans, a*b)

if ans != inf:
    print(ans)
else:
    print(-1)