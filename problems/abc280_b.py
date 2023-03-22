N, = map(int,input().split())

s = list(map(int,input().split()))

ans = [s[0]] + [s[i] -s[i-1] for i in range(1,N)]

print(*ans)