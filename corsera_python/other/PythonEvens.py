def evens(l):
    count_evens = 0
    for i in l:
        if i % 2 == 0:
            count_evens = count_evens + 1
    return count_evens
