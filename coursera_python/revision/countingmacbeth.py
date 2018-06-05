import re

file_handle = open('Macbeth.txt')
s = file_handle.read().upper()
file_handle.close()

total_words = re.findall('[a-zA-Z]+', s)
word_count = len(total_words)

macbeths = re.findall('MACBETH', s)
macbeth_count = len(macbeths)

percentage_of_macbeth = (macbeth_count / word_count) * 100
print(round(percentage_of_macbeth, 2), '%')
