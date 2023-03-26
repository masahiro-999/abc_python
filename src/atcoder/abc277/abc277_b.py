# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
N,  = map(int, input().split())

s=[]
for i in range(N):
    s.append(input())

for i in s:
    if i[0] not in ["H" , "D" , "C" , "S"]:
        print("No")
        exit()
    if i[1] not in [ "A" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K" ]:
        print("No")
        exit()

sets = set(s)
if len(sets) != len(s):
    print("No")
    exit()

print("Yes")
