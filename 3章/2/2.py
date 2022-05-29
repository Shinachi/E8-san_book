def func(x, y):
   if x % y != 0:
       return func(y, x% y)
   else:
       return y
   
a = list(map(int, input().split()))
z = func(max(a[0], a[1], min(a[0], a[1])))
for i in range(2, len(a)):
    z = func(a[i], z)
    
print(z)