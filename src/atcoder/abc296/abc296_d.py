N,M = map(int, input().split())


ans = inf = 2 ** 63 - 1

s = int(M**0.5)

for a in range(1,s+1):
    if M/a <= N:
        b = int((M+a-1)/a)
        print(a*b)
        exit()
print(-1)