unique_words = list()
fname = input('Enter file name:')
file_handle = open(fname)
for line in file_handle:
    words = line.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
unique_words.sort()
print(unique_words)
