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

a,b = mi()

def f(a):
    i = 2
    s = set()
    stopval = a**0.5
    while i <= stopval:
        if a % i ==0:
            s.add(i)
        while a % i ==0:
            a = a//i
        i += 1
    if a >1:
        s.add(a)
    return s


sa = f(a)
sb = f(b)

s = sa & sb

print(len(s)+1)