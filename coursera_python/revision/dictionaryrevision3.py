a = {'a': [10, 20, 30],
     'b': [100, 101, 102],
     'c': [105, 104, 103]}

for k, v in a.items():
    current_sum = 0
    for i in v:
        current_sum = current_sum + i
    print(k, current_sum)
