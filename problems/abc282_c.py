N, = map(int,input().split())
S = input()

ans = ""
c = 0
for i in S:
    if  i == '"':
        c += 1
        print(i, end="")
        continue
    if i == "," and c % 2 == 0:
        print(".", end="")
        continue
    print(i, end="")
print("")