N, M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a1 = []
b1 = []

i = 1
pa= 0
pb= 0
while pa != len(a) or pb != len(b):
    if pa != len(a):
        if pb == len(b) or a[pa] < b[pb]:
            a1.append(i)
            i+=1
            pa += 1
            continue
    if pb != len(b):
        if pa == len(a) or a[pa] >= b[pb]:
            b1.append(i)
            i+=1
            pb += 1
            continue
print(*a1)
print(*b1)

