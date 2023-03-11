def comp(a,b):
    if a != b:
        if a != "?" and b != "?":
            return False
    return True

s = input()
t = input()

lt = len(t)
def max_left(s, t):
    for x in range(len(t)):
        if comp(s[x],t[x]) == False:
            return x
    return x+1

x_left = max_left(s, t)
x_right = max_left(s[::-1], t[::-1])

for x in range(lt+1):
    if x > x_left or (lt-x) > x_right:
        print("No")
    else:
        print("Yes")

