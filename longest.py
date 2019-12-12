def longest(list_given):
    place = 0
    ans = 0
    word_collection = []
    word_collection.append(list_given[place])
    
    while place < len(list_given) - 1:
        place += 1
        if len(list_given[place]) == len(list_given[ans]):
            word_collection.append(list_given[place])
        elif len(list_given[place]) > len(list_given[ans]):
            word_collection.clear()
            word_collection.append(list_given[place])
            ans = list_given[place]
        else:
            pass
            
    print(word_collection)
