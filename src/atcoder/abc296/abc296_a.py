N, = map(int, input().split())
s, = input().split()


prev = s[0]

for i in s[1:]:
    if prev ==i:
        print("No")
        exit()

    prev = i

print("Yes")
