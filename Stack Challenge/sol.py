def stack(n , source, destination, middle):
    if n == 1:
        print("1 from",source,"to",destination)
        return None
    stack(n-1, source, middle, destination)
    print(n,"from",source,"to",destination)
    stack(n-1, middle, destination, source)

 
n = int(input())
stack(n, 'A', 'C', 'B')
