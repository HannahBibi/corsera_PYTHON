import re

file_handle = open('Macbeth.txt')
s = file_handle.read()
file_handle.close()
longest_word = ''
words = re.findall('[a-zA-Z]+', s)
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)
