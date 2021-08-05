import math

def taxi(radius):
    segment = radius * math.sqrt(2)
    S = segment*segment
    return S

def euclid(radius):
    S = math.pi*radius**2
    return S

radius = int(input())

euclidCircle = euclid(radius)
taxiCircle = taxi(radius)

print("%.6f" % euclidCircle)
print("%.6f" % taxiCircle)
