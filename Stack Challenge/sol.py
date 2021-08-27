def stack(n , start, to, mid):
    if n == 1:
        print("1 : ",start," --> ",to)
        return None
    stack(n-1, start, mid, to)
    print(n," : ",start," --> ",to)
    stack(n-1, mid, to, start)

 
n = int(input())
stack(n, 'A', 'C', 'B')
