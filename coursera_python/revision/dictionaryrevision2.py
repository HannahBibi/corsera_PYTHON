a = {'a': [-10, -20, -30],
     'b': [-100, 101, -111],
     'c': [-105, -104, -103]}

maximum_num = None
key_of_largest_number = None

for k, v in a.items():
    for x in v:
        if maximum_num is None:
            maximum_num = x
            key_of_largest_number = k
        elif x > maximum_num:
            maximum_num = x
            key_of_largest_number = k

print(key_of_largest_number, maximum_num)
