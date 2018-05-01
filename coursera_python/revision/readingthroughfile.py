fhand = open('Macbeth.txt')
for line in fhand:
    n = line.strip()
    print(n.upper())
fhand.close()
