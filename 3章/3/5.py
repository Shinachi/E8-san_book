def func(x):
    return (x*(x-1))//2

n = int(input())
a = list(map(int, input().split()))
red, yel, blue = 0, 0, 0
for i in a:
    if i == 1:
        red += 1
    elif i == 2:
        yel += 1
    else:
        blue += 1
        
print(func(red)+func(yel)+func(blue))