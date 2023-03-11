N, = map(int,input().split())
a = list(map(int,input().split()))

a = [i-1 for i in a]

f = {}

for i in range(N):
    if f.get(i, False) == False:
        f[a[i]] = True

result = []

for i in range(N):
    if f.get(i, False)==False:
        result.append(i+1)

print(len(result))
print(*result)

