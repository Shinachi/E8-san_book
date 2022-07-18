def main():
    def f(x):
        cnt = 1
        while x >= 1:
            cnt *= x
            x-=1
        return cnt

    n, r = map(int, input().split())
    a = f(n)
    b = f(r)
    c = f(n-r)
    print(a//(b*c))
    
if __name__=='__main__':
    main()