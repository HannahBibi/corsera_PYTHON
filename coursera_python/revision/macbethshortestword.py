file_handle = open('Macbeth.txt')
shortest_word = '      '

for line in file_handle:
    l = line.split()
    for word in l:
        x = word.replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '').replace(' | ', '')
        if x == '':
            continue
        elif len(x) < len(shortest_word):
            shortest_word = x

print('[', shortest_word, ']')
file_handle.close()
