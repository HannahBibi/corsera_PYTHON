def minimum(l):
    current_min = None
    for i in l:
        if current_min is None:
            current_min = i
        elif i < current_min:
            current_min = i
    return current_min
