H, W = map(int,input().split())
a = []
for i in range(H):
    x = list(map(int,input().split()))
    a.append(x)

def find_happy(i, j, history):
    if i==H-1 and j == W-1:
        if a[i][j] in history:
            return 0
        else:
            return 1
    if i == H:
        return 0
    if j == W:
        return 0
    if a[i][j] in history:
        return 0
    else:
        h1 = history[:]
        h1.append(a[i][j])
        h2 = history[:]
        h2.append(a[i][j])
        return find_happy(i+1, j, h1) + find_happy(i, j+1, h2)

result = find_happy(0, 0, [])
print(result)