N, M= map(int, input().split())

a = list(map(int, input().split()))

a.sort()

bc = []
for i in range(M):
    b1, c1 =  map(int, input().split())
    bc.append((b1, c1))

s = 0
l = 0
bc.sort(key=lambda x:x[1], reverse=True)
for b,c in bc:
    while l < N:
        if a[l] >= c:
            break
        l = l+1
        b -= 1
        s += c
        if b == 0:
            break
s += sum(a[l:])

print(s)