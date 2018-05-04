import re

try:
    file_handle = open('Macbeth.txt')
except:
    print('File cannot be opened.')
    file_handle.close()

s = file_handle.read().upper()
file_handle.close()

longest_word = None

words = re.findall('[A-Z]+', s)
for word in words:
    if longest_word is None:
        longest_word = word
    elif len(word) > len(longest_word):
        longest_word = word
w = re.findall(longest_word, s)
total_count = len(w)

print(longest_word, total_count)
