file_handle = open('Macbeth.txt')
longest_word = ' '
for words in file_handle:
    macbeth_list = words.split()
    for word in macbeth_list:
        if len(word) > len(longest_word):
            longest_word = word
file_handle.close()
print(longest_word)
