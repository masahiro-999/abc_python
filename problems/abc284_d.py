T, = map(int,input().split())

def solv(n):
    a = 0
    for i in range(2,n):
        if n % i == 0:
            a = i
            break

    if n % (a*a) == 0:
        return f'{a} {int(n//a//a)}'
    else:
        return f'{int((n // a) ** 0.5)} {a}'

for i in range(T):
    N, = map(int,input().split())
    print(solv(N))