from collections import defaultdict

# param
N,M = map(int, input().split())

d = defaultdict(list)

for i in range(M):
    a,b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

for i in range(1,N+1):
    ans = d[i][:]
    ans.sort()
    print(len(ans), *ans)
