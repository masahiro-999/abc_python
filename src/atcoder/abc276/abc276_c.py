# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
N = int(input())
a = list(map(int, input().split()))

for i in range(1,N):
    if a[N-i-1] > a[N-i]:
        break

def findmax(a, limit):
    max = -1
    for i in range(len(a)):
        if a[i] < limit:
            if max < a[i]:
                max = a[i]
                ret = i
    return ret

ret = findmax(a[N-i:], a[N-i-1]) + N-i
a[N-i-1], a[ret] = a[ret], a[N-i-1]

a[N-i:] = sorted(a[N-i:], reverse=True)

print(*a)