newlist = []

for i in range(10):
    val = int(input()) % 42
    if val in newlist:
        continue
    else:
        newlist.append(val)

print(len(newlist))
