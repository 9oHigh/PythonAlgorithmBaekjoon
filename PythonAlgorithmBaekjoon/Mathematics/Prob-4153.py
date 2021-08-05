
def pytha(x, y, z):
    if x**2 + y**2 == z**2:
        return True
    elif y**2 + z**2 == x**2:
        return True
    elif z**2 + x**2 == y**2:
        return True
    return False

while True:
    x, y, z = map(int, input().split())
    
    if x == 0 and y == 0 and z == 0:
        break
    if pytha(x, y, z):
        print("right")
    else:
        print("wrong")
