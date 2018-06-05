import re

file_handle = open('Macbeth.txt')
s = file_handle.read()
file_handle.close()
shortest_word = None
words = re.findall('[a-zA-Z]+', s)

for word in words:
    if shortest_word is None:
        shortest_word = word
    elif len(word) < len(shortest_word):
        shortest_word = word

print(shortest_word)
