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

N,  = li()
a = li()
Q, =li()

c = None
for i in range(Q):
    q = li()
    if q[0] == 1:
        c = q[1]
        a = defaultdict(lambda : c)
    elif q[0] == 2:
        a[q[1]-1] += q[2]
    else:
        print(a[q[1]-1])