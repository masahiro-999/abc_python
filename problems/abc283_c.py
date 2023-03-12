s = input()

count = 0
i = 0
while True:
    if i < len(s)-1 and s[i:i+2] == "00":
        i += 2
    else:
        i += 1
    count += 1
    if i == len(s):
        break
print(count)        

# 10888869450418352160768000001