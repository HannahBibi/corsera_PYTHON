def multiply_list_items(l):
    multiple = None
    for i in l:
        if multiple is None:
            multiple = i
        else:
            multiple = multiple * i
    return multiple
