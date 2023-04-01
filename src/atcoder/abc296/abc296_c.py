N,X = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

X = abs(X)
s = 0
e = 0
while True:

    if a[e] - a[s] == X:
        print("Yes")
        break
    elif a[e] - a[s] < X:
        e+= 1
    elif a[e] - a[s] > X:
        s+= 1
    if e == N:
        print("No")
        break
