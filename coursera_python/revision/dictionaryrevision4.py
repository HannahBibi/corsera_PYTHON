a = {'a': [10, 20, 30],
     'b': [100, 101, 102],
     'c': [105, 104, 103],
     'd': []}

for k, v in a.items():
    current_sum = 0
    c = len(v)
    if c == 0:
        current_sum = None
        print(k, current_sum)
    else:
        for i in v:
            current_sum = current_sum + i
        average_of_list = current_sum/c
        print(k, average_of_list)
