import sys
from collections import deque, Counter, defaultdict
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353

N,X,Y = mi()

g = defaultdict(list)

for i in range(N-1):
    g[i].append(i+1)
    g[i+1].append(i)

g[X-1].append(Y-1)
g[Y-1].append(X-1)

ans = [0]*N
q = deque()
for i in range(N):
    d = {i:0}
    q.append(i)
    while q:
        j = q.popleft()
        for next in g[j]:
            if d.get(next, None) == None:
                d[next] = d[j]+1
                q.append(next)
    for i,c in d.items():
        ans[c] += 1

for k in range(1,N):
    a = ans[k]//2
    print(a)
