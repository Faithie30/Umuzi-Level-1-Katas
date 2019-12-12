def frame(a):
    max_str = max(a, key = len)
    breadth = (len(max_str) + 4) * '*' 
    count = 0
    a_index = 0

    print(breadth)
    while count != len(a):
        spaces_left = (len(max_str)) - len(a[a_index])
        print('*', a[a_index], spaces_left * ' '+'*')
        count += 1; a_index += 1
    print(breadth)
