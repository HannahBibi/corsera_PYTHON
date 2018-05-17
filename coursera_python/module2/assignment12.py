count = 0
fname = input("Enter file name:")
file_handle = open(fname)

for line in file_handle:
    if 'From ' in line:
        words = line.split()
        count = count + 1
        print(words[1])

print('There were', count, 'lines in the file with From as the first word')
