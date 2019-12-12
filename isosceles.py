def isosceles(n):
    n=2
    i=0
    count = 1
    space = ' '
    times = n
    while i != n:
        print(space*times + count * '#')
        i+=1
        count += 2
        times -= 1
