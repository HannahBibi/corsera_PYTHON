from re import findall

try:
    file_handle = open('Macbeth.txt')
    s = file_handle.read().upper()
except:
    print('This file cannot be opened.')
finally:
    file_handle.close()

ladycount = 0
total = 0
words = findall('LADY MACBETH', s)
for word in words:
    ladycount = ladycount + 1

w = findall('MACBETH', s)
for macbeth in w:
    total = total + 1

onlymacbeth = total - ladycount


print(ladycount, total, onlymacbeth)
