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
a = li()

zero = False
min_a = inf
count = 0
sum = 0
for i in a:
    if i == 0:
        zero = True
    elif i < 0:
        count += 1
    min_a = min(min_a, abs(i))
    sum += abs(i)

if(zero):
    print(sum)
elif count % 2 == 1:
    print(sum - min_a*2)
else:
    print(sum)