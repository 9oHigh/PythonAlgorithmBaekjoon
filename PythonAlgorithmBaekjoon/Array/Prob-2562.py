newlist = []
for i in range(9):
    newlist.append(int(input()))

print(max(newlist))
print(newlist.index(max(newlist))+1)
