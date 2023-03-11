s = input()

out = ""
for i in s:
    if i == "0":
        out += "1"
    else:
        out += "0"

print(out)