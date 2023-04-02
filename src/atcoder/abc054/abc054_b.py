N, M = map(int, input().split())

a = []
b = []

for i in range(N):
    s, = input().split()
    a.append(s)

for i in range(M):
    s, = input().split()
    b.append(s)

def match(i1,j1):
    for i in range(M):
        if a[i1+i][j1:j1+M] != b[i]:
            return False
    return True

for i in range(N-M+1):
    for j in range(N-M+1):
        if match(i,j):
            print("Yes")
            exit()

print("No")