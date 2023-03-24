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

H,W = mi()
s=[input() for i in range(H)]
t=[input() for i in range(H)]

ss=[i for i in zip(*s)]
tt=[i for i in zip(*t)]

ss.sort()
tt.sort()

if ss != tt:
    print("No")
else:
    print("Yes")