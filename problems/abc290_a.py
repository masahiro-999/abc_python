N, M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

s = 0
for i in b:
    s += a[i-1]

print(s)