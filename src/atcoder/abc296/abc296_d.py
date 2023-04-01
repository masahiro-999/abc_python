N,M = map(int, input().split())

s = int(M**0.5)

ans = inf = 2 ** 63 - 1


if N*N < M:
    print(-1)
    exit


for i in range(M,N*N+1):
    s = int(i**0.5)
    for j in range(1,min(s+1,N+1)):
        if i%j == 0 and i//j <= N:
            print(i)
            exit()
