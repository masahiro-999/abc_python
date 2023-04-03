import sys
from collections import deque, Counter
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353

N, K = mi()
a = li()

s = 0
e = 0
sum = a[s]
ans = 0
while True:
    if sum >=K:
        ans += (N-e)
        sum -=a[s]
        s += 1
    else:
        e+=1
        if e == N:
            break
        sum += a[e]
print(ans)