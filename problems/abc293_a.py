s = input()

x =[ord(x) for x in s]

for i in range(1, len(s)//2+1):
    x[2*i-1-1],x[2*i-1] = x[2*i-1], x[2*i-1-1]


str = ""
for i in x:
    str += chr(i)

print(str)
