# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
ans = -1
for str, i in zip(s, range(len(s))):
    if str == "a":
        ans = i+1

print(ans)