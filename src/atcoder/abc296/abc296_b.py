
for i in range(8):
    s, = input().split()
    a = s.find("*")     
    if a == -1:
        continue
    ans = chr(97+a)+f'{8-i}'
print(ans)
