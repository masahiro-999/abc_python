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

H,M  = li()

def check(m):
    H, M = m//60, m%60
    a = H//10
    b = H%10
    c = M//10
    d = M%10
    return b < 6 and (a*10+c)<24
    
m = H*60+M
while True:
    if check(m) :
        print(m//60, m%60)
        break
    m += 1
    if (m==24*60):
        m=0