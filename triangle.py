def triangle(n):
    count = n
    while n != 0:
        for i in range(n):
            print('#' * (count - (n - 1)))
            n -= 1
