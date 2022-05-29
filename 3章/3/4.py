import collections

n = int(input())
li = list(map(int, input().split()))
c = collections.Counter(li)
print(li['100']* li['400'] + li['200']* li['300'])