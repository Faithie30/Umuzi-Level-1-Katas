def combine(a, b):
    ans = []
    a_index = 0; b_index = 0
    count = 0
    
    while count != len(a):
        ans.append(a[a_index]); ans.append(b[b_index])
        count += 1; a_index += 1; b_index += 1
    print(ans)
