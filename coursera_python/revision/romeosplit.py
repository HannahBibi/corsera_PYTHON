file_hand = open('romeo.txt')
t = []
for line in file_hand:
    romeo_list = line.split()
    for word in romeo_list:
        if word not in t:
            t.append(word)
        else:
            continue
t.sort()
print(t)
file_hand.close()
