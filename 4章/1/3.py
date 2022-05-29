import math

x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

seg = math.sqrt((x1 - x2)** 2 + (y1 - y2)** 2)
if seg == r1 + r2:
    print(4)
elif seg < r1 + r2:
    print(3)
elif seg < abs(r1- r2):
    print(1)
elif seg == abs(r1-r2):
    print(2)
else:
    print(5)