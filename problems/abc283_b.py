n, = map(int,input().split())
a = list(map(int,input().split()))
q, = map(int,input().split())

for i in range(q):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        a[cmd[1]-1] = cmd[2]
    else:
        print(a[cmd[1]-1])
        