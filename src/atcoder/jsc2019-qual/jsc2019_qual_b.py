# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
N,K = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(N):
    right = 0
    for j in range(i+1, N):
        if a[i] > a[j]:
            right += 1

    left = 0
    for j in range(i):
        if a[i] > a[j]:
            left += 1
    
    ans += K*(K+1)*right//2 + K*(K-1)*left//2

ans %= 1000000007

print(ans)