s = input()
t = input()

len_t = len(t)
for i in range((len(s)-len_t+1)):
    if s[i:i+len_t] == t:
        print("Yes")
        exit()
print("No")
