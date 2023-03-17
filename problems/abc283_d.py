s = input()

inbox_array = []
def check(s):
    inbox = set()
    i = 0
    while i < len(s):
        if s[i] == "(":
            copy_inbox = set(inbox)
            inbox_array.append(copy_inbox)
            i += 1
            continue
        if s[i] == ")":
            inbox = inbox_array.pop()
            i += 1
            continue
        if s[i] in inbox:
            return False
        inbox.add(s[i])
        i += 1
    return True

if check(s):
    print("Yes")
else:
    print("No")

