import math

points = []

n = int(input("Enter number of points: "))

for i in range(n):
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    points.append((x, y))

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def farthest_point(points):
    farthest = points[0]
    maximum = distance((0, 0), points[0])

    for p in points:
        d = distance((0, 0), p)
        if d > maximum:
            maximum = d
            farthest = p

    return farthest

p1 = points[0]
p2 = points[1]

print("Distance:", distance(p1, p2))
print("Farthest Point:", farthest_point(points))