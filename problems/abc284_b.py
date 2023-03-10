t, = map(int,input().split())

for i in range(t):
    n, = map(int,input().split())
    a = map(int,input().split())
    count = 0
    for j in a:
        if j % 2 == 1:
            count+=1
    print(count)