n, = map(int, input().split())

if n%2 == 0:
    ans = 0
    i = 1
    while True:
        if n>=5**i*2:
            ans += n//(5**i*2)
            i += 1
        else:
            break
    print(ans)
else:
    print("0")