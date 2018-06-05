t0 = [1, 2, {'x': [10, 20, 30]}]
t1 = [1, 2, {'y': [40, 50, 60]}]
t2 = [1, 2, {'z': [70, 80, 90]}]


b = { ('a', 1), ('b', 2), ('c', 3)}

a = { 'a': t0, 'b': t1, 'c': t2 }

for k, v in a.items():
    d2 = v[2]
    l2 = d2.values()
    for y in d2.values():
        print(y[1])
