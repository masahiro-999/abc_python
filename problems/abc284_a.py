n, = map(int,input().split())
l = []
for i in range(n):
    l.append(input())

for i in range(n):
    print(l[n-i-1])
