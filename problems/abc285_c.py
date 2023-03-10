s = input()

l = len(s)
offset = 1
for i in range(l-1):
    offset +=26 ** (i+1)


def az2int(s):
    sum = 0
    for i in range(len(s)):
        sum = (ord(s[i]) - ord('A')) + 26 * sum
    return sum

print(offset+az2int(s))