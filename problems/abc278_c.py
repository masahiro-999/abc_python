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

N,Q  = li()

t = defaultdict(set)

for i in range(Q):
    q,a,b = mi()
    if q == 1 :
        t[a].add(b)
    elif q == 2 :
        try:
            t[a].remove(b)
        except:
            pass

    else:
        if b in t[a] and a in t[b]:
            print("Yes")
        else:
            print("No")
