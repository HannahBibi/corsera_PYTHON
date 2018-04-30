def max(l):
    current_max = None
    for i in l:
        if current_max is None:
            current_max = i
        elif i > current_max:
            current_max = i
    return current_max
