N = int(input())
A = list(map(int, input().split()))
di = {}
for i in A:
    if i in di:
        di[i]+=1
    else:
        di[i]=1
        
if 100 in di and 400 in di:
    x=di[100]* di[400]
else:
    x=0
if 200 in di and 300 in di:
    y=di[200]* di[300]
else:
    y=0
    
print(x+y)