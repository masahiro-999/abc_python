n = input()
s = input()

def replace(s):
    if s == "":
        return ""
    if s[:2] =="na":
        return "nya" + replace(s[2:])
    else:
        return s[0] + replace(s[1:])

print(replace(s))
