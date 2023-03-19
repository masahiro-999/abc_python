N, T = map(int,input().split())
a = list(map(int,input().split()))

s = sum(a)

t = T % s

sum = 0
for i in range(N):
    sum = sum + a[i]
    if t < sum:
        print(i+1, t-(sum-a[i]))
        break

