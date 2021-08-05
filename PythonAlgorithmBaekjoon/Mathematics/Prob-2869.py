A, B, V = map(int, input().split())

#마지막 도착시에는 반드시 한번은 함
height = V - A

if height % (A-B) == 0:
    day = int(height/(A-B))
else:
    day = int(height/(A-B)+1)

print(day + 1)
