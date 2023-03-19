H, W = map(int,input().split())

for i in range(H):
    a = list(map(int,input().split()))
    b = []
    for i in a:
        if i == 0:
            b.append(".")
        else:
            b.append(chr(64+i))
    print("".join(b))