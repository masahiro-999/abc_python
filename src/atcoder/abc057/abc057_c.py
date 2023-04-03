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

N = ii()

def f(a,b):
    c = max(a,b)
    return len(f'{c}')

ans = inf
for a in range(1,int(N**0.5)+1):
    if N % a == 0:
        b = N//a
        l = f(a,b)
        ans = min(ans, l)

print(ans)
