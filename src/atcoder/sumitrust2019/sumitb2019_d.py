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

s = input()

set1 = set()
set10 = set()
set100 = set()

for i in s:
    for j in set10:
        set100.add(j+i)
    for j in set1:
        set10.add(j+i)
    set1.add(i)

print(len(set100))