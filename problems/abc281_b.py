a = input()

def check():
    if len(a) != 8:
        return False
    if a[0] <"A" or a[0] > "Z":
        return False
    if a[7] <"A" or a[7] > "Z":
        return False
    for i in range(6):
        if a[i+1] <"0" or a[i+1] > "9":
            return False
    if a[1] == "0":
        return False
    return True

if check():
    print("Yes")
else:
    print("No")