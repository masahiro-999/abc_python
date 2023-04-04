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
d = li()

def check(d):

    if d[0] != 0:
        return 0
    if len(d) == 1:
        return 1
    d = d[1:]
    d.sort()
    count = 1
    prev = d[0]
    if prev != 1:
        return 0
    ans = 1
    prev_count = 1
    for i in d[1:]:
        if prev == i:
            count += 1
        elif prev +1 == i:
            ans = (ans * (prev_count** count)) % mod
            prev = i
            prev_count = count
            count = 1
        else:
            return 0

    ans = (ans * (prev_count** count)) % mod

    return ans

print(check(d))