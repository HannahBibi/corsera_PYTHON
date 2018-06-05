import re

try:
    file_handle = open('Macbeth.txt')
    s = file_handle.read().upper()
except:
    print('File cannot be opened.')
finally:
    file_handle.close()

words = re.findall(' [A-Z]{4,4} ', s)
s = set(words)
sortedset = sorted(s)
for word in sortedset:
    print(word)
